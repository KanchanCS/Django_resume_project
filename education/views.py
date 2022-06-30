from django.shortcuts import render
from .models import Skill
# Create your views here.
def skill(request):
    context = Skill.objects.all()
    return render(request, 'education/skill.html', {"context":context})