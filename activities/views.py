
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Activity
from members.models import Profile  

@login_required(login_url="/")
def activities_list(request):
    activities = Activity.objects.all().order_by('-date')  # Fetch activities sorted by date
    
    # Ensure the logged-in user has a profile
    current_user_profile = getattr(request.user, 'profile', None)
    if not current_user_profile:
        current_user_profile = Profile.objects.get_or_create(user=request.user)[0]
    current_user_profile.refresh_from_db()  # Force reload from the database
    
    return render(request, 'activities.html', {
        'activities': activities,
        'current_user_profile': current_user_profile
    })