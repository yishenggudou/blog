#!/usr/bin/env bash
cd $(dirname $0)
DIR=`pwd`
rm -vrf ./dist
mkdir -p dist
cp -rf ./landing-page/* ./dist
cd ./docs/blog/
make clean html
rc=$?; if [[ ${rc} != 0 ]]; then exit 1 ${rc}; fi
cd -
mkdir -p ./dist/docs
cp  -rf ./docs/blog/_build/html ./dist/docs/blog
cd ./dist
