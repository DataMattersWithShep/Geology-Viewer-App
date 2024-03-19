from flask import render_template
from app import app
#Imported to read inital json file
import json
#Imported for math.floor
import math


@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Shep'}
	attribute_list = []
	geology_dict = {}
	#Go through the list of all possible field types and add them to the list	
	with app.open_resource('new_surface_geology.json') as f:
		full_line = f.read()
		all_data = json.loads(full_line)
    #Go through the list of all possible field types and add them to the list
	for attribute in all_data["features"][0]["properties"]:
		attribute_list.append(attribute)
	#Setup all entires(currently 104715)
	for x in range(0, len(all_data["features"])):
		geology_dict[x] = {}
		for attribute in attribute_list:
			geology_dict[x][attribute] = str(all_data["features"][x]["properties"][attribute])
			coordinate_pair = all_data["features"][x]["geometry"]["coordinates"]
			geology_dict[x]["coordinates"] = []
			for pair in coordinate_pair[0]:
				new_pair = tuple(pair)
				geology_dict[x]["coordinates"].append(new_pair)
	return render_template('index.html', user=user, attribute_list= attribute_list)

@app.context_processor
def date_now():
	return 100;
			