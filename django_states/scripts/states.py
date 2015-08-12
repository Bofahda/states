#!/usr/bin/env python

import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_states.settings")

from main.models import State, StateCapital

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"states.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for dictionary in reader:

	print dictionary
	print dictionary['capital']


	state_obj, created = State.objects.get_or_create(name=dictionary['state'])
	
	state_obj.name = dictionary['state']
	state_obj.abbreviation = dictionary['abbrev']
	state_obj.save()

	print state_obj.name
	print created

	capital_obj, created = StateCapital.objects.get_or_create(name=dictionary['capital'])
	capital_obj.latitude = dictionary['latitude']
	capital_obj.longitude = dictionary['longitude']
	capital_obj.population = dictionary['population']
	capital_obj.state = state_obj

	capital_obj.save()




