#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:23:49 2019
@author: toddford

This script parses the Fed's June 2019 statement to determine whether it still contains the
key word "patient" with respect to the FOMC's monetary policy stance. It also scrapes the
median dot from their projections of the future Fed Funds rate.

"""

import requests
from bs4 import BeautifulSoup
import time
import datetime


def getData():

    Fed_date = datetime.datetime(2019, 6, 19, 13, 0, 0)

    while datetime.datetime.now() < Fed_date:
        time.sleep(1)

    r0 = requests.get('https://www.federalreserve.gov/newsevents/pressreleases/monetary20190619a.htm')

    html = r0.text
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all('p')

    patient = False

    for p in elements:
        if 'no longer exists' in p.text:
            print('NO LONGER EXISTS')
            time.sleep(1)
            getData()

        if 'patient' in p.text:
            patient = True

    if patient:
        print("PATIENT")
    else:
        print("DROPPED")

    r = requests.get("https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20190619.htm")

    html_dots = r.text
    soup_dots = BeautifulSoup(html_dots, "html.parser")
    element_dots = soup_dots.find(text='Federal funds rate')
    dot_2019 = element_dots.find_next('td')
    dot_2020 = dot_2019.find_next('td')
    dot_2021 = dot_2020.find_next('td')

    print(dot_2019.text, dot_2020.text, dot_2021.text)

getData()
time.sleep(3)
getData()
