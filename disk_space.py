#Python
import os
import shutil
import platform

def free_space():
	usage=shutil.disk_usage('c:/')
	return {
		"Total in GB": format(usage.total / 1024 / 1024 / 1024, '.2f'),
		"Used in GB": format(usage.used / 1024 / 1024 / 1024, '.2f'),
		"Free in GB": format(usage.free / 1024 / 1024 / 1024, '.2f'),
		
	}
	
for space in ('c'):
	print(space, ":" , free_space())