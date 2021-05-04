from . import *  
from app.cloud_system.models.helpers import *
from app.cloud_system.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "CS 5412 Cloud Computing Final Project"
net_id = "Gia Yao (yy667), Tianxing Jiang (tj258), Ziwei Gu (zg48)"

@cloud_system.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)



