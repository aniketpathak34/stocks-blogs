from audioop import reverse
from multiprocessing import context
from pickle import TRUE
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from yahoo_fin.stock_info import *
import time
import queue
from threading import Thread
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse

def LikeView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.remove(request.user)
        liked = True
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(slug)]))

# Create your views here.
def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, 'mainapp/stockpicker.html', {'stockpicker':stock_picker})

# @sync_to_async
# def checkAuthenticated(request):
#     if not request.user.is_authenticated:
#         return False
#     else:
#         return True

def stockTracker(request):
    # is_loginned = await checkAuthenticated(request)
    # if not is_loginned:
    #     return HttpResponse("Login First")
    stockpicker = request.GET.getlist('stockpicker')
    stockshare=str(stockpicker)[1:-1]
    
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50()
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    
    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    start = time.time()
    # for i in stockpicker:
    #     result = get_quote_table(i)
    #     data.update({i: result})
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args = (que, stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)
    end = time.time()
    time_taken =  end - start
    print(time_taken)
            
    
    print(data)
    return render(request, 'mainapp/stocktracker.html', {'data': data, 'room_name': 'track','selectedstock':stockshare})



class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name='addPost.html'
    # fields = '__all__'

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home1')
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'
    # fields = ['title', 'slug', 'content']
    # fields = '__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home1')

def get_context_data(self, *args, **kwargs):
    stuff = get_object_or_404(Post, id=self.kwargs['slug'])
    total_likes = stuff.total_likes()

    liked = False
    if stuff.likes.filter(id=self.request.user.id).exists():
        liked = True
    context["total_likes"] = total_likes
    context["liked"] = liked
    return context

