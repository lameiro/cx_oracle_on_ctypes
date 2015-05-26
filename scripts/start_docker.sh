#!/bin/bash

docker run -P -p 1521:1521 -v /home/lameiro/projects/cx_oracle_on_ctypes/test:/oracle_scripts wnameless/oracle-xe-11g
