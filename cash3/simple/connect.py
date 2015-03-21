__author__ = 'G'

from api.activity import *
from data.users import *


#### Receiver
state, header, data = signin("+41798701749")
sessiontoken_usr1 = header['sessiontoken']
smscode_usr1 = data['smscode']

if data['type'] == 'register':
    exit()

elif data['type'] == 'login':
    state, header = login(sessiontoken_usr1, smscode_usr1)
    usertoken_usr1 = header['usertoken']

state, header, data = get_balance(usertoken_usr1)
print "Balance user1: " + str(data['balance'])


#Load money on account of user 1
#WARNING DOES NOT WORK
# data_load = {
#                   "amount": "50.00",
#                   "fee": "0.50",
#                   "creditCardId": "123"
#             }
#
# state, header = loadMoney(usertoken_usr1, data_load)
# print "Load money state:" + str(state)



##### Sender
state, header, data = signin(user2_phoneNumber)
sessiontoken_usr2 = header['sessiontoken']
smscode_usr2 = data['smscode']

if data['type'] == 'register':
    exit()

elif data['type'] == 'login':
    state, header = login(sessiontoken_usr2, smscode_usr2)
    usertoken_usr2 = header['usertoken']


state, header, data = get_balance(usertoken_usr2)
print "Balance user2: " + str(data['balance'])

# # Add credit card to user 2
# card_data = {"number":"1234567890123458",
#             "preferred": "true",
#             "expiration": "04/15",
#             "code": "123"}
# state, header, data = add_credit_card(usertoken_usr2, card_data)
# print data

# state, header, data = get_credit_card(usertoken_usr2)
# print "Credit card data: " + str(data)
#
# User2 send money to user 1 from its credit card
data_payment =  {"phoneNumber": "+41798701746",
                 "amount": "20.0",
                 #"comment": "Hello World",
                 "loadAmount" : "20.0",
                 "creditCardId": "10",
                 "loadFee": "0.50"}
state, header, data = sendMoney(usertoken_usr1, data_payment)
print "send money credit card state: " + str(state)
#
# # Print balance user 1
# state, header, data = get_balance(usertoken_usr1)
# print "Balance user1: " + str(data['balance'])
data = {"phoneNumber": user1_phoneNumber,
        "amount": "50.00",
        "comment": "Hello World"}
#status, header = requestMoney(usertoken_usr2, data)



state, header, data = get_all_activities(usertoken_usr1)
print str(data)

for e in data:
    if e['status'] == 4:
        print str(e['id'])

if len(data) > 0:
    print "Transation has happened"


data = {}
#status, header = accept_request(usertoken_usr1, data, 94)
status, header = reject_request(usertoken_usr1, 95)
if status == 200:
    print "Request accepted"
else:
    print "Failed to accept request"