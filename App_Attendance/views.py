from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from App_Attendance.forms import AttendanceForm
from App_Attendance.models import Attendance


@login_required
def attendance_sys(request):
    attendance_info = Attendance.objects.all()
    form = AttendanceForm()
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('App_Attendance:attendance'))
    return render(request, "App_Attendance/attendance.html", context={"form": form, 'attendance': attendance_info})
