try:from requests import get,post;from time import sleep;import re
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
def Delete_Follower(JQ,sis): 
    sleep(5)
    rq=post(f"https://www.tiktok.com/api/commit/follow/user/?aid=1988&user_id={JQ}",headers={'Host': 'www.tiktok.com','Cookie':  f'sessionid={sis}; csrf_session_id=2ac85fd70e3ce31e66b24c20b7ac1c33','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '0','X-Secsdk-Csrf-Token': '00010000000116d755acebcd6d5281dc5cce93f28fbcacaab53421ab7960847e4a213d2b12611713e42388e6792b','Origin': 'https://www.tiktok.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'})
    if 'status_code' in rq.text:
        if rq.json()['status_code']==0:print(f'\n- Done unfollow For ID : {JQ}')
        else:print(rq.text)
    else:print(rq.text)
def Get_users(sis):
    rq=get('https://www.tiktok.com/api/user/list/?aid=1988&app_language=en&count=10000&maxCursor=0&minCursor=0',headers={'Host': 'www.tiktok.com','Cookie': f'sessionid={sis}','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'})
    try:
        total=rq.json()["total"]
        print(f'\n- Total Count of Following List : {total}\n');u=0
        while total!=u:
            for i in re.findall('"uniqueId":"(.*?)",',rq.text):
                u+=1
                print(u,' - user :',i)
                with open('Users_List.txt','a') as x:
                    x.write(i+'\n')     
            c=input("\n\n- continue for unfollow All users [Y-n] :\n\n---{ ")
            if c=='Y':pass
            else:exit()
            for JQ in re.findall('"id":"(.*?)",',rq.text):
                Delete_Follower(JQ,sis)   
            break
    except Exception as E:
        if 'statusMsg' in rq.text:print('- Error --{',rq.json()['statusMsg'],'}--') 
        else:print('- Error',E)
print("""

████████╗██╗██╗  ██╗     ██╗   ██╗███╗   ██╗███████╗
╚══██╔══╝██║██║ ██╔╝     ██║   ██║████╗  ██║██╔════╝
   ██║   ██║█████╔╝█████╗██║   ██║██╔██╗ ██║█████╗  
   ██║   ██║██╔═██╗╚════╝██║   ██║██║╚██╗██║██╔══╝  
   ██║   ██║██║  ██╗     ╚██████╔╝██║ ╚████║██║     
   ╚═╝   ╚═╝╚═╝  ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝

            By @TweakPY - @vv1ck
""")
sis=input('---{ Session ID : ')
Get_users(sis)
