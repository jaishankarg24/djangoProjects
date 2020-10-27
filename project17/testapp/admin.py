from django.contrib import admin

# Register your models here.
from testapp.models import StudyOnlineStudent

class StudyOnlineAdmin(admin.ModelAdmin):
	list_display = ['student_name', 'student_email', 'student_phone_no', 'student_address']

admin.site.register(StudyOnlineStudent, StudyOnlineAdmin)