from django.shortcuts import render, get_object_or_404


def post_detail(request, pk):
    from driveapp.models import Post
    
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'driveapp/post_detail.html', {'post': post})
