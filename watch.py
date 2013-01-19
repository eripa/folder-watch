#!/usr/bin/env python
#

import os
import sys
import pickle
import smtplib
import datetime

#monitor_path = os.path.join(os.getenv('HOME'), 'Pictures', 'Aperture Library.aplibrary', 'Masters')

from_address = 'you@foo.bar'
from_address = 'you@foo.bar'
gmail_user = "you@foo.bar"
gmail_pwd = "fooBar1234"


def sendGmail(from_address, to_address, subject, message):
	FROM = from_address
	TO = [to_address] #must be a list
	SUBJECT = subject
	TEXT = message

	# Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		#server = smtplib.SMTP(SERVER) 
		server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		#server.quit()
		server.close()
		print 'successfully sent the mail'
	except smtplib.SMTPAuthenticationError:
		server.close()
		raise
	except:
		raise

def checkInput(dir):
	if not os.path.isdir(dir): raise IOError('Directory '+ dir +' does not seem to exist')

def getDataFromDisk(pickle_file):
	if os.path.isfile(pickle_file):
		with open(pickle_file, 'r') as pfile:
			return pickle.load(pfile)
	else:
		return {'run' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
				'data': []}

def writeDataToDisk(pickle_file, data):
	datadict = {'run' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
				'data': data}
	with open(pickle_file, 'w') as pickle_db:
		pickle.dump(datadict, pickle_db)

def scanPath(dir):
	ret = []
	for path, dirs, files in os.walk(dir):
		ret += files
	return sorted(ret)

def compareData(stored_data, data):
	return list(set(stored_data[1:]).symmetric_difference(data[1:]))
	return [(i,j) for i,j in zip(stored_data,data) if i!=j]

def generateMessage(data, runtime):
	msg = 'The following files have been removed since last run (%s):\n' % (runtime)
	for file in data:
		msg += file + '\n'
	return msg

def main():
	folder = sys.argv[1]
	try:
		checkInput(folder)
		datafile = os.path.join(os.path.dirname(sys.argv[0]), 'data.db')
		stored_data = getDataFromDisk(datafile)
		newdata = scanPath(folder)
		difference = compareData(stored_data['data'], newdata)
		print 'amount of files last run (%s): %s' % (stored_data['run'], len(stored_data['data']))
		print 'amount of files this run: %s' % (len(newdata))
		print 'difference: %s' % (len(difference))
		if len(stored_data['data']) > len(newdata):
			subject = 'Removed files from %s' % (folder)
			message = generateMessage(difference, stored_data['run'])
			print message
			sendGmail(from_address, from_address, subject, message)
		else:
			print 'Only new files or same amount, nothing to do.'
		writeDataToDisk(datafile, newdata)
	except IOError as e:
		err_str = "I/O error({0}): %s: {1}".format(e.errno, e.strerror) % (e.filename)
		sys.exit(err_str)
	except KeyboardInterrupt:
		print 'Aborting..'
	except smtplib.SMTPAuthenticationError as e:
		sys.exit(e.smtp_error)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
	sys.exit(0)




if __name__ == '__main__':
	main()