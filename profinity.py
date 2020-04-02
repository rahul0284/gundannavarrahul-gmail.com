from profanity_check import predict, predict_prob
import urllib.request

text = open("abc.txt","r")    
contents = text.read()
text.close()

if(predict([contents])==1):
    print("profane alert,profane word are there in the file")
else:
    print("No Profane words found in the file")