import urllib.request
import urllib.error
# If you are using Python 3+, import urllib instead of urllib2
import json 

def make_request(sample):
    '''
    Sends a JSON request to a Azure Machine Learning Studio deployed web server for classification predictions.
    '''
    data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["class_label", "feature0", "feature1", "feature2", "feature3", "feature4", "feature5", "feature6", "feature7", "feature8", "feature9", "feature10", "feature11", "feature12", "feature13", "feature14", "feature15", "feature16", "feature17", "feature18", "feature19"],
                    "Values": [ [ "value", str(sample[1]), str(sample[2]), str(sample[3]), str(sample[4]), str(sample[5]), str(sample[6]), str(sample[7]), str(sample[8]), str(sample[9]), str(sample[10]), str(sample[11]), str(sample[12]), str(sample[13]), str(sample[14]), str(sample[15]), str(sample[16]), str(sample[17]), str(sample[18]), str(sample[19]), str(sample[20]) ], ]
                },        },
            "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/a4bc090290d447d689ae2c0fc656e79f/services/d531673c852b422f9ce1a2b091ddc4a4/execute?api-version=2.0&details=true'
    api_key = 'yeet' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        return result 
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))
        return json.loads(error.read())