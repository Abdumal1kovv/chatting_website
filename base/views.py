from django.shortcuts import render

# Create your views here.
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


def register(request):
    return render(request, 'login.html')

def public_feed(request):
    posts = Post.objects.all().order_by('-created')

    context = {'posts': posts}
    return render(request, 'feed.html', context)


@api_view(['POST'])
def add_post(request):
    data = request.data
    print("Data:", data)
    post = Post.objects.create(
        body=data['body']
    )

    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


