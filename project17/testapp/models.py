from django.db import models

# Create your models here.
class StudyOnlineStudent(models.Model):
	student_name = models.CharField( max_length=50)
	student_email = models.CharField( max_length=50)
	student_phone_no = models.CharField( max_length=50)
	student_address = models.CharField( max_length=50)