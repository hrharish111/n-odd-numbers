import requests
import MySQLdb
from datetime import datetime
from pymongo import MongoClient
import thread
import time


def urlinputs( threadName,delay):
	while True:
		time.sleep(delay)
		client = MongoClient()
		db = client.mcollection
		try:	
			r = requests.get('http://52.9.185.212:4567/results/tok/'+threadName)
			data = r.json()
			project = data['client']
			mtype = data['check']['name']
			matrix = data['check']['output']
			status = data['check']['status']
			mdate = datetime.isoformat(datetime.now())
			print "everting going good"

			
		except:
			print "came to exception"
			urlinputs( threadName,delay)
		try:	
			result = db.mcollection.insert(
						{
							"project":project,
							"mtype":mtype,
							"matrix":matrix,
							"status":status,
							"mdatetime":mdate

						}

				)
		except Exception as e:
			print "has my Exception",e
			pass
		client.close()
		# print result,threadName,mdate
			
try:
	thread.start_new_thread( urlinputs,("check_mem",60))
	thread.start_new_thread( urlinputs,("check_cpu",60))
except Exception as e:
	print "error unable to process thread", e

while 1:
	pass