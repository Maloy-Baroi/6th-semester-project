from django.shortcuts import render, HttpResponseRedirect, reverse
from App_test.forms import MCQForm
from App_test.models import MCQ


# Create your views here.
def mutiple_choice_quiz(request):
    mcq = MCQ.objects.all()
    return render(request, "App_test/mcqTest.html", context={'exam': mcq})
