import csv  #to manipulate csv files
import json

sampleFile = open('data1.csv') #open method is part of the standard library in python

sampleReader = csv.reader(sampleFile);

#sampleData = list(sampleReader)
#print(sampleData) #each array in the list has two elements

for x in sampleReader:  #iterates through every object in SampleReader
	print("row number:" + str(sampleReader.line_num)+str(x)) #.line_num is a method from the csv module


jsonString = '{"name" : "Jon", "height" : "510"}' #json data is always in curly brackets;
#put quotes around it bc json object had to be a str

pythonData = json.loads(jsonString) #converting json data to python data

print(pythonData)


