from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from testapp.models import StudyOnlineStudent

from django.http import HttpResponse
import json
from django.core.serializers import serialize
from testapp.mixins import *

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_data_json
from testapp.forms import StudentForm

@method_decorator(csrf_exempt, name='dispatch')
class StudentCrudCbv(MixinHttpResponse, SerializeMixin, View):

	def post(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json_data = json.dumps({'msg':'please send the valid json data'})
			return self.render_to_http_response(json_data, status = 400)
		student_data = json.loads(data)

		form = StudentForm(student_data)
		if form.is_valid():
			form.save(commit = True)
			json_data = json.dumps({'msg': 'Record Created Successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status = 400)

	def get_object_data_by_id(self, id):
		try:
			student = StudyOnlineStudent.objects.get(id=id)
		except StudyOnlineStudent.DoesNotExist:
			student = None
		return student

	def get(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)

		if not valid_json_data:
			json_data = json.dumps({'msg':'please send id in json'})
			return self.render_to_http_response(json_data, status=400)

		provided_id = json.loads(data)
		id = provided_id.get('id', None)
		if id is not None:
			student = self.get_object_data_by_id(id)
			if student is None:
				json_data = json.dumps({'msg':'No Record found for the id provided.'})
				return self.render_to_http_response(json_data, status = 404)
		student = StudyOnlineStudent.objects.get(id=id)
		print(student)
		student_data = {
		'student_name': student.student_name,
		'student_email': student.student_email,
		'student_phone_no': student.student_phone_no,
		'student_address': student.student_address
		}
		json_data = json.dumps(student_data)
		return self.render_to_http_response(json_data)



	def get(self,request,*args,**kwargs):
		data = request.body
		valid_json_data = is_data_json(data)

		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the id in json'})
			return self.render_to_http_response(json_data, status = 400)
		
		provided_id = json.loads(data)

		id = provided_id.get('id', None)
		if id is not None:
			student = self.get_object_data_by_id(id)
			if student is None:
				json_data = json.dumps({'msg':'No Record found for the id provided.'})
				return self.render_to_http_response(json_data, status=404)
			json_data = self.serialize([student,])
			return self.render_to_http_response(json_data)
		
		student = StudyOnlineStudent.objects.all()
		json_data = self.serialize(student)
		return self.render_to_http_response(json_data)

	

	def put(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data, status=400)

		provided_data = json.loads(data)

		id = provided_data.get('id', None)

		if id is None:
			json_data = json.dumps({'msg':'Please Provide the id'})
			return self.render_to_http_response(json_data, status=400)

		student = self.get_object_data_by_id(id)

		if student is None:
			json_data = json.dumps({'msg':'The Record is not available'})
			return self.render_to_http_response(json_data, status=404)

		original_data = {
			'student_name': student.student_name,
			'student_email': student.student_email,
			'student_phone_no': student.student_phone_no,
			'student_address': student.student_address
			}
		
		print('Data before Updation')
		print(original_data)

		print('Data After updation')
		
		original_data.update(provided_data)
		print(original_data)

		form = StudentForm(original_data, instance = student)
		if form.is_valid():
			form.save(commit = True)
			json_data = json.dumps({'msg':'Record Updated successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status = 400)

	def delete(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data, status = 400)

		provided_id = json.loads(data)

		id = provided_id.get('id', None)

		if id is not None:
			student = self.get_object_data_by_id(id)
			if student is None:
				json_data = json.dumps({'msg':'No Record found, Deletion not possible'})
				return self.render_to_http_response(json_data, status = 404)
			
			(status, deleted_item) = student.delete()
			if status == 1:
				json_data = json.dumps({'msg':'Record deleted successfully'})
				return self.render_to_http_response(json_data)
			json_data=json.dumps({'msg':'Deletion not successful'})
			return self.render_to_http_response(json_data)

		json_data = json.dumps({'msg':'Please Provide the id to delete'})
		return self.render_to_http_response(json_data, status = 400)
