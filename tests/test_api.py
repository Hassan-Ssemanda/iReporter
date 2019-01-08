import pytest, json, unittest, run, json, datetime
from ireporter import api 
from flask_testing import TestCase

class TestMainFlask(TestCase):

	def create_app(self):
		return run.app

	def test_get_redflags(self):
		response = self.client.get('/redflags')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(len(data['data']),0)

	def test_get_redflag(self):
		response = self.client.get('/redflags/2')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{
            'id': 2,
            'type': 'redflag',
            'comment': 'Learn Python',
            'images': 'image2',
            'videos': 'video2',
            'location': 'location cordinates',
            'status': 'draft',
            "createdOn": "Wed, 02 Jan 2019 16:36:03 GMT"})


	def test_create_redflag(self):
		response = self.client.post('/redflags',
                                        content_type='application/json',
                                        data=json.dumps(dict(
                                        images = 'testimage',
                                        videos = 'testvideo',                                       					 type='Red-Flag',
                                        location='45,67',
                                        comment='comment3'
                                        )))


		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['data'],[{'id':3,'message': 'Successfully created'}])


	def test_update_redflag(self):
			response = self.client.put('/redflags/2',
	                                     content_type='application/json',
	                                     data=json.dumps(dict(Location='7,7')))



			data = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)
			self.assertEqual(data['data'],[{'id':2,'message': 'successfully edited'}])


	def test_delete_redflag(self):
		response = self.client.delete('/redflags/2')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['data'],[{'id':2,'message':'redflag deleted succesfuly'}])

if __name__ == '__main__':
	unittest.main()
