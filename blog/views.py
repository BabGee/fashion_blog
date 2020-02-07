from django.views import generic
from .models import Post, Profile, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


def postList(request):
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    qset = Comment.objects.all()
    paginate_by = 3
    context = {
        'f3qs' : queryset[:3],
        '4thqs' : queryset[3],
        '5th6qs' : queryset[4:6],
        '7thqs' : queryset[6],
        'oldest' : queryset[7:11],
        'shishaa' : Profile.objects.filter(id=2).first(),
        '' : qset.filter(),
    }
    return render(request, template_name, context)


#class PostList(generic.ListView):
#    queryset = Post.objects.filter(status=1).order_by("-created_on")
#    template_name = "blog/index.html"
#    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'


def post_detail(request, slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

def about(request):
    context = {
        'babgee' : Profile.objects.filter(id=4).first() 
    }
    return render(request, 'blog/about.html', context)