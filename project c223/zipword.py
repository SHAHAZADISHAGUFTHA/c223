import zipfile
import time

folderpath = input ("Path to the file: ")
zipf = zipfile.ZipFile(folderpath)
global result 
result = 0
global tried
result = 0
c = 0
if not zipf:
    print("the zipped file/folder is not password protected, you can easily open file/folder")
else :
    starttime = time.time()
    wordListFile = open.("wordlist.text", "r", errors = "ignore")
    body = wordListFile.read().lower()
    words = body.split("\n")
    for i in range(len(words)):
        word = words[i]
        password =word.encode("utf8").strip()
        c=c+1
        print("Trying to decode password by: {}".format(word))
        try:
            with zipfile.Zipfile(folderpsth,"r") as zf:
                zf.extractall(pwd = password)
                print("Success! the password is: "+word)
                endtime = time.time()
                result = 1
            break
        except: 
            pass

if (result == 0 ):
    print("Sorry, password not found. a total of" +str(c)+"possible combinations tried in"+str(duration)+"seconds. passwords is not of 4 charecters.")
else:
    duration = endtime - starttime
    print("Congo!!! password found after trying" +str(c)+"combinations in"+ str(duration)+"seconds")