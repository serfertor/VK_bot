import vk_api
import requests
import re
import math


def red(a):
    from PIL import Image, ImageDraw
    import random
    mode = a 
    image = Image.open('temp.jpg') 
    draw = ImageDraw.Draw(image) 
    width = image.size[0] 
    height = image.size[1] 
    pix = image.load() 

    if mode == 0: 
        for i in range(width): 
            for j in range(height): 
                a = pix[i,j][0] 
                b = pix[i,j][1] 
                c = pix[i,j][2] 
                S = (a+b+c)//3 
                draw.point((i,j),(S,S,S)) 
    if mode == 1: 
        depth = 30 
        for i in range(width): 
            for j in range(height): 
                a = pix[i,j][0] 
                b = pix[i,j][1] 
                c = pix[i,j][2] 
                S = (a+b+c)//3 
                a = S+ depth 
                b = S+2*depth 
                c = S 
                draw.point((i,j),(a,b,c))

    if mode == 2: 
        for i in range(width): 
            for j in range(height): 
                a = pix[i,j][0] 
                b = pix[i,j][1] 
                c = pix[i,j][2]  
                draw.point((i,j),(255-a,255-b,255-c))

    if mode == 3:
        for i in range(width): 
            for j in range(height):
                rand=random.randrange (-100,100)

                a = pix[i,j][0] + rand
                b = pix[i,j][1] + rand
                c = pix[i,j][2] + rand
                if a > 255:
                    a=255
                if b > 255:
                    b=255
                if c > 255:
                    c=255
                if a < 0:
                    a=255
                if b < 0:
                    b=255
                if c < 0:
                    c=255
                draw.point((i,j),(255-a,255-b,255-c))

    if mode == 4:
        for i in range(width): 
            for j in range(height):
                rand=random.randrange (-100,100)

                a = pix[i,j][0] + rand
                b = pix[i,j][1] * rand
                c = pix[i,j][2] - rand
                if a > 255:
                    a=255
                if b > 255:
                    b=255
                if c > 255:
                    c=255
                if a < 0:
                    a=255
                if b < 0:
                    b=255
                if c < 0:
                    c=255
                draw.point((i,j),(255-a,255-b,255-c)) 



    image.save('ans.jpg', "JPEG")    
    del draw



token='82d76d37996024e88e4f44780390b1c7273374d5b1a3d14842368d6279dcbc379b4e98604e2341a33dd6a'

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
        inu=[]
        a = str(body)
        inu= a.split(' ')
        try:
            if body =='/биток':
                url = 'https://coinmarketcap.com/currencies/bitcoin/' 
                regexp = 'data-currency-value>(\d+\.*\d*)' 
                pattern = re.compile(regexp)
                res=requests.get (url)
                if res.ok:
                    body=res.text
                    res=pattern.findall(body)[0]
                    answer=res
                print (answer)
                vk.method('messages.send',{'peer_id':id,'random_id':0,'message':answer})
            if body =='/риплл':
                print ('1')
                regexp = 'data-currency-value>(\d+\.*\d*)' 
                url='https://coinmarketcap.com/currencies/ripple/'
                pattern = re.compile(regexp)
                res=requests.get (url)
                if res.ok:
                    print ('1')
                    body=res.text
                    res=pattern.findall(body)[0]
                    answer=res
                print (answer)
                vk.method('messages.send',{'peer_id':id,'random_id':0,'message':answer})

            if inu[0]=='/фото':
                try:
                    urlt = messages['items'][0]['last_message']['attachments'][0]['photo']['sizes'][2]['url']
                    p = requests.get(urlt)
                    f = open('temp.jpg','wb')
                    f.write(p.content)
                    f.close()
                    b=int(inu[1])
                    red(b)
                    uploader = vk_api.upload.VkUpload(vk)
                    img = uploader.photo_messages('ans.jpg')[0]
                    data = {
                        'peer_id':id,
                        'random_id':0,
                        'attachment':'photo'+str(img['owner_id'])+'_'+str(img['id'])
                     }
                    vk.method('messages.send', data)
                except:
                    vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'falses'})
            if inu [0] == '/реши':
                try:
                    a = int(inu[1])
                    b = int(inu[2])
                    c = int(inu[3])
                    d = (b**2) - (4*a*c)
                    if d > 0 :
                        x1 = (-b - math.sqrt(d)) / (2*a)
                        x2 = (-b + math.sqrt(d)) / (2*a)
                        vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'x1=' + str(x1) + '  x2=' + str(x2)})
                    elif d == 0:
                        x = (-b) / (2*a)
                        vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'x=' + str(x)})
                    elif d < 0:
                        vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'Корней нет' })
                except:
                    vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'Неверные данные' })

                
                    
        except:
             vk.method('messages.send',{'peer_id':id,'random_id':0,'message':'Список команд \n /биток - отправляет актуальный курс биткоина \n /риплл - отправляет актуальный курс риплл \n /фото (цифра 0-4 через пробел + фотография) - наложение фильтра на фотографию \n /реши (коофиценты a b c через пробел) - решение квадратных уравнений'})
