import requests
import json
import os


folderName = input("folderName: ")


os.mkdir(folderName)

f = open('source.json', encoding="utf-8")
data = json.load(f)
f.close()

imageListURL = []

for i in range(len(data['log']['entries'])):
    thisURL = data['log']['entries'][i]['request']['url']
    if ".jpg" in thisURL:
        imageListURL.append(thisURL)

# print(len(imageListURL))


# download
print("Total images: "+str(len(imageListURL)))
print("==============================")
print("Start Downloading. . .")
print("==============================")
for i in range(len(imageListURL)):
    
    imageName = imageListURL[i].rsplit("/", 1)[-1]
    print("Downloading: "+imageName)

    with open('{}/{}'.format(folderName, imageName), 'wb') as handle:
        response = requests.get(imageListURL[i], stream=True)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

print("==============================")
print("-----------Complete-----------")
input("Press enter to exit.")