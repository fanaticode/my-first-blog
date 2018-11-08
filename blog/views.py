from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def test(request):
	return render(request,'blog/test.html',{})

'''def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})'''


def post_detail(request,pk):
	Det_post=Post.objects.get(pk=pk)
	return render(request,'blog/post_detail.html',{'post':Det_post })


'''def home(request):
	return render(request, 'blog/home.html', {})'''