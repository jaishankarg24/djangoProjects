from django.http import HttpResponse
from django.core.serializers import serialize
import json

class MixinHttpResponse(object):
	def render_to_http_response(self, json_data, status = 200):
		
		return HttpResponse(json_data, content_type='application/json', status=status)

class SerializeMixin(object):
	def serialize(self,student):
		json_data = serialize('json', student)
		dict_data = json.loads(json_data)
		complete_list_of_data = []

		for d in dict_data:
			student_data = d['fields']
			complete_list_of_data.append(student_data)

		json_data=json.dumps(complete_list_of_data)
		return json_data