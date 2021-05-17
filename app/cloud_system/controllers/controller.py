from . import *  
from app.cloud_system.models.helpers import *
from app.cloud_system.models.helpers import NumpyEncoder as NumpyEncoder
# import random
import json
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from azure.cosmos.partition_key import _Undefined, _Empty
import pymongo

endpoint = "https://cow-sensor-data.documents.azure.com:443/"
key = 'A5zE6A6HCFHh4qxdHAiJkSeqgdY44gdpaAMdkbdhG0lviJAYX0v26PcQVcddEmWkyY34OeNz56WSDzy9bBpKoA=='
client = CosmosClient(endpoint, key)

database_name = 'FinalProjectDB'
database = client.get_database_client(database_name)
container_name = 'SensorData'
container = database.get_container_client(container_name)
DB_URI = "mongodb://cow-sensor-data-mongo:oZv3OYwlOJEkj9c5VVmVGFzvEkCW6RYyCROEh3l1xdmxXzVMFSM3FBt9cqgz9boIV2OmajAnykPJprWXocfoFQ==@cow-sensor-data-mongo.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cow-sensor-data-mongo@"
db_client = pymongo.MongoClient(DB_URI)

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

@cloud_system.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
	#  SensorData.stand, SensorData.walk, SensorData.ruminate, SensorData.nothing, SensorData.inactive, SensorData.active, SensorData.highActive, 
	# query = "SELECT SensorData.deviceID, MAX(SensorData.datetime) FROM SensorData GROUP BY SensorData.deviceID"
	# query = "SELECT VALUE root FROM (SELECT SensorData.deviceID, SensorData.lie, MAX(SensorData.datetime) FROM SensorData GROUP BY SensorData.deviceID) as root"
	results = db_client.FinalProjectDB.SensorData.aggregate([
		{
			"$sort": {"datetime": 1},
		},
		{
			"$group": {
				'_id': { "deviceID" : "$/deviceID" },
				'lie': { "$first" : "$lie" },
				'stand': { "$first" : "$stand" },
				'walk': { "$first" : "$walk" },
				'datetime': { "$first" : "$DateTime" },
			}
		}
	])
	results = list(results)
	return {
		"results": results
	}
