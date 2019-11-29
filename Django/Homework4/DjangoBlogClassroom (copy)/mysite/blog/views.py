from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostFrom
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, y, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=y,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html',
                  {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} recommends you to read'.format(cd['name'])
            message = ' Read at {} '.format(post_url)
            send_mail(subject, message, 'admin@myblog.com', [cd['to']],fail_silently=True)
            sent = True

    else:
        form = EmailPostFrom()

    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})

@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html', {'section': 'dashboard'})


