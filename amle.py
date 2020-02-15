import urllib.request
import urllib.error
# If you are using Python 3+, import urllib instead of urllib2
import json 
sample = ["dog",-292.7117614746094,118.45552062988281,-60.6423454284668,-29.92791175842285,-27.643247604370117,-29.70526123046875,-21.8773136138916,-20.5919132232666,-6.0968523025512695,-11.078291893005371,-2.1155812740325928,7.589086532592773,0.705446720123291,4.404763221740723,-2.8959426879882812,-13.291520118713379,-7.228797912597656,-1.2514899969100952,-4.480558395385742,-4.507116317749023]
#sample = str(sample)
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
api_key = 'FyEZrfMADhspKONzdzHke3kaEmRyQygKucVpJ5DrL9+bRZ0lVjNI95Hnw2hnjQL5JckOfp+7Zd3/f/38k0pxlg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print("Result:\n\r")
    print(result) 
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 

