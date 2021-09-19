from bs4 import BeautifulSoup
import urllib3
import json
http=urllib3.PoolManager()
Abbr_dict={}
#Function to get the Slangs from https://www.noslang.com/dictionary/
def get_abbreviation(alpha):
    global Abbr_dict
    r=http.request('GET','https://www.noslang.com/dictionary/'+alpha)
    soup=BeautifulSoup(r.data,'html.parser')
    
    for i in soup.findAll('div',{'class':'dictionary-word'}): 

        abbr=i.find('abbr')['title']
        Abbr_dict[i.find('span').text[:-2]]=abbr
linkDict=[]
#Generating a-z
for one in range(97,123):
    linkDict.append(chr(one))
#Creating Links for https://www.noslang.com/dictionary/a...https://www.noslang.com/dictionary/b....etc
for i in linkDict:
    get_abbreviation(i)
# finally writing into a json file
with open('ShortendText.json','w') as file:
    jsonDict=json.dump(Abbr_dict,file)