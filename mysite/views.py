from django.contrib.auth.models import User
from django.shortcuts import render

from friendship.models import Friend, Follow

# Create your views here.
def about(request):
    return render(request,"about1.html", {})

