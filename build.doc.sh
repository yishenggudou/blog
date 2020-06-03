#!/usr/bin/env bash
cd $(dirname $0)
DIR=$(pwd)
rm -rf ./dist
mkdir -p dist
cp -rf ./landing-page/* ./dist
if [ -e ./venv/bin/activate ]
then
  . ./venv/bin/activate
fi
cd ./pelican-blog
if [ -e ./venv/bin/activate ]
then
  . ./venv/bin/activate
fi
pip install -r requirements.txt
make html
cd -
pwd
rm -rf ./dist/docs/blog
mkdir -p ./dist/docs/blog
pwd
cp -rf ./pelican-blog/output/* ./dist/docs/blog/
if [ -d ./pelican-blog/output/docs ]; then
  cp -rf ./pelican-blog/output/docs/* ./dist/docs/
fi
pwd
if [ -d /usr/share/nginx/html ]; then
  mkdir -p /usr/share/nginx/html/blog/
  cp -rf ./dist/* /usr/share/nginx/html/blog/
  #ln -s /usr/share/nginx/html/blog /usr/share/nginx/html/blog
  #ln
  chmod -R 777 /usr/share/nginx/html/blog/
  echo 'finish ...'
fi
#make clean html
#rc=$?; if [[ ${rc} != 0 ]]; then exit 1 ${rc}; fi
#cd -
#mkdir -p ./dist/docs
#cp  -rf ./docs/blog/_build/html ./dist/docs/blog
#cd ./dist
