 # old method used to get sig and token

                # payloadacesstokentemplate = '{\"operationName\":\"PlaybackAccessToken_Template\",\"query\":\"query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isLive) {    value    signature    __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: \\"web\\", playerBackend: \\"mediaplayer\\", playerType: $playerType}) @include(if: $isVod) {    value    signature    __typename  }}\",\"variables\":{\"isLive\":true,\"login\":\"gaules\",\"isVod\":false,\"vodID\":\"\",\"playerType\":\"site\"}}'
                #
                # atresponse = str(sss.post('https://gql.twitch.tv/gql', data=payloadacesstokentemplate).json())

                # sigstart = re.sub("signature\":\""," [",atresponse)
                # sigend = re.sub("\",\"__typename\":\"","]\" ",sigstart)
                # signature = re.findall("([0-9a-f]{40})",sigend,flags=re.IGNORECASE)
                # tokenstart = re.sub("{'data': {'streamPlaybackAccessToken': {'value': '","",atresponse)
                # tokenend = str(tokenstart).split("\', \'signature",1)
                # token = tokenend[0]
                # sig = str(*signature)

                # print(atresponse)

                # now we use
                # get_Playback(session
                # print(sig)
                # print(get_Playback("sig"))
                # print("primtei as 2 sig")
                # print(channel_id)
                # print(token)
                # print("agora é o usher")

                # print("ue")
                # old method used to get sig and token

