from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required
def news_list_view(request):
    return render(request, 'news/news_list.html', {'message': 'Posts coming soon!'})