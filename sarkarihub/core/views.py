from django.shortcuts import get_object_or_404

def job_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'job_detail.html', {'post': post})
# About page view
def about(request):
    return render(request, 'about.html')
# Email subscription view
from .models import Subscriber
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def subscribe(request):
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        try:
            validate_email(email)
            if Subscriber.objects.filter(email=email).exists():
                message = 'You are already subscribed.'
            else:
                Subscriber.objects.create(email=email)
                message = 'Subscription successful! You will receive alerts for new posts.'
        except ValidationError:
            message = 'Please enter a valid email address.'
    return render(request, 'subscribe.html', {'message': message})


from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def home(request):
    query = request.GET.get('q', '').strip()
    if query:
        vacancy_posts = Post.objects.filter(category='vacancy', title__icontains=query).order_by('-created_at')
        admit_card_posts = Post.objects.filter(category='admit_card', title__icontains=query).order_by('-created_at')
        result_posts = Post.objects.filter(category='result', title__icontains=query).order_by('-created_at')
    else:
        vacancy_posts = Post.objects.filter(category='vacancy').order_by('-created_at')
        admit_card_posts = Post.objects.filter(category='admit_card').order_by('-created_at')
        result_posts = Post.objects.filter(category='result').order_by('-created_at')
    return render(request, 'home.html', {
        'vacancy_posts': vacancy_posts,
        'admit_card_posts': admit_card_posts,
        'result_posts': result_posts,
        'search_query': query,
    })


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


# New views for navbar links
def latest_jobs(request):
    posts = Post.objects.filter(category='vacancy').order_by('-created_at')
    return render(request, 'category_posts.html', {
        'posts': posts,
        'section_title': 'Latest Job 2025',
        'badge_class': 'bg-primary',
        'badge_label': 'Vacancy',
    })

def admit_cards(request):
    posts = Post.objects.filter(category='admit_card').order_by('-created_at')
    return render(request, 'category_posts.html', {
        'posts': posts,
        'section_title': 'Admit Card',
        'badge_class': 'bg-warning text-dark',
        'badge_label': 'Admit Card',
    })

def results(request):
    posts = Post.objects.filter(category='result').order_by('-created_at')
    return render(request, 'category_posts.html', {
        'posts': posts,
        'section_title': 'Results',
        'badge_class': 'bg-success',
        'badge_label': 'Result',
    })
