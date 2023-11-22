from django.shortcuts import HttpResponse, render
from datetime import datetime
from post.models import Post
#e

def hello(requests):
    if requests.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date(requests):
    current_date = datetime.now()
    if requests.method == 'GET':
        return HttpResponse(current_date)


def goodbye(requests):
    if requests.method == 'GET':
        return HttpResponse("Goodbye user!")

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def post_view (request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context ={
            'post': posts
        }

        return render(request, 'post/post.html', context=context)