# vosk-api-frontend
a website frontend for Vosk-api

Running on Ubuntu.

1) install vosk --> https://alphacephei.com/vosk/install
2) install apache2 and php
3) setup custom or default apache site location
4) get this git   (modified from : https://github.com/Sanmeet007/file-manager.git
5) place webroot into apache site dir, and place the coskroot dir outside of it.
6) in the voskrook get the vosk-api and model's
7) git clone vosk-api --> https://github.com/alphacep/vosk-api
8) wget model zipfiles from https://alphacephei.com/vosk/models
9) unzip and rename folder to 'model'. (where ever your running the main vosk script, this model folder needs to be in the same dir.)
10) check sudoers to allow apache user 'www-data' to run script.

check the links from index.php/load.php/load_folders.php for pointing to the voskroot files dir. (where you will upload audio and download transcripts)
check pointer links in transcribe.php to point to your voskroot dir, vosk script.
check the vosk-api python script to point to your voskroot for output of text file.
by accessing your apache server, http://(ip-address)/index.php you can view the file manager, upload files, and initiate the vosk transcriber to output to a text file.
