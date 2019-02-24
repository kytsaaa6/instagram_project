from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from posts.models import Post
from django.http import HttpResponse,HttpResponseRedirect


def comment_create(request, pk):
    # 요청 메서드가 POST방식 일 때만 처리
    if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = Post.objects.get(pk=pk)
        # request.POST에서 'content'키의 값을 가져옴
        content = request.POST.get('content')

        # 'content'키가 없었거나 내용이 입력되지 않았을 경우
        if not content:
            # 400(BadRequest)로 응답을 전송
            return HttpResponse('댓글 내용을 입력하세요', status=400)

        # 내용이 전달 된 경우, Comment객체를 생성 및 DB에 저장
        Comment.objects.create(
            post=post,
            # 작성자는 현재 요청의 사용자로 지정
            account=request.user,
            content=content
        )
        # 정상적으로 Comment가 생성된 후
        # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def comment_delete(request, pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=pk)
        comment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))  # 첫페이지로 이동하기


# Create your views here.
