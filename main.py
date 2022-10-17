import http
import httpx;
import requests;
import random;
import json; 
import re;
import string;
import socket;

def get_config():
    config_file = open("config.json","r", encoding="utf8")
    configx = config_file.read()
    config_file.close()
    return configx


config_file = get_config()
config = json.loads(config_file)
channel = "channel name"

def start_spam(ttoken, channel = "channel name"):
                    for i in range(1):
                        try:
                            try:
                                sss = requests.Session()                                
                                proxy = random.choice(open("proxy.txt","r").read().splitlines())
                                proxies = {"https": f"http://{proxy}"}
                                sss.proxies = proxies
                                payloadacesstokentemplate = '{\"operationName\":\"PlaybackAccessToken_Template\",\"query\":\"query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isLive) {    value    signature    __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isVod) {    value    signature    __typename  }}\",\"variables\":{\"isLive\":true,\"login\":\"channel\",\"isVod\":false,\"vodID\":\"\",\"playerType\":\"site\"}}'
                                payloadrealtimestreamtaglist = '[{\"operationName\":\"RealtimeStreamTagList\",\"variables\":{\"channelLogin\":\"channel name\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"a4747cac9d8e8bf6cf80969f6da6363ca1bdbd80fe136797e71504eb404313fd\"}}},{\"operationName\":\"UseLive\",\"variables\":{\"channelLogin\":\"channel name\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"639d5f11bfb8bf3053b424d9ef650d04c4ebb7d94711d644afb08fe9a0fad5d9\"}}}]'
                                payloadtest = '[{\"operationName\":\"RealtimeStreamTagList\",\"variables\":{\"channelLogin\":\"channel name\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"a4747cac9d8e8bf6cf80969f6da6363ca1bdbd80fe136797e71504eb404313fd\"}}},{\"operationName\":\"UseLive\",\"variables\":{\"channelLogin\":\"channel name\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"639d5f11bfb8bf3053b424d9ef650d04c4ebb7d94711d644afb08fe9a0fad5d9\"}}},{\"operationName\":\"WithIsStreamLiveQuery\",\"variables\":{\"id\":\"666114811\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"04e46329a6786ff3a81c01c50bfa5d725902507a0deb83b0edbf7abe7a3716ea\"}}},{\"operationName\":\"ChannelPage_SetSessionStatus\",\"variables\":{\"input\":{\"sessionID\":\"75d8da3ef7650385\",\"availability\":\"ONLINE\",\"activity\":{\"userID\":\"666114811\",\"type\":\"WATCHING\"}}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"8521e08af74c8cb5128e4bb99fa53b591391cb19492e65fb0489aeee2f96947f\"}}}]'
                               
                                payloadwithstreamlivequery = '[{\"operationName\":\"WithIsStreamLiveQuery\",\"variables\":{\"id\":\"666114811\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"04e46329a6786ff3a81c01c50bfa5d725902507a0deb83b0edbf7abe7a3716ea\"}}}]'
                                payloadsetsessionstatus = '[{\"operationName\":\"ChannelPage_SetSessionStatus\",\"variables\":{\"input\":{\"sessionID\":\"75d8da3ef7650385\",\"availability\":\"ONLINE\",\"activity\":{\"userID\":\"666114811\",\"type\":\"WATCHING\"}}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"8521e08af74c8cb5128e4bb99fa53b591391cb19492e65fb0489aeee2f96947f\"}}}]'
                                payload = '[{\"operationName\":\"ClientSideAdEventHandling_RecordAdEvent\",\"variables\":{\"input\":{\"eventName\":\"video_ad_quartile_complete\",\"eventPayload\":\"{\\"player_mute\\":false,\\"player_volume\\":0.5,\\"visible\\":true,\\"ad_id\\":\\"\\",\\"ad_position\\":1,\\"duration\\":30,\\"creative_id\\":\\"\\",\\"total_ads\\":1,\\"order_id\\":\\"\\",\\"line_item_id\\":\\"590384345057343213\\",\\"roll_type\\":\\"preroll\\",\\"quartile\\":1,\\"stitched\\":true}\",\"radToken\":\"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJicm9hZGNhc3RlciI6IjgyNTExNDgxMSIsInZpZXdlciI6IiIsInNlc3Npb24iOiJhOTAwODI2YTY2ZmU0OTJiYTgwNTcwMzAwZjBlOTBlYSIsInZpZGVvX3Nlc3Npb25faWQiOiIxOTk0NDM0NTI4MDY4MzUwNDk3IiwicGxhdGZvcm1fdHlwZSI6IldFQiIsImR1cmF0aW9uIjozMCwiaXNfdmxtIjpmYWxzZSwiaXNfc3RpdGNoZWQiOnRydWUsImlhdCI6MTY2NjAyODk2MywiaXNzIjoiR3JhbmREQWRzIn0.YnS3Gp7Uwm8_-qm-loyFcKDHvUSWbEzHRXeJgh5Pb2OZuT2GbUtdl_Vibp9QHdAT_jjqeMR11JZi5k6NfEsyTg\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"7e6c69e6eb59f8ccb97ab73686f3d8b7d85a72a0298745ccd8bfc68e4054ca5b\"}}}]'
                                #payload = '[{\"operationName\":\"ClientSideAdEventHandling_RecordAdEvent\",\"variables\":{\"input\":{\"eventName\":\"video_ad_impression\",\"eventPayload\":\"{\\"player_mute\\":false,\\"player_volume\\":0.5,\\"visible\\":true,\\"ad_id\\":\\"\\",\\"ad_position\\":1,\\"duration\\":30,\\"creative_id\\":\\"\\",\\"total_ads\\":1,\\"order_id\\":\\"\\",\\"line_item_id\\":\\"590384345057343213\\",\\"roll_type\\":\\"preroll\\",\\"stitched\\":true}\",\"radToken\":\"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJicm9hZGNhc3RlciI6IjgyNTExNDgxMSIsInZpZXdlciI6IiIsInNlc3Npb24iOiJhOTAwODI2YTY2ZmU0OTJiYTgwNTcwMzAwZjBlOTBlYSIsInZpZGVvX3Nlc3Npb25faWQiOiIxOTk0NDM0NTI4MDY4MzUwNDk3IiwicGxhdGZvcm1fdHlwZSI6IldFQiIsImR1cmF0aW9uIjozMCwiaXNfdmxtIjpmYWxzZSwiaXNfc3RpdGNoZWQiOnRydWUsImlhdCI6MTY2NjAyODk2MywiaXNzIjoiR3JhbmREQWRzIn0.YnS3Gp7Uwm8_-qm-loyFcKDHvUSWbEzHRXeJgh5Pb2OZuT2GbUtdl_Vibp9QHdAT_jjqeMR11JZi5k6NfEsyTg\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"7e6c69e6eb59f8ccb97ab73686f3d8b7d85a72a0298745ccd8bfc68e4054ca5b\"}}}]'
                               # payload = '[{\"operationName\":\"FollowButton_FollowUser\",\"variables\":{\"input\":{\"disableNotifications\":false,\"targetID\":\"'+"channel name"+'\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"51956f0c469f54e60211ea4e6a34b597d45c1c37b9664d4b62096a1ac03be9e6\"}}}]'
                                headers = {"Authorization": f"OAuth {ttoken}","Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',"Content-Type": "application/json"}
                                print("1ee :  ")

                                atresponse = str(sss.post('https://gql.twitch.tv/gql', data=payloadacesstokentemplate, headers=headers, timeout=5).json())
                                sss.post('https://gql.twitch.tv/gql', data=payloadrealtimestreamtaglist, headers=headers, timeout=5).json()                                
                                sss.post('https://gql.twitch.tv/gql', data=payloadtest, headers=headers, timeout=5).json()                        
                                sss.post('https://gql.twitch.tv/gql', data=payloadwithstreamlivequery, headers=headers, timeout=5).json()    
                                sss.post('https://gql.twitch.tv/gql', data=payloadsetsessionstatus, headers=headers, timeout=5).json()
                                sigstart = re.sub("signature\":\""," [",atresponse)
                                sigend = re.sub("\",\"__typename\":\"","]\" ",sigstart)
                                signature = re.findall("([0-9a-f]{40})",sigend,flags=re.IGNORECASE)
                                
                                tokenstart = re.sub("{'data': {'streamPlaybackAccessToken': {'value': '","",atresponse)
                                tokenend = str(tokenstart).split("\', \'signature",1)
                                token = tokenend[0]

                                sig = str(*signature)
                                print(sig)
                                print(atresponse)
                                print("agora é o usher")
                                print(token)                            
                                
                                print(sss.get("https://usher.ttvnw.net/api/channel/hls/"+channel+".m3u8?sig="+sig+"&token="+token+"", headers=headers, timeout=5))
                                headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",'Authorization':f'OAuth {ttoken}'}
                                response = httpx.get("https://id.twitch.tv/oauth2/validate",headers=headers).json()
                                token_name = response['login']
                                proxy = test_proxy().split(":")
                                print(proxy)              
                            except Exception as e:
                             print("exception: "+ str(e)) 
                            def test_proxy():
                                while True:
                                    try: 
                                        session = requests.Session()
                                        proxy = random.choice(open("proxy.txt","r").read().splitlines())
                                        proxies = {"https": f"http://{proxy}"}
                                        session.get("https://twitch.tv",proxies=proxies, timeout=5)
                                        return proxy
                                    except:
                                        None
                            headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",'Authorization':f'OAuth {ttoken}'}
                            response = httpx.get("https://id.twitch.tv/oauth2/validate",headers=headers).json()
                            print("response:  ")
                            print(response)
                            #token_name = response['login']
                            proxy = test_proxy().split(":")
                            print("proxy:  ")
                            print(proxy)

                        except Exception as e:
                            print(e) 

start_spam("r8rr5l9v9uwodkd9furjop33334ozb")


def get_id(user):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'Accept-Language': 'en-US',
        'sec-ch-ua-mobile': '?0',
        'Client-Version': '7b9843d8-1916-4c86-aeb3-7850e2896464',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Client-Session-Id': '51789c1a5bf92c65',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'X-Device-Id': 'xH9DusxeZ5JEV7wvmL8ODHLkDcg08Hgr',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://www.twitch.tv',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.twitch.tv/',
    }
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+user+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'
    try:
        session = requests.Session()
        response = session.post('https://gql.twitch.tv/gql', headers=headers, data=data)
        print(response.text)
        id = response.json()[0]['data']['user']['id']
        return id
    except:
        return None
    
