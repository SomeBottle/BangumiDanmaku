import requests
import os

epid = input("Please type in the Episode ID of the bangumi!\n")
if epid.isdigit():
    url = "http://api.bilibili.com/pgc/view/web/season?ep_id="+epid
    epid = int(epid)
    resource = requests.get(url)
    resjson = resource.json()
    if int(resjson["code"]) == 0:
        eps = resjson["result"]["episodes"]
        theep = None
        for val in eps:
            if int(val["id"]) == epid:
                theep = val
                break
        if theep != None:
            cid = theep["cid"]
            danmaku_url = "http://comment.bilibili.com/"+str(cid)+".xml"
            danmaku_resource = requests.get(danmaku_url)
            danmaku_resource.encoding = "utf-8"
            danmaku_content = danmaku_resource.text
            relpath = "./ep"+str(epid)+".xml"
            thefile = open(relpath, "w", encoding="utf-8")
            thefile.write(danmaku_content)
            thefile.close()
            currentpath = os.path.abspath(os.path.dirname(__file__))
            print("Danmaku get successfully: ep"+str(epid))
            print("The file lies in:", currentpath)
        else:
            print("Failed to find CID")
    else:
        print("Request failed")
else:
    print("Please type in the correct ID")
input("Press Any key to continue...")
