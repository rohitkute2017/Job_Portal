from django.db import models


# Create your models here.
Gender_male = 'Male'
Gender_Female = 'Female'
Gender_Choices = (
                (Gender_male,'Male'),
                (Gender_Female,'Female'),
)

Status_Pending = 'Pending'
Status_Accedpted = 'Accepted'
Statuse_Rejected = 'Rejected'
Status_Choices = ((Status_Pending, 'Pending'),
                 (Status_Accedpted, 'Accepted'),
                 (Statuse_Rejected, 'Rejected')
                 )

class employee(models.Model):
    """
    Name 
    Qualification
    Gender
    Mobile
    City 
    Salary Expectation
    Current Location
    Preferrable Location

    """
    Name = models.CharField(max_length=100)
    Qualification = models.TextField()
    Gender = models.CharField(max_length=20,choices=Gender_Choices,default=Gender_male)
    Mobile = models.IntegerField()
    City = models.CharField(max_length=20)
    Salary_Expectation = models.CharField(max_length=50)
    Current_Locatin = models.CharField(max_length=20)
    Preferrable_Location = models.CharField(max_length=500)


    def __str__(self):
        
        return "{} - {}".format(self.Name, self.Mobile)

class Employeejobmap(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.job',on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status_Choices, default=Status_Pending)
    Feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.employee.Name, self.job.Designation)
