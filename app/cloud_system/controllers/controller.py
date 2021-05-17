from . import *  
from app.cloud_system.models.helpers import *
from app.cloud_system.models.helpers import NumpyEncoder as NumpyEncoder
# import random
import json

project_name = "CS 5412 Cloud Computing Final Project"
net_id = "Gia Yao (yy667), Tianxing Jiang (tj258), Ziwei Gu (zg48)"

@cloud_system.route('/', methods=['GET'])
def search():
	# query = request.args.get('search')
	# if not query:
	# 	data = []
	# 	output_message = ''
	# else:
	# 	output_message = "Your search: " + query
	# 	data = range(5)
	with open('example.json') as f:
		data = json.load(f)
	# data = [{'id': i, 'col_1': random.randint(1, 100), 'col_2': random.randint(1, 100), 'col_3': random.randint(1, 100), 'col_4': random.randint(1, 100)} for i in range(1, 20)]
	return render_template('search.html', data=data)


