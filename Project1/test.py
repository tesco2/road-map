import requests


def Get_Map_Image(Location):
    centre = input("Enter Desired Location Here")
    centre.replace(' ','+')
    f=open('static.png','wb')
    #takes a 1000* 1209 meter square from google maps centred on Centre with everthing blackended and the roads highlighted white
    f.write(requests.get('https://maps.googleapis.com/maps/api/staticmap?center='+ centre +'&zoom=16&size=530x640&scale=1&style=visibility:off&style=feature:road|element:geometry|color:0xffffff|visibility:on&sensor=false').content)
    f.close()


Get_Map_Image("35+Atkinson+st+Templestowe")