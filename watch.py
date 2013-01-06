#!/usr/bin/env python
#

import os
import pickledb
import sys
import datetime

# some global settings
monitor_path = os.path.join(os.getenv('HOME'), 'Pictures', 'iPhoto Library', 'Masters')
history_to_keep = 10

def checkInput(dir):
	if not os.path.isdir(monitor_path): raise IOError('Directory '+ dir +' does not seem to exist')

def initializeDB(db, date):
	if not db.get(0):
		db.set(0, "Database created "+ date.strftime("%Y%m%d-%H%M"))
		return True
	else:
		return True

def getNextIndex(db):
	index = 0
	while db.get(index):
		index += 1
	return index

def main():
	try:
		checkInput(monitor_path)

		date = datetime.datetime.now()
		db = pickledb.load('files.db', True)

		print db.get(0)
		
		initializeDB(db, date)
		free_index = getNextIndex(db)
		print "Setting index %s" % (free_index)
		db.set(free_index, "bla bla")
		#db.lcreate()

		db.dump()
	except IOError as e:
		sys.exit(e.message)
	except KeyboardInterrupt:
		print 'Aborting..'
	sys.exit(0)




if __name__ == '__main__':
	main()