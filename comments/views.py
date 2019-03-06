from django.http import HttpResponseRedirect
from posts.models import Post
from .models import Comment


def comment_create(request, pk):
    # 요청 메서드가 POST방식 일 때만 처리
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        content = request.POST.get('content')

        # 'content'키가 없었거나 내용이 입력되지 않았을 경우
        if not content:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        # 내용이 전달 된 경우, Comment객체를 생성 및 DB에 저장
        Comment.objects.create(
            post=post,
            # 작성자는 현재 요청의 사용자로 지정
            account=request.user,
            content=content
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def comment_delete(request, pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=pk)
        comment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
