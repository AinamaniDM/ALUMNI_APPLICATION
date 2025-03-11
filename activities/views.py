
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required
def activity_list_view(request):
    return render(request, 'activities/activity_list.html', {'message': 'Activities coming soon!'})