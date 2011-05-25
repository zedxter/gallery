#!/bin/bash

case "$1" in
"start") 
python manage.py runfcgi method=threaded host=127.0.0.1 port=8801 pidfile=/tmp/gallery-server.pid 
;;
"stop") 
kill -9 `cat /tmp/gallery-server.pid` 
;;
"restart")
$0 stop
sleep 1
$0 start
;;
*) echo "Usage: ./server.sh {start|stop|restart}";;
esac
