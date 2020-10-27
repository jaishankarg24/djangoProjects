import requests
import json
import sys

BASE_URl = 'http://127.0.0.1:8000/'
END_POINT = 'webapi/'


def create_data():
	student_name = input('Enter the Student Name :\t')
	student_email = input('Enter the Student email :\t')
	student_phone_no = input('Enter the Student phone number :\t')
	student_address = input('Enter the Student address :\t')

	student_data = {
		 'student_name': student_name, 'student_email': student_email, 'student_phone_no': student_phone_no, 'student_address': student_address
	}

	response = requests.post(BASE_URl + END_POINT, data = json.dumps(student_data) )
	print(response.status_code)
	print(response.json())

def select_single_data():
	id = input('Enter the id to select record :\t')
	data = {}
	if id is not None:
		data = {'id': id}
	response = requests.get(BASE_URl + END_POINT , data = json.dumps(data))
	print(response.status_code)
	print(response.json())

def select_complete_data(id = None):
	data = {}
	if id is not None:
		data  = {'id': id}
	response = requests.get(BASE_URl + END_POINT, data = json.dumps(data))
	print(response.status_code)
	print(response.json())

def update_partially():
	id = input('Enter the id to record data partially:\t')
	update_data = { 'id': id, 'student_phone_no': '9578631524', 'student_address': 'mysore'}
	response = requests.put(BASE_URl + END_POINT , data = json.dumps(update_data))
	print(response.status_code)
	print(response.json())

def update_completely():
	id = input('Enter the id to update record :\t')
	student_name = input('Enter the Student Name :\t')
	student_email = input('Enter the Student email :\t')
	student_phone_no = input('Enter the Student phone number :\t')
	student_address = input('Enter the Student address :\t')	

	update_data = { 'id': id, 'student_name': student_name, 'student_email':student_email, 'student_phone_no': student_phone_no, 'student_address': student_address}
	response = requests.put(BASE_URl + END_POINT , data = json.dumps(update_data))
	print(response.status_code)
	print(response.json())

def delete_data():
	id = input('Enter the id to delete record :\t')
	data = {'id': id}
	response = requests.delete(BASE_URl + END_POINT, data = json.dumps(data))
	print(response.status_code)
	print(response.json())
	
def exit():
	sys.exit()

def invalidOption():
	print('please provide valid option(1-7)')
	

if __name__ == '__main__':

	while(1):
		print(''' 
			Please Select the below operation.
			1. Create the data.
			2. Select single data.
			3. Select complete data.
			4. Update partially.
			5. Update Completely.
			6. Delete the data.
			7. To Exit.
			 ''')

		choice = int(input('Enter your choice(number):'))

		options = {
			1: create_data,
			2: select_single_data,
			3: select_complete_data,
			4: update_partially,
			5: update_completely,
			6: delete_data,
			7: exit
		}
		options.get(choice, invalidOption)()


