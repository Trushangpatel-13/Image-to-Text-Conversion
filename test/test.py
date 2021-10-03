import requests
import time
import base64
from json import dumps

image_path = "./test/4..png"
with open(image_path, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

data = {"file":my_string}
res = requests.post('http://21dd-35-221-131-173.ngrok.io/ocr',data)
print(res.text)
