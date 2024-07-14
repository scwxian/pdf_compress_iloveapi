import requests
import json

publickey = "insert_public_key_from_iloveapi"

def getAuthToken():
  Payload = json.dumps({
    "public_key": publickey
  })
  Headers = {
    'Content-Type': 'application/json',
  }
  response = requests.post("https://api.ilovepdf.com/v1/auth", headers=Headers, data=Payload)
  r = response.json()
  token = r["token"]
  return(token)

def startCompressTask(headers):
  payload = {}
  headers = headers
  response = requests.get("https://api.ilovepdf.com/v1/start/compress", headers=headers, data=payload)
  r = response.json()
  serverURL, taskID = r["server"], r["task"]
  return(serverURL, taskID)

def uploadPDF(newURL, taskID, headers):
  url = newURL + 'upload'
  payload = {'task': taskID}
  files={'file': open('sample.pdf', 'rb')}
  headers = headers

  response = requests.post(url, headers=headers, data=payload, files=files)
  Response = response.json()
  serverFilename = Response["server_filename"]
  return(serverFilename)

def processPDF(newURL, taskID, headers, serverFilename):
  url = newURL + 'process'
  payload = {
    "task": taskID,
    "tool": "compress",
    "files": [
      {
        "server_filename": serverFilename,
        "filename": "sample.pdf"
      }
    ],
    "output_filename": "{date}_{filename}"
  }
 
  headers = headers
  response = requests.post(url, headers=headers, json=payload)
  r = response.json()
  downloadedFileName = r["download_filename"]
  return(downloadedFileName)

# Step 1 - Get Auth Token & Set Headers
token = getAuthToken()
headers = {'Authorization': 'Bearer ' + token}

# Step 2 - Start Task & Set Server URL
serverURL, taskID = startCompressTask(headers)
newURL = "https://"+serverURL+"/v1/"
print(newURL)

# Step 3 - Upload File to Task ID
serverFilename = uploadPDF(newURL, taskID, headers)
print(serverFilename)

# Step 4 - Process File
newFileName = processPDF(newURL, taskID, headers, serverFilename)
print(newFileName)

# Step 5 - Download File
payload = {}
r = requests.get(newURL+'download/'+taskID, headers=headers, data=payload)
open(newFileName, 'wb').write(r.content)
