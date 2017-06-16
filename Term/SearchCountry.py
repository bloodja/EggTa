from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from xml.dom.minidom import parse, parseString
from tkinter import *
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk
import sys
import tkinter.messagebox

a=[]


g_Tk = Tk()
g_Tk.geometry("1000x650+0+0")
controllSearch = False
iSearchIndex = -1

DataList = None
conn = None
regKey = "3DRxHFGHwyhN9OZIX8Sd8ulg%2BQASwGkEae6T5jJlruKY3bH%2F65q6P0dnkTz5EG6Rcqd7kVuxXe%2B47Jop0aj%2B7Q%3D%3D"
server = "apis.data.go.kr"

def InputImg():
    photo = PhotoImage(file = 'earth.png')
    imageLabel = Label(g_Tk,image=photo, height=40, width=40)
    imageLabel.pack()
    imageLabel.place(x=50, y=3)
    imageLabel.image = photo


def PrintWarningHistory():

    RenderText.delete(0.0, END)
    import http.client
    global conn, regKey, servers
    b=[]

    conn = http.client.HTTPConnection(server)
    uri =   "/1262000/CountryWarningHistoryService/getCountryHistoryList?serviceKey="+regKey+"&numOfRows=20&pageSize=20&pageNo=1&startPage=1"
    conn.request("GET", uri)
    req = conn.getresponse()

    if req.status == 200:
        BooksDoc = req.read()
        if BooksDoc == None:
            RenderText.insert(INSERT,"에러")
        else:
            parseData = parseString(BooksDoc)

            layer1 = parseData.childNodes
            layer2 = layer1[0].childNodes
            layer3 = layer2[1].childNodes
            layer4 = layer3[0].childNodes

            for item in layer4:
                if item.nodeName == "item":
                    finalLayer = item.childNodes
                    title = finalLayer[2].firstChild.nodeValue
                    date = finalLayer[3].firstChild.nodeValue
                    RenderText.insert(INSERT,date)
                    RenderText.insert(INSERT,"\n")
                    RenderText.insert(INSERT,title)
                    RenderText.insert(INSERT,"\n")
                    RenderText.insert(INSERT,"\n")


                    # a = finalLayer[2].firstChild.nodeValue
                    b.append(finalLayer[2].firstChild.nodeValue)
                    b.append(finalLayer[3].firstChild.nodeValue)
                    a.append(b)
                    Favorite()

def PrintEmergencyContact():
    global countryName
    import http.client
    import urllib
    import http.client
    global conn, regKey, servers
    b=[]


    RenderText.delete(0.0, END)
    conn = http.client.HTTPConnection(server)
    hangul_utf8 = urllib.parse.quote(countryName.get())
    uri = "/1262000/ContactService/getContactList?serviceKey=" + regKey + "&numOfRows=10&pageSize=12&pageNo=1&startPage=1&countryName=" +hangul_utf8
    conn.request("GET", uri)
    req = conn.getresponse()

    if req.status == 200:
        BooksDoc = req.read()
        if BooksDoc == None:
            RenderText.insert(INSERT,"에러")
        else:
            parseData = parseString(BooksDoc)

            layer1 = parseData.childNodes
            layer2 = layer1[0].childNodes
            layer3 = layer2[1].childNodes
            layer4 = layer3[0].childNodes
            layer5 = layer4[0].childNodes

            RenderText.insert(INSERT,layer5[0].firstChild.nodeValue)
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")

            b.append(layer5[0].firstChild.nodeValue)
            a.append(b)
            Favorite()

def PrintCountryBasicInform():
    global countryName
    import http.client
    import urllib
    import http.client
    global conn, regKey, servers
    b = []

    RenderText.delete(0.0, END)
    conn = http.client.HTTPConnection(server)
    hangul_utf8 = urllib.parse.quote(countryName.get())
    uri = "/1262000/CountryBasicService/getCountryBasicList?serviceKey=" + regKey + "&numOfRows=10&pageSize=12&pageNo=1&startPage=1&countryName=" +hangul_utf8
    conn.request("GET", uri)
    req = conn.getresponse()

    if req.status == 200:
        BooksDoc = req.read()
        if BooksDoc == None:
            RenderText.insert(INSERT,"에러")
        else:
            parseData = parseString(BooksDoc)

            layer1 = parseData.childNodes
            layer2 = layer1[0].childNodes
            layer3 = layer2[1].childNodes
            layer4 = layer3[0].childNodes
            layer5 = layer4[0].childNodes



            RenderText.insert(INSERT,"위치: ")
            RenderText.insert(INSERT,layer5[1].firstChild.nodeValue)
            RenderText.insert(INSERT,"\n\n")
            RenderText.insert(INSERT, layer5[0].firstChild.nodeValue)
            RenderText.insert(INSERT, "\n")

            b.append(layer5[1].firstChild.nodeValue)
            b.append(layer5[0].firstChild.nodeValue)
            DrawFlag(layer5[5].firstChild.nodeValue)
            a.append(b)
            Favorite()




def PrintAccidentByCountry():
    global countryName
    import http.client
    import urllib
    import http.client
    global conn, regKey, servers
    b = []

    RenderText.delete(0.0, END)
    conn = http.client.HTTPConnection(server)
    hangul_utf8 = urllib.parse.quote(countryName.get())
    uri = "/1262000/AccidentService/getAccidentList?serviceKey=" + regKey + "&numOfRows=10&pageSize=10&pageNo=1&startPage=1&countryName=" +hangul_utf8
    conn.request("GET", uri)
    req = conn.getresponse()

    if req.status == 200:
        BooksDoc = req.read()
        if BooksDoc == None:
            RenderText.insert(INSERT,"에러")
        else:
            parseData = parseString(BooksDoc)

            layer1 = parseData.childNodes
            layer2 = layer1[0].childNodes
            layer3 = layer2[1].childNodes
            layer4 = layer3[0].childNodes
            layer5 = layer4[0].childNodes

            RenderText.insert(INSERT,layer5[6].firstChild.nodeValue)

            b.append(layer5[6].firstChild.nodeValue)
            a.append(b)

            Favorite()


