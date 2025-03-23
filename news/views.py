# news/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from members.models import Profile

@login_required
def news_list_view(request):
    posts = Post.objects.all()
    
    # Ensure the logged-in user has a profile
    current_user_profile = getattr(request.user, 'profile', None)
    if not current_user_profile:
        current_user_profile = Profile.objects.get_or_create(user=request.user)[0]
    current_user_profile.refresh_from_db()  # Force reload from the database
    
    return render(request, 'news_list.html', {
        'news': posts,
        'current_user_profile': current_user_profile
    })