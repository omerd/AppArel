import sys
import os
import urllib2
import requests
import mp3play
import time

ALARM_PATH = r'alarm.mp3'

PRODUCT_OK = 0
THEFT = 1
#NON_EXIST_ID = 2
#BAD_SERVER_RESPONSE = 3

#TODO: the HTTP get could only be fired from an authenticated user which is a superuser, but not the system admin (Permissions...). or add the user to a group!
#TODO: HTTPS
def doesPaidProduct(productID):
	url = "http://localhost:8000/ctrl/" + str(int(productID,16)) + '/'
	
	response = requests.get( url)
	if(not response.ok):
		raise Exception("invalid HTTP response from server")
		
	if response.content == "OK":
		return PRODUCT_OK
		
	elif response.content == "BAD":
		return THEFT
		
	elif response.content == "ID does not exist":
		raise Exception("ID does not exist in the system")
		
	#elif response.content == "ID does not exist":
	#	return THEFT
	raise Exception("invalid server response")
	
#TODO this should start in new thread, so this function would be unblocking
def IdChecker(id):
	try:
		res = doesPaidProduct(id)
		if PRODUCT_OK == res:
			return
		elif THEFT == res:
			handleTheft(id)
	except Exception as e:
		handleError(id, e)

def handleTheft(id):
	log(id)
	alarm()
	
	
def alarm():
	#TODO: while multithreading, the access to the mp3 player should be synchronized
	clip =  mp3play.load(ALARM_PATH)
	clip.play()
	time.sleep(min(15, clip.seconds()))
	clip.stop()
	
def log(id):
	print "Theft detected !!!! ID: %s" % str(id)
	
def	handleError(id, e):
	#report to the system manger.
	print str(e) + ". ID: 0x%s, 0n%s" % (str(id), str(int(id,16)))
	
def waitForInput():
	while True:
		id = raw_input("Waiting for ID...  ")
		IdChecker(id)


waitForInput()