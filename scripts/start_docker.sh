#!/bin/bash
INITDB_PATH=$( cd $(dirname $0)/../test/initdb ; pwd -P )
docker run -P -p 49160:22 -p 1521:1521 -v $INITDB_PATH:/docker-entrypoint-initdb.d wnameless/oracle-xe-11g
