

SpeechPi
========
#What's SpeechPi?
SpeechPi is an easy to use Speech Recognition Client using Google's SpeechAPI (You will not need a API-Key for this ;D )

Video: (Following soon)

#Setup
##Prerequisite:
###Install pip

wget https://bootstrap.pypa.io/get-pip.py

sudo python get-pip.py
(From  https://pip.pypa.io/en/latest/installing.html)

###Install these using pip:
### Wolframalpha
sudo pip install wolframalpha  

  (From https://pypi.python.org/pypi/wolframalpha)
### SpeechRecognition
sudo pip install SpeechRecognition

  (From https://pypi.python.org/pypi/SpeechRecognition/)

#Main Setup:

Get files:

1. git clone https://github.com/thegimliboy/SpeechPi.git


  cd SpeechPi

  chmod -R +x *

#Configure Wolframalpha
You will need a Wolframa. API-Key!
Get it here: http://products.wolframalpha.com/api

Put it in your “queryprocess.py”, you will see where exactly!

#Move files:
mv speechscrips /opt/ ##Move folder "speechscripts" to /opt/ 

mv bin/* /usr/local/bin ##Move these files to /usr/local/bin

#Usage
speech2wra	:And then ask Wolframalpha something!

text2speech "Text"	:Lets the Pi output your text!



#Thanks to
http://blog.oscarliang.net/raspberry-pi-voice-recognition-works-like-siri/ for the Idea and some part of these scripts!

#Last Words
I think i am not going to update this often, but I will answer your Questions and think about you suggestions! 
