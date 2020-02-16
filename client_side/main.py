import os, sys, io
import urllib3
import urllib
from urllib.parse import urlparse
import soundfile as sf
import utils
import azure_ml_prediction

sys.path.append("./atlastk")
sys.path.append("../atlastk")

import atlastk as Atlas

head = """
<title>"Cat and dog .wav classifier" example</title>
<link rel="shortcut icon" href="https://i.imgur.com/aecc2b2.png"/>
"""

body = """
<div style="display: table; margin: 100px auto auto auto;">
 <fieldset>
  <p>Type in a valid file URL site:</p>
  <input id="input" placeholder="Enter a valid url here" type="text" data-xdh-onevent="Submit"/>
  <p id="result">Result: </p>
  <div style="display: flex; justify-content: space-around; margin: 5px auto auto auto;">
   <button data-xdh-onevent="Submit">Submit</button>
   <button data-xdh-onevent="Clear">Clear</button>
  </div>
 </fieldset>
</div>
"""

http = urllib3.PoolManager()

def fetch_file(file_url):
    '''
    Give it a file url for a cat or dog .wav file and it will return a string 'cat' or 'dog' depending on the results of the ML prediction
    '''
    print(file_url)
    if(urlparse(file_url)[0]!=None):#urlparse to see if it really is a valid url
        if(str(file_url).find("http://") == -1):#check to see if it contains the http:// part of the link
            temp_url = "http://"+file_url
        else:
            temp_url = file_url
        try:
            data, samplerate = sf.read(io.BytesIO(urllib.request.urlopen(temp_url).read()))
            features = utils.extract_mfcc_features_ds(data, samplerate)
            sample = utils.prepare_sample(features)
            #print(sample)
            result = azure_ml_prediction.make_request(sample)
            if(result.rfind(b'dog') != -1):
                return "dog"
            elif(result.rfind(b'cat') != -1):
                return "cat"
            else:
                return "failed..."
        except:
            return "failed..."
        
def acConnect(dom):
    dom.setLayout("", body )
    dom.focus( "input")

def acSubmit(dom):
    dom.focus( "input")
    print(dom.getContent("input"))
    dom.setContent("result", "Result: ...apraising..." )
    dom.setContent("result", "Result: "+fetch_file(dom.getContent("input")))
    dom.setContent("input", "")

def acClear(dom):
    dom.setContent("input", "" )

callbacks = {
    "": acConnect,
    "Submit": acSubmit,
    "Clear": acClear,
}

Atlas.launch(callbacks, None, head)