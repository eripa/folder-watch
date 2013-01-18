#!/usr/bin/env python
#

import os
import datastore
from datastore.impl.filesystem import FileSystemDatastore
import sys
import datetime


#import pickle

# pickle.dump(itemlist, outfile)
# To read it back:

# itemlist = pickle.load(infile)

# some global settings
monitor_path = os.path.join(os.getenv('HOME'), 'Pictures', 'iPhoto Library', 'Masters')
history_to_keep = 10

def checkInput(dir):
	if not os.path.isdir(monitor_path): raise IOError('Directory '+ dir +' does not seem to exist')

def initializeDS(ds, date):
	initkey = datastore.Key(0)
	if not ds.contains(initkey):
		ds.put(initkey, "Database created "+ date.strftime("%Y%m%d-%H%M"))
		print ds.get(initkey)
		return True
	else:
		return True

def getNextIndex(ds):
	i = 0
	next_key = datastore.Key(i)
	while ds.contains(next_key):
		i += 1
		next_key = datastore.Key(i)
	last_key = datastore.Key(i - 1)
	return last_key, next_key

def main():
	try:
		checkInput(monitor_path)

		date = datetime.datetime.now()
		ds = FileSystemDatastore('datastore')
		
		initializeDS(ds, date)
		last_key, next_key = getNextIndex(ds)
		print "Last written: %s" % (last_key)
		print "Setting index %s" % (next_key)
		ds.put(next_key, ['bla', 'bla2', 'bla3'])

	except IOError as e:
		sys.exit(e.message)
	except KeyboardInterrupt:
		print 'Aborting..'
	sys.exit(0)




if __name__ == '__main__':
	main()