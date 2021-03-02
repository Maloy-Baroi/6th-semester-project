from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse


@login_required
def index(request):
    return render(request, 'FreeSchooling/Home.html')
