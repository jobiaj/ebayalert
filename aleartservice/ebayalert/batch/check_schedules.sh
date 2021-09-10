echo "Reached"

if ! type "sleep" > /dev/null; then
   echo "Sleep Command Not Found. Please update PATH variable in crontab -e"
   exit 0
fi

if [ $(ps aux | grep -v grep | grep from_cron | grep schedule_alert.py | wc -l) -lt 1 ]; then
    $2 $3/batch/schedule_alert.py $4
else
  echo "A process is already running. Exit"
  exit 0
fi