from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required




def frontpage(request):
    return render(request, 'core/pages/landingpage.html')

