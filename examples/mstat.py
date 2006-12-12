#!/usr/bin/python

### Example2: simple sub-second monitor (ministat)

### This is a quick example showing how to implement your own *stat utility
### If you're interested in such functionality, contact me at dag@wieers.com
import sys
sys.path.insert(0, '/usr/share/dstat/')
import dstat, time

### Allow arguments
try: delay = float(sys.argv[1])
except: delay = 0.2
try: count = int(sys.argv[2])
except: count = 10

### Load stats
stats = []
for o in (dstat.dstat_epoch(), dstat.dstat_cpu(), dstat.dstat_mem(), dstat.dstat_load(), dstat.dstat_disk(), dstat.dstat_sys()):
	try: o.check()
	except Exception, e: print e
	else: stats.append(o)

### Make time stats sub-second
stats[0].format = ('t', 14, 0)

### Print headers
title1 = title2 = ''
for o in stats:
	title1 = title1 + '  ' + o.title1()
	title2 = title2 + '  ' + o.title2()
print '\n' + title1 + '\n' + title2

### Print stats
for dstat.update in range(count):
	line = ''
	for o in stats:
		o.extract()
		line = line + '  ' + o.show()
	print line + dstat.ansi['reset']
	if dstat.update != count-1: time.sleep(delay)
	dstat.tick = 1
print dstat.ansi['reset']
