from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator,  PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} Pesan django" \
                        f"{post.title}"
            message = f"Membagikan {post.title} di alamat {post_url}\n\n" \
                        f"{cd['name']}\'s comments: {cd['comments']}"
            try:
                send_mail(subject, message, 'akhmadfaizal13@gmail.com', [cd['to']], fail_silently=False)
                sent = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent':sent})
    return render(request, 'blog/post/share.html')

def post_list(request):
    obj = Post.published.all()
    paginator= Paginator(obj, 4)
    page = request.GET.get('page')
    try:
    	post = paginator.page(page)
    except PageNotAnInteger:
    	post = paginator.page(1)
    except:
    	post = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': post, 'page': page})

def comment_list(request):
    comment = Comment.publishing.all()
    return render(request, 'blog/comment/comment.html', {'comments': comment})

def post_detail(request, year, month, day, post):
    posts = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = posts.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = posts
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, 'blog/post/detail.html',{'post': posts,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})
    return render(request, 'blog/post/detail.html',{'post': posts})