import requests as a
import os as b
import subprocess as c
from bs4 import BeautifulSoup as d

def main():
  tmpl0 = []
  target = input("Enter target root domain: (example.com)")
  try:
    req0 = a.get('https://'+target)
    if req0.status_code==200:
      tmp = req0.text
      maind = d(tmp,'html.parser')
      print("Attempting to gather relative links from target index...")
      for vrt in maind.find_all('a'):
        if target in vrt.get('href') or vrt.get('href').startswith('/'):
          print(vrt.get('href'))
          tmpl0.append(str(vrt.get('href')))
  except:
    print("Error! Closing now :(")

main()
