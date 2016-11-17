#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$DIR/s3simple.sh get s3://cxoracleonctypes/dependencies_linux.tar.gz dependencies_linux.tar.gz
tar xvzf dependencies_linux.tar.gz

curl -o pypy2.tar.bz2 -L https://bitbucket.org/pypy/pypy/downloads/pypy2-v5.6.0-linux64.tar.bz2
tar xvjf pypy2.tar.bz2
mv $(ls | grep pypy2 | grep -v tar) pypy2

curl -o pypy3.tar.bz2 -L https://bitbucket.org/pypy/pypy/downloads/pypy3.3-v5.5.0-alpha-linux64.tar.bz2
tar xvjf pypy3.tar.bz2
mv $(ls | grep pypy3 | grep -v tar) pypy3
