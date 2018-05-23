import requests
from PIL import Image
import sys
import time


def Get_Map_Image(Location):
    centre = Location
    f=open('static.png','wb')
    #takes a 1000* 1209 meter square from google maps centred on Centre with everthing blackended and the roads highlighted white
    Toggle_Everything = "style=visibility:off"
    Turn_Roads_Red = 'style=feature:road.local|element:geometry|color:0xff0000|visibility:on'
    Turn_State_Roads_Green = 'style=feature:road.highway|element:geometry|color:0x00ff00|visibility:on'
    Turn_Main_Roads_Blue = 'style=feature:road.arterial|element:geometry|color:0x0000ff|visibility:on'
    f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center=' + centre + '&zoom=16&size=530x640&scale=1&' + Toggle_Everything +'&' + Turn_Roads_Red + '&'+Turn_State_Roads_Green+ '&' + Turn_Main_Roads_Blue+ '&sensor=false').content)
    f.close()





def Test_Count_Pixels(image):
    im = Image.open('static.png')
    rgb_im = im.convert('RGBA')
    R_count = 0
    G_count = 0
    B_count = 0
    Map_Size = 530*530
    #Itterates across the image counting white and dark pixels
    for y in range(55,585):
        for x in range(1,530):
            r,g,b,a = rgb_im.getpixel((x,y))
            if r == 255:
                R_count +=1
            elif g == 255:
                G_count +=1
            elif b == 255:
                B_count +=1
    print("% Highway: " + str((G_count/Map_Size)*100))
    print("\tSquare Meters: " + str(round(1000000*(G_count/Map_Size))))
    print("% Main Roads: " + str((B_count/Map_Size)*100))
    print("\tSquare Meters: " + str(round(1000000*(B_count/Map_Size))))
    print("% Local Streets: " + str((R_count/Map_Size)*100))
    print("\tSquare Meters: " + str(round(1000000*(R_count/Map_Size))))
    sys.stdout.flush()

def Count_Pixels(image):
    im = Image.open('static.png')
    rgb_im = im.convert('RGBA')
    R_count = 0
    G_count = 0
    B_count = 0
    Map_Size = 530*530
    #Itterates across the image counting white and dark pixels
    for y in range(55,585):
        for x in range(1,530):
            r,g,b,a = rgb_im.getpixel((x,y))
            if r == 255:
                R_count +=1
            elif g == 255:
                G_count +=1
            elif b == 255:
                B_count +=1

    print(str(round(1000000*(G_count/Map_Size))))

    print(str(round(1000000*(B_count/Map_Size))))

    print(str(round(1000000*(R_count/Map_Size))))


def Caculate_Area():
    x = time.time()
    lat = -37.8066061867195
    lng = 144.954833984375
    centre = (str(lat)+","+str(lng))

    Get_Map_Image(centre)
    Request_Time = time.time()
    Count_Pixels("static.png")
    Count_Time = time.time()
    y=time.time()
    duration = y-x
    print(Request_Time-x)

Caculate_Area()