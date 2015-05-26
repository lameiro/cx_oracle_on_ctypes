#!/bin/bash

INSTANTCLIENT_HOME=/home/lameiro/projects/instantclient/instantclient_12_1

python /home/lameiro/projects/ctypesgen/ctypesgen.py $INSTANTCLIENT_HOME/sdk/include/oci.h $INSTANTCLIENT_HOME/sdk/include/ociap.h $INSTANTCLIENT_HOME/sdk/include/ocidfn.h $INSTANTCLIENT_HOME/sdk/include/ori.h $INSTANTCLIENT_HOME/sdk/include/ort.h $INSTANTCLIENT_HOME/sdk/include/orl.h $INSTANTCLIENT_HOME/sdk/include/oro.h -I $INSTANTCLIENT_HOME/sdk/include -o oci_generated_12.py -l libclntsh.so.12.1
