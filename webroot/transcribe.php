<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $filename = $_POST['filename'];
    #$filename = implode("",$filename);
    $newname = '../../..//trans/files/audio/'.$filename;
   # function transcribe()
    #{
	    exec('sudo -u netadmin ./../../..//trans/vosk-api/python/example/webrun.py '.$newname);
	    echo "success";
    #}
  }
?>
