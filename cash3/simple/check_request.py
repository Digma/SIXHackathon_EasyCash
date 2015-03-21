__author__ = 'G'

from api.activity import *
from data.users import *

state, header, data = signin("+41798701749")
sessiontoken_usr2 = header['sessiontoken']
smscode_usr2 = data['smscode']

if data['type'] == 'register':
    exit()

elif data['type'] == 'login':
    state, header = login(sessiontoken_usr2, smscode_usr2)
    usertoken_usr2 = header['usertoken']


state, header, data = get_balance(usertoken_usr2)
print "Balance user2: " + str(data['balance'])


state, header, data = get_all_activities(usertoken_usr2)
print str(data)

for e in data:
    if e['status'] == 4:
        print str(e['id'])

if len(data) > 0:
    print "Transation has happened"