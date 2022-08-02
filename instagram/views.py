from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.tag_set #TODO
            post.save()
            messages.success(request,"포스팅을 저장했습니다.")
            return redirect("/") #TODO get_absolute_url 활용해보기
    else:
        form = PostForm() #get요청
    
    return render(request, "instagram/post_form.html" ,{
        "form":form,
    })

