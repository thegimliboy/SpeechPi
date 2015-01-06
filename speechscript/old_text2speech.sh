#!/bin/bash
wget -q -O "/tmp/gt-dl.mp3" -U "Mozilla/5.0" "http://translate.google.com/translate_tts?tl=en&q=$1"
mplayer -quiet /tmp/gt-dl.mp3
rm /tmp/gt-dl.mp3

