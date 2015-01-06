

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
You will need a Wolframalpha API-Key!
Get it from here: https://developer.wolframalpha.com/portal/apisignup.html (Alternate Link http://products.wolframalpha.com/api)

You don't have to confirm their E-Mail!

When they redirected you to the "Developer Portal" klick on the button "Get an AppID"

Choose any Application Name...



Put it in your “queryprocess.py”, you will see where exactly!(Use nano speechscript/queryprocess.py to edit it)

#Move files:
sudo mv speechscript /opt/ ##Move folder "speechscript" to /opt/ 

sudo mv bin/* /usr/local/bin ##Move these files to /usr/local/bin

# Your installation is complete

#Usage
speech2wra	:And then ask Wolframalpha something!

text2speech "Text"	:Lets the Pi output your text!



#Thanks to
http://blog.oscarliang.net/raspberry-pi-voice-recognition-works-like-siri/ for the Idea and some part of these scripts!

#Last Words
I think i am not going to update this often, but I will answer your Questions and think about you suggestions! 
