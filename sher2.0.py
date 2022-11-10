import vk_api
import requests
import re
import time




token='3ab2112788fa3db64146e823fd21499b42c53781311575238fef2426ff5c06f48cced0bbc2550dcd0777a'

vk=vk_api.VkApi(token=token)
vk._auth_token()




value = {
    'offset':0,
    'count':20,
    'filter':'unanswered'
    }

while True:
    messages = vk.method('messages.getConversations',value)
    if messages['count']>=1:
        body = messages['items'][0]['last_message']['text']
        id = messages['items'][0]['last_message']['from_id']
        time.sleep(15)
        vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'1) 80% \n 2) 100% \n 3) 80% \n 4) 73% \n 5) 80% \n 6) 66% \n 7) 77% \n 8) 87% \n 9) 80% \n 10) 73% \n 11) 70% \n 12) 80% \n 13) 53% \n 14) 53% \n 15) 57% \n 16) 43% \n 17) 43% \n 18) 60% \n 19) 60% \n 20) 73% \n 21) 40% \n 22) 80% \n 23) 100% \n 24) 70% \n 25) 60% \n 26) 60% \n 27) 27% \n 28) 20% \n 29) 40% \n 30) 13% \n 31) 37% \n 32) 47% \n'})
        
