from django import forms

from testapp.models import StudyOnlineStudent

class StudentForm(forms.ModelForm):

	class Meta:
		model = StudyOnlineStudent
		fields = '__all__'