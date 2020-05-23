#!/usr/bin/env bash
cd $(dirname $0)
DIR=`pwd`
rm -vrf ./dist
mkdir -p dist
cp -rf ./landing-page/* ./dist
cd ./pelican-blog
. ./venv/bin/activate
make html
cd -
pwd
mkdir -p ./dist/docs/blog
pwd
cp -vrf ./pelican-blog/output/* ./dist/docs/blog/
cp -vrf ./pelican-blog/output/docs/* ./dist/docs/
pwd
mkdir -p /usr/share/nginx/html/blog/
cp -vrf ./dist/*  /usr/share/nginx/html/blog/
#ln -s /usr/share/nginx/html/blog /usr/share/nginx/html/blog
#ln
chmod -R 777 /usr/share/nginx/html/blog/
echo 'finish ...'

#make clean html
#rc=$?; if [[ ${rc} != 0 ]]; then exit 1 ${rc}; fi
#cd -
#mkdir -p ./dist/docs
#cp  -rf ./docs/blog/_build/html ./dist/docs/blog
#cd ./dist
