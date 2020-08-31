import requests
res=requests.get('https://www.py4e.com/code3/mbox.txt')
with open('mbox.txt','w',encoding=res.encoding) as wf:
    wf.write(res.text)
    
