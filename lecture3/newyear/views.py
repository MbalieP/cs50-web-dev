from django.shortcuts import render
from datetime import datetime  # Correct import
from django.http import HttpResponse

def index(request):
    now = datetime.now()  # Use datetime.now() directly
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })