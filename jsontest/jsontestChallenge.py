#!/usr/bin/python3

import requests

# define the URL we want to use
IPURL = "http://ip.jsontest.com/"
POSTURL = "http://validate.jsontest.com/"
DATEURL = "http://date.jsontest.com/"

myservers = []

with open("/home/student/mycode/jsontest/myservers.txt", 'r') as file:
    hosts = file.read()
    myservers = hosts.split("\n")
    # Read the contents of the file



ip_data = requests.get(IPURL).json()
date_data = requests.get(DATEURL).json()

# mydata = {f"json": "time: "{date_data['date']}", ip: "{ip_data['ip']}", mysvrs: '{myservers}'"}
# print(mydata)