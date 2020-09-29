#!/bin/bash

cd app
./setup.sh
./runAPI.sh &

cd ../web
./setup.sh
npm run build
npm run develop


# trap ctrl-c and call ctrl_c()
trap ctrl_c SIGINT

function ctrl_c() {
    echo -e "\n** Trapped CTRL-C **\n"
    FLASK_PID=$(ps aux | grep flask | awk '{print $2}')
    kill $FLASK_PID
    echo -e "\nCleaned up flask related processes (started in background)\nPIDs: "
    echo $FLASK_PID
    echo -e "\nGood Bye :)\n"
    exit
}

while true 
do
    sleep 1
done
