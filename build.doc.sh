#!/usr/bin/env bash
cd $(dirname $0)
DIR=`pwd`
rm -vrf ./dist
mkdir -p dist
cp -vrf ./landing-page/* ./dist
cd ./docs/blog/
pip install -r requirements.txt
make clean html
cd -
mkdir -p ./dist/docs
cp  -vrf ./docs/blog/_build/html ./dist/docs/blog
mkdir -p /data/sites/timger/
cp -vrf ./dist/* /data/sites/timger/
