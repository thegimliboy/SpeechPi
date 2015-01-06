

SpeechPi
========
#Whats is SpeechPi?
SpeechPi is an easy to use Speech Recognition Client using Google's SpeechAPI (You will not need a API-Key for this ;D )

Video: (Following soon)

#You need:
Install pip (https://pip.pypa.io/en/latest/installing.html)

wget https://bootstrap.pypa.io/get-pip.py

sudo python get-pip.py

Install these using pip:

https://pypi.python.org/pypi/wolframalpha

https://pypi.python.org/pypi/SpeechRecognition/

#Setup:

Get files:
wget https://github.com/thegimliboy/SpeechPi/archive/master.zip
unzip master.zip SpeechPi
cd SpeechPi
chmod -R 777 *

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
