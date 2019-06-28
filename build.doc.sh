#!/usr/bin/env bash
cd $(dirname $0)
DIR=`pwd`
pip install -r requirements.txt
rm -vrf ./dist
mkdir -p dist
cp -rf ./landing-page/* ./dist
cd ./docs/blog/
pip install -r requirements.txt
make clean html
rc=$?; if [[ ${rc} != 0 ]]; then exit 1 ${rc}; fi
cd -
mkdir -p ./dist/docs
cp  -rf ./docs/blog/_build/html ./dist/docs/blog
mkdir -p /data/sites/timger/
cp -rf ./dist/* /www/sites/timger
