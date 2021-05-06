import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os
from flask import Flask,render_template,redirect,url_for,request,session

app=Flask(__name__)

app.secret_key='abcdefghijklmnopqrstuvwxyz'

@app.route('/')
@app.route('/home')
def main():
    url = "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"


    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)

    driver.get(url)

    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")

    i=0
    a=[]
    for child in soup.find('tbody').children:
        b=[]
        for td in child:
            if str(type(td))=="<class 'bs4.element.Tag'>":
                b.append(td.text)
        a.append(b)
    del a[0]
    del a[13]

    return render_template('index.html',data=a)

@app.route('/district/<string:name_data>', methods = ['POST','GET'])
def district(name_data):

    url = "http://dashboard.covid19.ap.gov.in/ims/hospbed_reports/"


    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)

    driver.get(url)

    time.sleep(5)

    driver.find_element_by_link_text(name_data).click()
    
    time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")

    i=0
    a=[]
    for child in soup.find('tbody').children:
        b=[]
        for td in child:
            if str(type(td))=="<class 'bs4.element.Tag'>":
                b.append(td.text)
        a.append(b)
    del a[0]
    del a[len(a)-1]

    return render_template('district.html',data=a)
