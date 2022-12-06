from django.shortcuts import render,get_object_or_404
from .models import Post, Comment
# Create your views here.
from django.utils import timezone
from django.views.generic import DetailView, UpdateView,DeleteView
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())

    return render(request,'test_app/post_list.html',{'posts':posts})


class NewsDetailView(DetailView):
    model= Post, Comment
    template_name='test_app/post_detail.html'
    context_object_name = 'post','comment'


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'test_app/create.html', {'form': form})


def post_update(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'test_app/create.html', {'form': form})


class NewsDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name='test_app/news_delete.html'

def post_comment(request,pk):
    error = ''
    post = get_object_or_404(Post,id=pk)
    comment = Comment.objects.filter(post=pk)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.post = post
            form.save()
            return redirect('post_list')
        else:
            error = 'Форма была неверной'
    return render(request, 'test_app/comment.html', {'comments':comment,'form':form,'error':error})


def post_detail(request,pk):

    post = get_object_or_404(Post,id=pk)
    comment = Comment.objects.filter(post=pk)
    count = len(comment)
    return render(request, 'test_app/post_detail.html',{'post': post,'count':count,'comments':comment})


def personal(request):
    comment = Comment.objects.filter(author=request.user)
    count = len(comment)
    return render(request, 'test_app/personal.html',{'count':count,'comments':comment})
# def post_list(request):
#    if request.method == 'POST':
#       id = request.POST.get('id', None)
#       form = PostForm()
#       if id:
#          try:
#             post = Post.objects.get(pk=id)
#          except ObjectDoesNotExist:
#             return () # обработка ошибки пост не найден
#          if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             form.post = post
#             form.save()
#             return () # все хорошо, коммент сохранен
#          return () # обработка ошибки форма не валидная
#       return () # обработка ошибки id не передан
#    # else здесь не обязательно писать код выполнится только если не ПОСТ
#    context = {
#       'form': CommentForm(),
#       'comments': Comment.objects.all()
#    }
#    return (request, 'text_app/post_detail.html', context) # return метод GET


