#!/usr/bin/env bash
export PATH=$PATH:/Library/TeX/texbin/
make clean
make latex
#make pdflatex
cd _build/latex
xelatex *.tex
xelatex *.tex
cd -
open _build/latex/*.pdf