#!/bin/bash

function GetPID #User #Name 
{
	PsUser=$1
	PsName=$2
	pid=`/bin/ps -u $PsUser -ef|/bin/grep $PsName|/bin/grep -v grep|/bin/grep -v vi|/bin/grep -v dbx\n |/bin/grep -v tail|/bin/grep -v start|/bin/gr
ep -v stop |/bin/sed -n 1p |/usr/bin/awk '{print $2}'` 
	echo $pid
}

#check litok
PID=`GetPID root 139.162.97.136`
echo $PID >> /home/vpn/tmp.log
/usr/bin/renice -19 -p $PID
if [ "-$PID" == "-" ]
	then
	{	
		echo "The process does not exist."
		/bin/bash /home/vpn/ocserv.to/start.sh
		/bin/bash /home/vpn/route.sh
		/bin/bash /home/vpn/iptables.sh
	}
fi

#check litsg
PID=`GetPID root 139.162.33.85`
echo $PID >> /home/vpn/tmp.log
/usr/bin/renice -19 -p $PID
if [ "-$PID" == "-" ]
        then
        {
                echo "The process does not exist."
                /bin/bash /home/vpn/ocserv.sg/start.sh
		/bin/bash /home/vpn/route.sh
		/bin/bash /home/vpn/iptables.sh
        }
fi


echo 'crontab '`date` >> /home/vpn/check.log
