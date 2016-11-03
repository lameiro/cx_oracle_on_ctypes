#!/bin/bash

INSTANTCLIENT_HOME=/Users/lameiro/projects/cx_oracle_on_ctypes/instantclient_12_1
CTYPESGEN_HOME=/Users/lameiro/projects/cx_oracle_on_ctypes/ctypesgen
SO_NAME=libclntsh.dylib.12.1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$INSTANTCLIENT_HOME
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$INSTANTCLIENT_HOME

python $CTYPESGEN_HOME/ctypesgen.py $INSTANTCLIENT_HOME/sdk/include/oci.h $INSTANTCLIENT_HOME/sdk/include/ociap.h $INSTANTCLIENT_HOME/sdk/include/ocidfn.h $INSTANTCLIENT_HOME/sdk/include/ori.h $INSTANTCLIENT_HOME/sdk/include/ort.h $INSTANTCLIENT_HOME/sdk/include/orl.h $INSTANTCLIENT_HOME/sdk/include/oro.h -I $INSTANTCLIENT_HOME/sdk/include -o oci_generated_12.py -l $SO_NAME
