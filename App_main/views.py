from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from App_main.forms import RoutineUploadForm, ClassVideoUploadForm, ClassNotesUploadForm
from App_main.models import Routine, ClassVideo, ClassNotes
from App_login.models import CustomUser, StudentInfo, TeacherInfo
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm


# Create your views here.
@login_required
def routine_sys(request):
    exist_routine = Routine.objects.all()  # All information from Routine table
    form = RoutineUploadForm()
    if request.method == 'POST':
        form = RoutineUploadForm(request.POST, request.FILES)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.Author = request.user
            routine.save()
            return HttpResponseRedirect(reverse('App_main:routine'))
    return render(request, 'App_main/Routine.html', context={'form': form, 'Routine': exist_routine})


@login_required
def class_video_sys(request):
    videos = ClassVideo.objects.all()
    form = ClassVideoUploadForm()
    if request.method == 'POST':
        form = ClassVideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            videoForm = form.save(commit=False)
            videoForm.Teacher = request.user
            videoForm.save()
            return HttpResponseRedirect(reverse('App_main:class-videos'))
    return render(request, 'App_main/ClassVideos.html', context={'form': form, 'Videos': videos})


@login_required
def class_notes_sys(request):
    classNote = ClassNotes.objects.all()
    form = ClassNotesUploadForm()
    if request.method == 'POST':
        form = ClassNotesUploadForm(request.POST, request.FILES)
        if form.is_valid():
            noteForm = form.save(commit=False)
            noteForm.Teacher = request.user
            noteForm.save()
            return HttpResponseRedirect(reverse('App_main:class-notes'))
    return render(request, 'App_main/ClassNotes.html', context={'form': form, 'classNote': classNote})


@login_required
def profile(request):
    return render(request, "App_main/Profile.html")


