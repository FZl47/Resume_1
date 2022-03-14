from django.db import models
from MyResume.Tools import GetDifferenceTime
import random


def UploadSrcImage(instance,path):
    N = random.randint(1,99999999999999999999999)
    return f"ImagesWorkSample/{N}/Image.{path.split('.')[-1]}"


class Skill(models.Model):
    Title = models.CharField(max_length=100)
    ValuePercent = models.CharField(max_length=5)

    def __str__(self):
        return self.Title


class WorkSample(models.Model):
    Title = models.CharField(max_length=200)
    Link = models.CharField(max_length=200)
    Image = models.ImageField(upload_to=UploadSrcImage)
    DateTimeField = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    Skills = models.TextField()

    def __str__(self):
        return self.Title

    def GetSkills(self):
        return self.Skills.split('-')

    def GetTimePast(self):
        return GetDifferenceTime(self.DateTimeField)



class MyInfo(models.Model):
    NameAndFamily = models.CharField(max_length=100)
    LabelWork = models.CharField(max_length=50)
    AboutMe = models.TextField()
    UserInstagram = models.CharField(max_length=100)
    UserTelegram = models.CharField(max_length=100)
    UserEmail = models.CharField(max_length=100)

    def __str__(self):
        return 'Fazel Momeni'

    def GetLenWorkSamples(self):
        return WorkSample.objects.count()

    def GetLenSkills(self):
        return Skill.objects.count()



