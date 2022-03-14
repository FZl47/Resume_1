from django.shortcuts import render
from Information.models import WorkSample , MyInfo , Skill

def Home(request):
    Context = {}
    WorkSamples = WorkSample.objects.all().order_by('-id')
    Context['WorkSamples'] = WorkSamples
    Context['Skills'] = Skill.objects.all()
    Context['Info'] = MyInfo.objects.first()
    return render(request,'Home.html',Context)