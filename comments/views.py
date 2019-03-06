from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from posts.models import Post
from comments.models import Comment


def comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        content = request.POST.get('content')

        if not content:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        Comment.objects.create(
            post=post,
            account=request.user,
            content=content
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def comment_delete(request, comment_id):
    if request.method == 'GET':
        comments = Comment.objects.get(pk=comment_id)
        comments.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