def PrintCountrySafetyInform():

    import http.client
    import urllib
    import http.client
    global conn, regKey, servers
    b =[]

    RenderText.delete(0.0, END)
    conn = http.client.HTTPConnection(server)
    uri = "/1262000/CountrySafetyService/getCountrySafetyList?serviceKey=" + regKey + "&numOfRows=10&pageSize=10&pageNo=1&startPage=1"
    conn.request("GET", uri)
    req = conn.getresponse()

    if req.status == 200:
        BooksDoc = req.read()
        if BooksDoc == None:
            RenderText.insert(INSERT,"에러")
        else:
            parseData = parseString(BooksDoc)

            layer1 = parseData.childNodes
            layer2 = layer1[0].childNodes
            layer3 = layer2[1].childNodes
            layer4 = layer3[0].childNodes
            layer5 = layer4[0].childNodes

            for item in layer4:
                if item.nodeName == "item":
                    date = item.lastChild
                    title = item.childNodes
                    content = item.firstChild

                    RenderText.insert(INSERT,date.firstChild.nodeValue)

                    b.append(date.firstChild.nodeValue)

                    for text in title:
                        if text.nodeName =="title":
                            RenderText.insert(INSERT,text.firstChild.nodeValue)
                            RenderText.insert(INSERT,"\n")
                            RenderText.insert(INSERT,"\n")

                            b.append(text.firstChild.nodeValue)

                    RenderText.insert(INSERT,content.firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "====================================================================================================")

                    b.append(content.firstChild.nodeValue)
                    a.append(b)

                    Favorite()

def InitTopText():
    TempFont = font.Font(g_Tk, size=25, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[여행정보 프로그램]")
    MainText.pack()
    MainText.place(x=100)

def InitInputLabel():
    global countryName
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    countryName = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    countryName.pack()
    countryName.place(x=70, y=195)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=StartFunc)
    SearchButton.pack()
    SearchButton.place(x=390, y=200)

def TravelAlertHistoryButton():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="여행경보 히스토리", command=PrintWarningHistory)
    SearchButton.pack()
    SearchButton.place(x=80, y=50)
def TravelSafetyInform():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="  여행 안전정보  ", command= PrintCountrySafetyInform)
    SearchButton.pack()
    SearchButton.place(x=270, y=50)
def EmergencyContactNetwork():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="   비상 연락망   ",command = SearchButtonAction1 )
    SearchButton.pack()
    SearchButton.place(x=80, y=100)
def AccidentIncident():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text=" 국가별 사건사고 ", command = SearchButtonAction2 )
    SearchButton.pack()
    SearchButton.place(x=270, y=100)
def CountryBasicInform():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="  국가 기본정보  ", command = SearchButtonAction3 )
    SearchButton.pack()
    SearchButton.place(x=80, y=150)
def EMail():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="     E-Mail     ")
    SearchButton.place(x=270, y=150)

def Favorite():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="     즐겨찾기 추가     ", command = Addfavorite )
    SearchButton.place(x=460, y=150)


def DelFavorite():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="     즐겨찾기 초기화     ", command = Delfavorite )
    SearchButton.place(x=460, y=100)

def ReadFavorite():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="     즐겨찾기 조회     ", command = Readfavorite )
    SearchButton.place(x=460, y=50)

def Addfavorite():

    f = open('Favorite.txt', 'a')
    for i in range(len(a)):
        aa = a.pop()
        if type(aa) == 'str':
            f.write(aa)
        else :
            for j in range(len(aa)):
                aaa = aa.pop()
                f.write(aaa)
                f.write('\n')
        f.write('\n\n')
    f.close()


def Delfavorite():
    f = open('Favorite.txt','w')
    f.close()


def Readfavorite():
    f = open('Favorite.txt','r')
    while True:
        line = f.readline()
        if not line:
            break
        RenderText.insert(INSERT, line)
    f.close()



def SearchButtonAction1():
    global iSearchIndex
    iSearchIndex = 0
    InitInputLabel()
    InitSearchButton()
def SearchButtonAction2():
    global iSearchIndex
    iSearchIndex = 1
    InitInputLabel()
    InitSearchButton()
def SearchButtonAction3():
    global iSearchIndex
    iSearchIndex = 2
    InitInputLabel()
    InitSearchButton()

def StartFunc():
    global iSearchIndex
    if iSearchIndex == 0:
        PrintEmergencyContact()
    elif iSearchIndex == 1:
        PrintAccidentByCountry()
    elif iSearchIndex == 2:
        PrintCountryBasicInform()



def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=100, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=70, y=250)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)


def DrawFlag(flagurl):
    url = flagurl
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)

    label = Label(g_Tk, image=image, height=50, width=90)
    label.pack()
    label.place(x=450, y=190)
    label.image = image







DelFavorite()
Favorite()
ReadFavorite()
InitTopText()
InitRenderText()
TravelAlertHistoryButton()
TravelSafetyInform()
EmergencyContactNetwork()
AccidentIncident()
CountryBasicInform()
InitSearchButton()
EMail()
InputImg()

g_Tk.mainloop()

