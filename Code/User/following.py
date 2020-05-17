import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing
import json
import time
import pandas as pd 


# Twitter App access keys for @user
CONSUMER_KEY = "" 
CONSUMER_SECRET = "" 
ACCESS_TOKEN = "" 
ACCESS_TOKEN_SECRET = "" 



# Authentication and access using keys:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)

#accountlist = pd.read_excel('../list/test.xlsx')
accountlist = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberattacks/Follow/list/1000_100.xlsx')



values = accountlist['Twitter accounts'].values
column = ['Twitter accounts']
df_selection = accountlist[column]
usernames=values
temp = []


text ='port="dddddd" aaa="22222" local="gangnam"'

data = {
        "port" : ''
        }

for username in usernames:
    
    
    data = {
            "username" : '',
            "following" : []}
    
   
    
    try :
        user_id = api.get_user(username).id
        data["username"] = user_id
        followings_id = api.friends_ids(screen_name = username)
        data["following"] = followings_id
        
    except :
        data["username"] = ''
        data["following"] = []
            
    temp.append(data)
    print(username)
    
    
#    with open('../1000ing/'+username+'.json','w') as towrite:
with open('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberattacks/Follow/1000ing/list_100.json','w') as towrite:
    json.dump(temp,towrite,ensure_ascii=False)
    
    
    