__author__ = 'G'

import json
import requests
import urllib2

def signin(phoneNumber):
    url = "https://ppp.ti8m.ch/hackathon/signin/"+ phoneNumber + "/"
    r = requests.get(url)
    return r.status_code, r.headers, r.json()

def register(sessiontoken, smscode):
    url_register = "https://ppp.ti8m.ch/hackathon/signin/register/"+ str(smscode) + "/"
    header = {'sessiontoken': sessiontoken}
    r = requests.get(url_register, headers=header)
    print r.status_code
    print r.text
    print r.headers

    return r.status_code, r.headers

def register_finish(registrationtoken, user_data):
    """
    User data under the form
    data = {"firstname":"Max",
            "lastname": "Muster",
            "email": "max.muster@example.com",
            "pin": "1234"}

    :param registrationtoken:
    :param user_data:
    :return:
    """
    url_final = "https://ppp.ti8m.ch/hackathon/signin/register/finish/"
    header = {'registrationtoken': registrationtoken,
               'Content-Type': 'application/json'}

    jdata = json.dumps(user_data).encode('utf-8')
    r = requests.put(url_final, data=jdata, headers=header)

    return r.status_code, r.headers

def login(sessiontoken, smscode):
    header = {'sessiontoken': sessiontoken}
    url_login = "https://ppp.ti8m.ch/hackathon/signin/login/" + str(smscode) + "/"
    r = requests.get(url_login, headers=header)
    return r.status_code, r.headers

def get_credit_card(usertoken):
    header = {'usertoken': usertoken}
    url = "https://ppp.ti8m.ch/hackathon/creditcard/"
    r = requests.get(url, headers=header)
    return r.status_code, r.headers, r.json()

def add_credit_card(usertoken, card_data):
    """
    Card data ahve the following form
    data = {"number":"1234567890123456",
            "preferred": "true",
            "expiration": "04/15",
            "code": "123"}
    :param usertoken:
    :param card_data:
    :return:
    """
    url_final = "https://ppp.ti8m.ch/hackathon/creditcard/"
    header2 = {'usertoken': usertoken,
               'Content-Type': 'application/json'}

    jdata = json.dumps(card_data).encode('utf-8')
    r = requests.put(url_final, data=jdata, headers=header2)
    return r.status_code, r.headers, r.json()

def sendMoney(usertoken, data):
    """
    Transaction data have the following form
    data = {"phoneNumber": phoneNumber,
        "amount": "50.00",
        "comment": "Hello World"}
    :param usertoken:
    :param data:
    :return:
    """
    # send Money
    url = "https://ppp.ti8m.ch/hackathon/balance/transaction/send/"
    header = {'usertoken': usertoken,
               'Content-Type': 'application/json'}
    jdata = json.dumps(data).encode('utf-8')
    r = requests.put(url, data=jdata, headers=header)
    return r.status_code, r.headers, r.json

def requestMoney(usertoken, data):
    """
    data = {"phoneNumber": phoneNumber,
            "amount": "50.00",
            "comment": "Hello World"}
    :param usertoken:
    :param data:
    :return:
    """

    url = "https://ppp.ti8m.ch/hackathon/balance/transaction/request/"
    header = {'usertoken': usertoken,
               'Content-Type': 'application/json'}
    jdata = json.dumps(data).encode('utf-8')
    r = requests.put(url, data=jdata, headers=header)
    return r.status_code, r.headers

def loadMoney(usertoken, data):
    """
        {
          "amount": 0,
          "fee": 0,
          "creditCardId": 0
        }
    :param usertoken:
    :param data:
    :return:
    """
    url = "https://ppp.ti8m.ch/hackathon/balance/transaction/load/"
    header = {'usertoken': usertoken,
               'Content-Type': 'application/json'}
    jdata = json.dumps(data).encode('utf-8')
    r = requests.put(url, data=jdata, headers=header)
    return r.status_code, r.headers

def accept_request(usertoken, data, transactionid):
    """
    data = {"loadAmount": "23.30",
            "creditCardId": "123",
            "loadFee": "0.50"}
    :param usertoken:
    :param data:
    :return:
    """

    url = "https://ppp.ti8m.ch/hackathon/activity/accept/" + str(transactionid) + "/"
    header = {'usertoken': usertoken,
               'Content-Type': 'application/json'}
    jdata = json.dumps(data).encode('utf-8')
    r = requests.post(url, data=jdata, headers=header)
    return r.status_code, r.headers

def get_balance(usertoken):
    """
    r.text:
    {"balance":"99.95"}
    :param usertoken:
    :return:
    """
    url = "https://ppp.ti8m.ch/hackathon/balance/"
    header = {'usertoken': usertoken}
    r = requests.get(url,  headers=header)
    return r.status_code, r.headers, r.json()

def get_all_activities(usertoken):
    url = "https://ppp.ti8m.ch/hackathon/activity/activities/"
    header = {'usertoken': usertoken}
    r = requests.get(url,  headers=header)
    return r.status_code, r.headers, r.json()

def reject_request(usertoken, transactionid):
    url = "https://ppp.ti8m.ch/hackathon/activity/reject/" + str(transactionid) + "/"
    header = {'usertoken': usertoken,
               'Content-Type': 'application/json'}
    r = requests.post(url, headers=header)
    return r.status_code, r.headers