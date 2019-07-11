#!/usr/bin/env bash
git pull
git commit -a -m "auto push by:`hostname`  in:`date`"
git push origin master
