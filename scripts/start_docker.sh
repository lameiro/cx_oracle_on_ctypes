#!/bin/bash
TESTPATH=$( cd $(dirname $0)/../test ; pwd -P )
docker run -P -p 49160:22 -p 1521:1521 -v $TESTPATH:/oracle_scripts wnameless/oracle-xe-11g
