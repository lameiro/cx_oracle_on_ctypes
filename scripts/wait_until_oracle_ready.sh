#!/bin/bash

until [[ $DOCKER_STARTUP_FINISHED == "Disconnected from Oracle Database" ]]; do 
	sleep 5
	echo "Waiting for Oracle XE container to startup..."
	
        DOCKER_STARTUP_FINISHED=$(docker logs oracle_xe | grep "Disconnected from Oracle Database" | cut -d" " -f1-4)
done
