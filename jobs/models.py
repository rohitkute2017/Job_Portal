from django.db import models
from django.contrib.auth.models import User



class Job(models.Model):
    Designation = models.CharField(max_length=100)
    Orgnization_name = models.CharField(max_length=100)
    Experience = models.CharField(max_length=20)
    No_of_openings = models.IntegerField()
    Salary = models.CharField(max_length=20)
    Job_Description = models.TextField()
    Job_Location = models.CharField(max_length=100)
    Key_skills = models.TextField()
    Education = models.TextField()
    Employment_Type = models.CharField(max_length=100)
    About_company = models.TextField()
    HR_details = models.TextField()
    Job_Category = models.CharField(max_length=100)
    Link_to_apply = models.URLField(max_length=500)
    Perks = models.CharField(max_length=100)
    creater = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.Designation



