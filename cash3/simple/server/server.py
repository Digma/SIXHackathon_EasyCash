__author__ = 'G'

import requests
from api.activity import *

class Group():
    def __init__(self, name, amount, phoneNumber, requests):
        #Do the registration
        state, header, data = signin(phoneNumber)
        sessiontoken = header['sessiontoken']
        smscode = data['smscode']

        self.name = name
        state, header = login(sessiontoken, smscode)
        self.usertoken = header['usertoken']
        self.phoneNumber = phoneNumber
        self.requests = requests
        self.paid = [False for e in requests]

        # The amount requested
        self.amount = amount
        # The current amount
        self.current = self.get_balance

        self.makeRequests()

    def get_balance(self):
        """
        r.text:
        {"balance":"99.95"}
        :param usertoken:
        :return:
        """
        status , _, data = get_balance(self.usertoken)
        if status == 200:
            self.current = data['balance']
        else:
            print "Error: Could not get balance"

    def makePayment(self, to):
        # User2 send money to user 1 from its credit card
        data_payment =  {"phoneNumber": to,
                         "amount": self.amount,
                         "comment": "Hello World"}

        status, header, databack = sendMoney(self.usertoken, data_payment)
        if status == 200:
            print "Payment succeeded"
        else:
            print "Error: could not make payment"

    def makeRequests(self):
        for e in self.requests:
            data_req = {"phoneNumber": e[0],
                        "amount": str(e[1]),
                        "comment": "Request"}
            status, header = requestMoney(self.usertoken, data_req)
            if status == 200:
                print "Request succeeded"
            else:
                print "Request failed"

    def check_who_paid(self):
        """
        Check who already paid or not
        :return:
        """
        #TODO
        pass

    def dissolve_group(self):
        """Dissolve group after request or a certain laps of time"""
        #TODO
        pass



def createGroup(name, amount, phoneNumber, requests):
    """

    :param amount:
    :param phoneNumber:
    :param requests: [["+4179871746", 10.0],
                      ["+4179871746", 10.0]]
    :return:
    """
    group = Group(name, amount, phoneNumber, requests)
    return group

