#!/bin/bash
hostname=`ssh root@yourserv_tc 'hostname'`
backup=`ssh root@yourserv_tc 'find .BuildServer/backup -mtime -1 -iname tc*'`
if [ -n "$backup" ]; then
	echo "###############################################"
	echo
	echo -e "last bacup on: $hostname \nlocate:\n$backup"
	echo
	echo "################################################"
else
	echo "No one backup file(s)"
exit 1
fi
