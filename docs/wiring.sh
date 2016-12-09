#!/bin/bash

mkdir _build/tex

pdflatex -output-directory _build/tex wiring-gpio.tex && \
convert -flatten -density 300 _build/tex/wiring-gpio.pdf -quality 90 -resize 500x500 _static/wiring-gpio.png

pdflatex -output-directory _build/tex wiring-i2c.tex && \
convert -flatten -density 300 _build/tex/wiring-i2c.pdf -quality 90 -resize 500x500 _static/wiring-i2c.png
