#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:23:49 2019

@author: toddford
"""

import requests
from bs4 import BeautifulSoup
from colorama import Fore
from colorama import Style
import time
import datetime


def getData():
    
    Fed_date = datetime.datetime(2019, 6, 19, 13, 0, 0)
    
    while datetime.datetime.now() < Fed_date:
        time.sleep(1)
    
    r0 = requests.get('https://www.federalreserve.gov/newsevents/pressreleases/monetary20190619a.htm')
  
    
    
    
    html0 = r0.text
    soup0 = BeautifulSoup(html0, "html.parser")
    element0 = soup0.find_all('p')

    patient = False
    
    for p in element0:
        if 'no longer exists' in p.text:
            print('NO LONGER EXISTS')
            time.sleep(1)
            getData()
            
        
        if 'patient' in p.text:
            patient = True
    
    if patient: 
        print(f"{Fore.BLUE}PATIENT PATIENT PATIENT{Style.RESET_ALL}")
    else: 
        print(f"{Fore.GREEN}DROPPED DROPPED DROPPED{Style.RESET_ALL}")
    
    #r = requests.get("https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20190320.htm")
    r = requests.get("https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20190619.htm")
    
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    element = soup.find(text='Federal funds rate')
    dot_2019 = element.find_next('td')
    dot_2020 = dot_2019.find_next('td')
    dot_2021 = dot_2020.find_next('td')
    
    print(f"{Fore.MAGENTA}", dot_2019.text, dot_2020.text, dot_2021.text)

getData()
getData()
getData()


time.sleep(3)

getData()