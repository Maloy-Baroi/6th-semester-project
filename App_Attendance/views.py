import numpy as np
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from App_Attendance.forms import AttendanceForm
from App_Attendance.models import Attendance
import cv2
import face_recognition
from App_login.models import CustomUser, StudentInfo


# @login_required
# def attendance_sys(request):
#     attendance_info = Attendance.objects.all()
#     form = AttendanceForm()
#     if request.method == "POST":
#         form = AttendanceForm(request.POST)
#         if form.is_valid():
#             return testing(request, attendance_form=form)
#     return render(request, "App_Attendance/attendance.html", context={"form": form, 'attendance': attendance_info})


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


@login_required
def attendance_sys(request):
    # Get a reference to webcam #0 (the default one)
    student_roll = -1
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    images = []
    encodings = []
    names = []
    files = []
    studentIDs = []

    if not CustomUser.objects.all().filter(is_student=1):
        return render(request, "App_Attendance/attendance.html",
                      context={'No_student_data': 'No student attendance data'})

    prsn = CustomUser.objects.all().filter(is_student=1)
    form = AttendanceForm()
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attend_form = form.save(commit=False)
            for p in prsn:
                name = p.first_name + p.last_name
                images.append(name + '_image')
                encodings.append(name + '_face_encoding')
                files.append(str(p.profile_picture).replace("photos/profile_picture/", ""))
                names.append('Name: ' + name + ', Student ID: ' + p.Student.student_id)
                studentIDs.append(p.Student.student_id)

            filesFolder = []
            for i in files:
                filesFolder.append(cv2.imread(f"media/photos/profile_picture/{i}"))

            try:
                encodingList = findEncodings(filesFolder)
            except:
                messages.error(request, "Identification Error!!!")
                return HttpResponseRedirect(reverse('Home'))

            # Create arrays of known face encodings and their names
            known_face_encodings = encodingList
            known_face_names = names
            s_id = studentIDs
            while_runner = True
            while while_runner:
                # Grab a single frame of video
                ret, frame = video_capture.read()

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_frame = frame[:, :, ::-1]

                # Find all the faces and face enqcodings in the frame of video
                face_location = face_recognition.face_locations(rgb_frame)
                face_encoding = face_recognition.face_encodings(rgb_frame, face_location)

                # Loop through each face in this frame of video
                for face_encode, face_loc in zip(face_encoding, face_location):
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encode)

                    name = "Unknown"

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encode)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        s_id_best = s_id[best_match_index]
                        person = StudentInfo.objects.filter(student_id=s_id_best)
                        name = known_face_names[best_match_index] + ', Status: ' + "Present"
                        try:
                            student_roll = person.get().student_id
                        except:
                            attend_form.presence = 0

                while_runner = False
            if student_roll == -1:
                return HttpResponseRedirect(reverse('App_Attendance:attendance'))
            else:
                attend_form.student_id = student_roll
                attend_form.save()
            # form.student_id = student_roll
            # form.save()
            # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
            return render(request, 'App_Attendance/attendance.html')

    attendance_details = Attendance.objects.all()
    return render(request, "App_Attendance/attendance.html",
                  context={"form": form, 'attendance_details': attendance_details})
