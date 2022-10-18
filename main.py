import httpx
import requests
import random
import json

def get_config():
    config_file = open("config.json", "r", encoding="utf8")
    configx = config_file.read()
    config_file.close()
    return configx


config_file = get_config()
config = json.loads(config_file)


# This will be added into config file later.
channel = "jhondybala"
tkn = "ydaesb2hz9pb19dxvgf3qbyotuc1nc"
useragent = random.choice(open("UserAgents.txt", "r").read().splitlines())
refererOrigin = random.choice(open("Referers.txt", "r").read().splitlines())


payloads = {
        # This list of payloads is not being used yet.
        # when use this, you have to solve channel_id callback.
     "payloadrealtimestreamtaglist": ('[{"operationName":"RealtimeStreamTagList","variables":{"channelLogin":"'+ channel +'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"a4747cac9d8e8bf6cf80969f6da6363ca1bdbd80fe136797e71504eb404313fd"}}},{"operationName":"UseLive","variables":{"channelLogin":"'+ channel +'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"639d5f11bfb8bf3053b424d9ef650d04c4ebb7d94711d644afb08fe9a0fad5d9"}}}]'),
     "payloadwithstreamlivequery": ('[{"operationName":"WithIsStreamLiveQuery","variables":{"id":"' + channel_id +'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"04e46329a6786ff3a81c01c50bfa5d725902507a0deb83b0edbf7abe7a3716ea"}}}]'),
     "payloadsetsessionstatus": ('[{"operationName":"ChannelPage_SetSessionStatus","variables":{"input":{"sessionID":"75d8da3ef7650385","availability":"ONLINE","activity":{"userID":"' + channel_id +'","type":"WATCHING"}}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"8521e08af74c8cb5128e4bb99fa53b591391cb19492e65fb0489aeee2f96947f"}}}]'),
     "ClientSideAdEventHandling_RecordAdEvent": '[{\"operationName\":\"ClientSideAdEventHandling_RecordAdEvent\",\"variables\":{\"input\":{\"eventName\":\"video_ad_impression\",\"eventPayload\":\"{\\"player_mute\\":false,\\"player_volume\\":0.5,\\"visible\\":true,\\"ad_id\\":\\"\\",\\"ad_position\\":1,\\"duration\\":30,\\"creative_id\\":\\"\\",\\"total_ads\\":1,\\"order_id\\":\\"\\",\\"line_item_id\\":\\"590384345057343213\\",\\"roll_type\\":\\"preroll\\",\\"stitched\\":true}\",\"radToken\":\"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJicm9hZGNhc3RlciI6IjgyNTExNDgxMSIsInZpZXdlciI6IiIsInNlc3Npb24iOiJhOTAwODI2YTY2ZmU0OTJiYTgwNTcwMzAwZjBlOTBlYSIsInZpZGVvX3Nlc3Npb25faWQiOiIxOTk0NDM0NTI4MDY4MzUwNDk3IiwicGxhdGZvcm1fdHlwZSI6IldFQiIsImR1cmF0aW9uIjozMCwiaXNfdmxtIjpmYWxzZSwiaXNfc3RpdGNoZWQiOnRydWUsImlhdCI6MTY2NjAyODk2MywiaXNzIjoiR3JhbmREQWRzIn0.YnS3Gp7Uwm8_-qm-loyFcKDHvUSWbEzHRXeJgh5Pb2OZuT2GbUtdl_Vibp9QHdAT_jjqeMR11JZi5k6NfEsyTg\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"7e6c69e6eb59f8ccb97ab73686f3d8b7d85a72a0298745ccd8bfc68e4054ca5b\"}}}]',
     "FollowButton_FollowUser": '[{\"operationName\":\"FollowButton_FollowUser\",\"variables\":{\"input\":{\"disableNotifications\":false,\"target_Id\":\"'+"'+channel+'"+'\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"51956f0c469f54e60211ea4e6a34b597d45c1c37b9664d4b62096a1ac03be9e6\"}}}]'
     }

def test_proxy():
    while True:
        try:
            session = requests.Session()
            proxy = random.choice(open("proxy.txt", "r").read().splitlines())
            proxies = {"https": f"http://{proxy}"}
            session.get("https://twitch.tv", proxies=proxies, timeout=5)
            return proxy
        except:
            None
        response = httpx.get(
            "https://id.twitch.tv/oauth2/validate", header=get_Headers()
        ).json()
        print("response:  ")
        print(response)
        token_username = response["login"]
        print("token_name:  " + str(token_username))
        proxy = test_proxy().split(":")
        print("proxy:  ")
        print(proxy)


def get_Headers():
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "Client-Version": "7b9843d8-1916-4c86-aeb3-7850e2896464",
        "User-Agent": useragent,
        "Authorization": f"OAuth {tkn}",
        "auth-token": "OAuth " + tkn,
        "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
        "Content-Type": "application/json, text/plain;charset=UTF-8, application/vnd.apple.mpegurl",
        "Client-Session-Id": "51789c1a5bf92c65",
        "X-Device-Id": "xH9DusxeZ5JEV7wvmL8ODHLkDcg08Hgr",
        "sec-ch-ua-platform": '"Windows"',
        "Accept": "*/*",
        "Origin": refererOrigin,
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": refererOrigin,
    }
    return headers


def get_Id(user, session):
    WatchTrackQuery = ('[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+ user +'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]')

    try:
        response = session.post("https://gql.twitch.tv/gql", data=WatchTrackQuery)
        id = response.json()[0]["data"]["user"]["id"]
        return id
    except:
        return None


def get_Playback(session):
    PlaybackAccessToken_Template = (
        '{"operationName":"PlaybackAccessToken_Template","query":"query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isLive) {    value    signature    __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isVod) {    value    signature    __typename  }}","variables":{"isLive":true,"login":"'+ channel +'","isVod":false,"vodID":"","playerType":"site"}}')

    try:
        response = session.post("https://gql.twitch.tv/gql", data=PlaybackAccessToken_Template).json()

        playbackList = {"Signature": response["data"]["streamPlaybackAccessToken"]["signature"],"Token": response["data"]["streamPlaybackAccessToken"]["value"]}
        return playbackList

    except:
        return None



def start(channel, runCount):
    for i in range(runCount):
        try:
            try:
                # Create the session
                sss = requests.Session()                
                sss.headers = get_Headers()
                sss.proxies = proxies

                # Definitions
                # proxies
                proxy = random.choice(open("proxy.txt", "r").read().splitlines())
                proxies = {"https": f"http://{proxy}"}
                # Callbacks                
                playback = get_Playback(sss)
                sig, token = playback["Signature"], playback["Token"]
                
                # Run
                sview = sss.get("https://usher.ttvnw.net/api/channel/hls/"+ channel + ".m3u8?&token=" + token + "&sig="+ sig, timeout=5)
                if sview.status_code == 200:
                    liveVideo = sview.text.split().pop()
                    sss.get(liveVideo)
                else:
                    print("Error, unable to get liveVideo.")

            except Exception as e:
                print("exception: " + str(e))

        except Exception as e:
            print("exception: " + str(e))

channel_id = get_Id(channel)

start(channel)
