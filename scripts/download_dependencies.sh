#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$DIR/s3simple.sh get s3://cxoracleonctypes/dependencies_linux.tar.gz dependencies_linux.tar.gz
tar xvzf dependencies_linux.tar.gz
