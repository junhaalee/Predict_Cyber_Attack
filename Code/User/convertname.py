import json
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data


# Consumer API keys:
CONSUMER_KEY = "" #API key
CONSUMER_SECRET = "" 
ACCESS_TOKEN = "" 
ACCESS_TOKEN_SECRET = "" 


# Authentication and access using keys:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)


accountlist = pd.read_excel('2.xlsx')

values = accountlist['Twitter accounts'].values
column = ['Twitter accounts']
df_selection = accountlist[column]
usernames=values
temp = []


for username in usernames:
    
    #with open('hackers/'+username+'.json','r') as toread:
    #with open('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Follow/list/'+username+'.json','r') as json_file:
    with open('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Follow/hacker/'+username+'.json','r') as json_file:

        data=json.load(json_file);
        
    name = {
                "username" : username,
                "following" : [],
                "follower" : []
            }


    for i in range(0, len(data[0]["follower"])):
        try :
            name["follower"].append( api.get_user(data[0]["follower"][i]).screen_name)
        except tweepy.error.TweepError :    
            print(data[0]["follower"][i])
    
    
    for i in range(0, len(data[0]["following"])):
        try :
            name["following"].append(api.get_user(data[0]["following"][i]).screen_name)
        except tweepy.error.TweepError :    
            print(data[0]["following"][i])
    
    temp.append(name)
    print(username)
        
    #with open('list_name/'+username+'.json','w') as towrite:
    with open('hacker_name/'+username+'.json','w') as towrite:
        json.dump(temp,towrite,ensure_ascii=False)
        
    temp =[]
