import os, sys, io
import urllib3
import urllib
from urllib.parse import urlparse
import soundfile as sf
import utils
import azure_ml_example

sys.path.append("./atlastk")
sys.path.append("../atlastk")

import atlastk as Atlas

head = """
<title>"Hello, World !" example</title>
<link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAMFBMVEUEAvyEhsxERuS8urQsKuycnsRkYtzc2qwUFvRUVtysrrx0ctTs6qTMyrSUksQ0NuyciPBdAAABHklEQVR42mNgwAa8zlxjDd2A4POfOXPmzZkFCAH2M8fNzyALzDlzg2ENssCbMwkMOsgCa858YOjBKxBzRoHhD7LAHiBH5swCT9HQ6A9ggZ4zp7YCrV0DdM6pBpAAG5Blc2aBDZA68wCsZPuZU0BDH07xvHOmAGKKvgMP2NA/Zw7ADIYJXGDgLQeBBSCBFu0aoAPYQUadMQAJAE29zwAVWMCWpgB08ZnDQGsbGhpsgCqBQHNfzRkDEIPlzFmo0T5nzoMovjPHoAK8Zw5BnA5yDosDSAVYQOYMKIDZzkoDzagAsjhqzjRAfXTmzAQgi/vMQZA6pjtAvhEk0E+ATWRRm6YBZuScCUCNN5szH1D4TGdOoSrggtiNAH3vBBjwAQCglIrSZkf1MQAAAABJRU5ErkJggg==" />
"""

body = """
<div style="display: table; margin: 50px auto auto auto;">
 <fieldset>
  <p>Type in a valid file URL site:</p>
  <input id="input" placeholder="Enter a valid url here" type="text"
         data-xdh-onevent="Submit" value="World"/>
  <div style="display: flex; justify-content: space-around; margin: 5px auto auto auto;">
   <button data-xdh-onevent="Submit">Submit</button>
   <button data-xdh-onevent="Clear">Clear</button>
  </div>
 </fieldset>
</div>
"""

http = urllib3.PoolManager()

def fetch_file(file_url):
    print(file_url)
    if(urlparse(file_url)[0]!=None):
        #temp_file = io.BytesIO(urllib.request.urlopen(file_url).read())
        temp_url = "http://"+file_url
        data, samplerate = sf.read(io.BytesIO(urllib.request.urlopen(temp_url).read()))
        features = utils.extract_mfcc_features_ds(data, samplerate)
        sample = utils.prepare_sample(features)
        print(sample)
        azure_ml_example.make_request(sample)

def acConnect(dom):
    dom.setLayout("", body )
    dom.focus( "input")

def acSubmit(dom):
    dom.alert("Hello, " + dom.getContent("input") + "!")
    dom.focus( "input")
    print(dom.getContent("input"))
    fetch_file(dom.getContent("input"))


def acClear(dom):
    if ( dom.confirm("Are you sure?" ) ):
        dom.setContent("input", "" )
    dom.focus( "input")

callbacks = {
    "": acConnect,
    "Submit": acSubmit,
    "Clear": acClear,
}



Atlas.launch(callbacks, None, head)