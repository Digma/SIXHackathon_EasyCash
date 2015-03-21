from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.clock import Clock
from multiprocessing import Process, Queue
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.progressbar import ProgressBar

from api.activity import *
from data.users import *
from server.server import *
from server.db import *

# Set ID user in
user_phone_number = "+41798701746"
Builder.load_string("""
<RootWidget>:
    _screen_manager: _screen_manager

    grid_layout_group: grid_layout_group

    label_balance: balance_label
    label_balance2: balance_label2
    label_balance3: balance_label3

    id_name: id_name
    id_pay: id_pay
    id_amount: id_amount

    req_from: req_from
    req_name: req_name
    req_amount: req_amount
    pb:pb

    payment_success_label: payment_success_label

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, 1
            id: _screen_manager

			Screen:
				name: 'screen0'
                BoxLayout:
                    ##size_hint: 1, 1
                    orientation: 'vertical'
                    BoxLayout:
                        padding: 2
                        size_hint: 1, 0.04
                        orientation: 'horizontal'
                        cols: 2
                        Label:
                            size_hint: .8, .1
                            id: balance_label2
                            text: ""
                        Button:
                            size_hint: .2, .1
                            text: '+'
                            on_press: _screen_manager.current = 'screen2'
                    BoxLayout:
                        size_hint: 1, 0.9
                        orientation: 'vertical'
                        cols: 1
                        Label:
                            text: "No transactions."
                            italic: True

            Screen:
                name: 'screen1'
                GridLayout:
                    size_hint: 1, .4
                    cols: 2
                    padding: 2
                    Label:
                        id: balance_label3
                        text: ""
                    Button:
                        text: 'Create a Group'
                        on_press: _screen_manager.current = 'screen2'
                    Button:
                        text: 'Pay'
                        on_press: _screen_manager.current = 'screen2a'
                    Button:
                        text: 'Request'
                        on_press: _screen_manager.current = 'screen2b'
                    Button:
                        text: 'Transactions'
                        on_press: _screen_manager.current = 'screen2c'
                    Button:
                        text: 'settings'
                        on_press: _screen_manager.current = 'screen2d'
            Screen:
                name: 'screen2'
                BoxLayout:
                    size_hint: 1, 1
                    orientation: 'vertical'

                    BoxLayout:
                        padding: 2
                        size_hint: 1, 0.04
                        orientation: 'horizontal'
                        cols: 3
                        Button:
                            size_hint: .2, .1
                            text: '<-'
                            on_press: _screen_manager.current = 'screen0'
                        Label:
                            size_hint: .6, .1
                            id: "New Payment"
                            text: ""
                        Button:
                            size_hint: .2, .1
                            text: 'QR Code'

                    GridLayout:
                        id: grid_layout_group
                        padding: 20
                        space: [10, 5]
                        cols: 2
                        size_hint: 1, 0.80
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: "Title"
                        TextInput:
                            id: id_name
                            multiline: True
                            font_size: 16
                            text: str(root.server_json["restaurant"]["name"])
                            ##on_text: root.update_id_name(id_name, args[1])
                        Label:
                            text: "Recipient"
                        TextInput:
                            id: id_pay
                            text: str(root.server_json["restaurant"]["phoneNumber"])
                            multiline: False
                            font_size: 16
                            ##on_text: root.update_id_pay(id_pay, args[1])
                        Label:
                            text: "Amount"
                        TextInput:
                            id: id_amount
                            font_size: 16
                            multiline: False

                            text: str(root.server_json["restaurant"]["price"])
                            ##on_text: root.update_id_amount(id_amount, args[1])
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        AnchorLayout:
                            anchor_x: 'center'
                            Button:
                                text: "+ Friends"
                                on_press: _screen_manager.current = 'screen_people_list'

                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Button:
                            text: "Cancel"
                            on_press: _screen_manager.current = 'screen1'
                        Button:
                            text: "Valid"
                            on_press: _screen_manager.current = 'screen4'

            Screen:
                name: 'screen2b'
                BoxLayout:
                    size_hint: 1, 1
                    orientation: 'vertical'

                    BoxLayout:
                        padding: 2
                        size_hint: 1, 0.04
                        orientation: 'horizontal'
                        cols: 3
                        Button:
                            size_hint: .2, .1
                            text: '<-'
                            on_press: _screen_manager.current = 'screen0'
                        Label:
                            size_hint: .6, .1
                            id: "New Payment"
                            text: ""
                        Button:
                            size_hint: .2, .1
                            text: 'Cam'

                    GridLayout:
                        id: grid_layout_group
                        padding: 20
                        space: [10, 5]
                        cols: 2
                        size_hint: 1, 0.80
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: "Title"
                        TextInput:
                            id: id_name
                            multiline: True
                            font_size: 16
                            text: str(root.server_json["restaurant"]["name"])
                            ##on_text: root.update_id_name(id_name, args[1])
                        Label:
                            text: "Recipient"
                        TextInput:
                            id: id_pay
                            text: str(root.server_json["restaurant"]["phoneNumber"])
                            multiline: False
                            font_size: 16
                            ##on_text: root.update_id_pay(id_pay, args[1])
                        Label:
                            text: "Amount"
                        TextInput:
                            id: id_amount
                            font_size: 16
                            multiline: False

                            text: str(root.server_json["restaurant"]["price"])
                            ##on_text: root.update_id_amount(id_amount, args[1])
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: "Me"
                        Label:
                            text: "50%"
                        Label:
                            text: str(root.server_json["userA"]["nom"])
                        Label:
                            text: "50%"
                        Label:
                            text: ""
                        AnchorLayout:
                            anchor_x: 'center'
                            Button:
                                text: "+ Friends"
                                on_press: _screen_manager.current = 'screen_people_list'

                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Button:
                            text: "Cancel"
                            on_press: _screen_manager.current = 'screen1'
                        Button:
                            text: "Valid"
                            on_press: root.createGroup()
                            on_press: _screen_manager.current = 'screen4'

            Screen:
                name: 'screen2c'
                BoxLayout:
                    size_hint: 1, 1
                    orientation: 'vertical'

                    BoxLayout:
                        padding: 2
                        size_hint: 1, 0.04
                        orientation: 'horizontal'
                        cols: 3
                        Button:
                            size_hint: .2, .1
                            text: '<-'
                            on_press: _screen_manager.current = 'screen0'
                        Label:
                            size_hint: .6, .1
                            id: "New Payment"
                            text: ""
                        Button:
                            size_hint: .2, .1
                            text: 'Cam'

                    GridLayout:
                        id: grid_layout_group
                        padding: 20
                        space: [10, 5]
                        cols: 2
                        size_hint: 1, 0.80
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: "Title"
                        TextInput:
                            id: id_name
                            multiline: True
                            font_size: 16
                            text: str(root.server_json["restaurant"]["name"])
                            ##on_text: root.update_id_name(id_name, args[1])
                        Label:
                            text: "Recipient"
                        TextInput:
                            id: id_pay
                            text: str(root.server_json["restaurant"]["phoneNumber"])
                            multiline: False
                            font_size: 16
                            ##on_text: root.update_id_pay(id_pay, args[1])
                        Label:
                            text: "Amount"
                        TextInput:
                            id: id_amount
                            font_size: 16
                            multiline: False

                            text: str(root.server_json["restaurant"]["price"])
                            ##on_text: root.update_id_amount(id_amount, args[1])
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: "Me"
                        Label:
                            text: "50%"
                        Label:
                            text: str(root.server_json["userB"]["nom"])
                        Label:
                            text: "50%"
                        Label:
                            text: ""
                        AnchorLayout:
                            anchor_x: 'center'
                            Button:
                                text: "+ Friends"
                                on_press: _screen_manager.current = 'screen_people_list'

                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Label:
                            text: ""
                        Button:
                            text: "Cancel"
                            on_press: _screen_manager.current = 'screen0'
                        Button:
                            text: "Valid"
                            on_press: root.createGroup()
                            on_press: _screen_manager.current = 'screen4'



			Screen:
				name: 'screen_people_list'
				BoxLayout:
					size_hint: 1., .5
					orientation: 'vertical'
					spacing: 10
				    Label:
				        font_size: 24
				        text: "Friend List"
					Button:
						text: str(root.server_json["userA"]["nom"])
						on_press: _screen_manager.current = 'screen2b'
						on_press: root.add_user(str(root.server_json["userA"]["nom"]),str(root.server_json["userA"]["phoneNumber"]))
					Button:
                        text: str(root.server_json["userB"]["nom"])
						on_press: _screen_manager.current = 'screen2c'
						on_press: root.add_user(str(root.server_json["userB"]["nom"]),str(root.server_json["userB"]["phoneNumber"]))
                    Label:
					    text: ""
                    Label:
					    text: ""
					Button:
						text: 'Back'
						on_press: _screen_manager.current = 'screen2'
					Label:
					    text: ""
                    Label:
					    text: ""
			Screen:
			    id: 'sc3'
                name: 'screen3'
				GridLayout:
					size_hint: 1, .4
                    cols: 2
					Label:
                        text: "Name:"
					TextInput:
                        text: id_name.text
					Label:
                        text: "Id name:"
					TextInput:
                        text: id_pay.text
					Label:
                        text: "Amount:"
					TextInput:
                        text: id_amount.text + " CHF"
                    Button:
                        text: "Request"
                    Button:
                        text: "specific request"

					Button:
                        text: "Cancel"
						on_press: _screen_manager.current = 'screen0'
                    Button:
                        text: "Valid"
						on_press: _screen_manager.current = 'screen4'
			Screen:
                name: 'screen4'
                BoxLayout:
                    size_hint: 1, 1
                    orientation: 'vertical'

                    BoxLayout:
                        padding: 2
                        size_hint: 1, 0.04
                        orientation: 'horizontal'
                        cols: 3
                        Button:
                            size_hint: .2, .1
                            text: '<-'
                            on_press: _screen_manager.current = 'screen0'
                        Label:
                            size_hint: .8, .1
                            id: "New Payment"
                            text: ""
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint: 1, .8
                        cols: 5
                        padding: 10

                        Label:
                            font_size: 24
                            text: root.server_json["conversationC"]["title"]
                        Label:
                            text: ""
                        Label:
                            font_size: 14
                            text_size: self.size
                            height: 80
                            multiline: True
                            text: root.server_json["restaurant"]["description"]
                        Label:
					        text: ""
                        Label:
					        text: ""

                        Label:
                            text: 'Progression: {}%'.format(int(pb.value))
                            size_hint_y: None
                            height: '24dp'

                        ProgressBar:
                            size_hint_x: 1.
                            id: pb
                            size_hint_y: None
                            height: '96dp'
                            value: 0 % 100.

                        BoxLayout:
                            orientation: 'horizontal'
                            cols: 2
                            Label:
                                font_size: 24
                                height: 40
                                text: root.server_json["conversationC"]["userA"]["nom"]
                            Label
                                text: root.server_json["conversationC"]["userA"]["part"]
                        BoxLayout:
                            orientation: 'horizontal'
                            cols: 2
                            Label:
                                font_size: 24
                                text: root.server_json["conversationC"]["userB"]["nom"]
                            Label
                                text: root.server_json["conversationC"]["userB"]["part"]

                        Label:
					        text: ""
                        Label:
					        text: ""
					    Label:
					        text: ""
                        Label:
					        text: ""
					    Label:
					        id: payment_success_label
					        text: root.payment_success

                        ##Button:
                        ##    text: "Pay"
                        ##    on_press: _screen_manager.current = 'screen5c'
                        ##    on_press: root.createGroup()
			Screen:
                name: 'screen5a'
				Label:
                    markup: True
                    text: '[size=24]Total amount'
			Screen:
                name: 'screen5b'
				Label:
                    markup: True
                    text: '[size=24]Who has paid'
			Screen:
                name: 'screen5c'
				Label:
                    markup: True
                    text: '[size=24]Done!'
			Screen:
                name: 'screen2a'
				Button:
					text: "Back"
					on_press: _screen_manager.current = 'screen1'
			Screen:
                name: 'screen2d'
				Button:
					text: "Back"
					on_press: _screen_manager.current = 'screen1'

			Screen:
				name: 'screen_request'
				Label:
					text: "you've got request"
				Button:
					text: "Decline"
				Button:
					text: "Accept"

			Screen:
			    id: id_sc_popup
			    name: 'screen_popup'
			    AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'center'
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint: 0.5, 0.5
                        Label:
                            text: "You have a Request:"
                        Label:
                            id: req_from
                            text: ""
                        Label:
                            id: req_name
                            text: ""
                        Label:
                            id: req_amount
                            text: ""
                        Label:
                            id: balance_label
                            text: ""
                        GridLayout:
                            size_hint: 1, .4
                            cols: 2
                            Button:
                                text: "Cancel"
                                on_press: _screen_manager.current = 'screen0'
                                on_press: root.rejectRequest()
                            Button:
                                text: "Valid"
                                on_press: _screen_manager.current = 'screen4'
                                on_press: root.acceptRequest()
				""")


class RootWidget(FloatLayout):
    # Interface
    _screen_manager = ObjectProperty(None)
    sc3 = ObjectProperty(None)
    id_pay = ObjectProperty(None)
    id_name = ObjectProperty(None)
    id_amount = ObjectProperty(None)

    req_from = ObjectProperty(None)
    req_name = ObjectProperty(None)
    req_amount = ObjectProperty(None)
    payment_success_label = ObjectProperty(None)

    balance_str = ""
    balance_int = 0
    label_balance = ObjectProperty()

    payment_success = ""

    #User accounts
    state, header, data = signin(user_phone_number)
    sessiontoken_usr1 = header['sessiontoken']
    smscode_usr1 = data['smscode']

    # Group
    conversation_name = []
    conversation_number = []

    state, header = login(sessiontoken_usr1, smscode_usr1)
    if state == 200:
        usertoken_usr1 = header['usertoken']
        transaction = []
    else:
        raise Exception("Connection failed")
    #Other users

    # Fake server
    server_json = json

    #Group class
    amount_group = 0.0
    to_group = ""
    request = []
    balance_group = 0.0

    def __init__(self, **kwargs):
        from kivy.core.window import Window
        Window.size = (320, 480)
        Clock.schedule_interval(self.checkBalance, 1)
        Clock.schedule_interval(self.checkRequest, 1)
        Clock.schedule_interval(self.checkGroup, 1)
        super(RootWidget, self).__init__(**kwargs)
        #self.workers[1].start()
        #self.workers[2].start()
        #self.workers[3].start()
        #Clock.schedule_interval(self.checkisrunning, 0.1)
        #Clock.schedule_interval(self.getblockinfo, 1)

        #Clock.schedule_interval(self.checkname, 0.1)

    # def update_id_pay(self, id_pay, str):
    #     self.id_pay = str
    #
    # def update_id_name(self, id_name, str):
    #     self.id_name = str
    #
    # def update_id_amount(self, id_amount, str):
    #     self.id_amount = str

    def add_user(self, name, phoneNumber):
            self.conversation_name.append(name)
            self.conversation_number.append(phoneNumber)

    def checkBalance(self, dt):
        """Try to update balance stats"""
        try:
            state, header, data = get_balance(self.usertoken_usr1)
            if state == 200:
                self.balance_int = data['balance']
                self.balance_str = str(self.balance_int)
                self.label_balance.text = "Current Balance: " + self.balance_str
                self.label_balance2.text = "Current Balance: " + self.balance_str
                self.label_balance3.text = "Current Balance: " + self.balance_str
            else:
                print "Balance check failed"
        except:
            pass

    def checkRequest(self, dt):
        try:
            self.transaction = []
            state, header, data = get_all_activities(self.usertoken_usr1)
            for req in data:
                if req['status'] == 4:
                    print "Found request " + str(req['id']) + " for " + str(req['amount'])
                    self.transaction.append(req['id'])
                    break
            if self.transaction:
                print "Show popup transaction"
                self.load_popup(req)
        except:
            pass

    def checkGroup(self, dt):
        if hasattr(self, 'group'):
            self.group.get_balance()
            balance_group = self.group.current / self.group.amount
            self.pb.value = balance_group*100.
            if balance_group >= 1.0:
                self.payment_success_label.text = "Payment Success!"

    def load_popup(self, req):
        self.req_name.text = self.server_json["conversationC"]["title"]
        self.req_amount.text = "Amount: " +str(req['amount'])
        self.req_from.text = "TransactionId: " + str(req['id'])
        self.label_balance.text = "Current Balance: " + self.balance_str
        self._screen_manager.current = 'screen_popup'

    def sendPaiment(self, amount, to):
        # User2 send money to user 1 from its credit card
        data_payment =  {"phoneNumber": to,
                         "amount": amount,
                         "comment": "Hello World"}

        status, header, databack = sendMoney(self.usertoken_usr1, data_payment)
        if status == 200:
            print "Payment succeeded"
        else:
            print "Error: could not make payment"

    def createGroup(self):
        print "Creating Group"
        try:
            self.amount_group = float(self.id_amount.text)
        except:
            print "Failed: Incorrect Amount in create Group"
        self.to_group = self.server_json["restaurant"]["phoneNumber"]
        self.request = [[self.server_json["userA"]["phoneNumber"], 0.5*self.amount_group]]
        self.group = createGroup(self.id_name.text, self.amount_group, self.to_group, self.request)
        self.sendPaiment(0.5*self.amount_group, self.to_group)
        #self.group.makeRequests()

    def acceptRequest(self):
        # If wallet has enough money
        data = {}
        status, header = accept_request(self.usertoken_usr1 , data, self.transaction[0])
        self.transaction.pop(0)
        if status == 200:
            print "Request accepted"
        else:
            print "Failed to accept request"

    def rejectRequest(self):
        status, header = reject_request(self.usertoken_usr1 , self.transaction[0])
        self.transaction.pop(0)
        if status == 200:
            print "Request accepted"
        else:
            print "Failed to accept request"

    def sendGroupPayment(self, group, amount):
        # User2 send money to user 1 from its credit card
        data_payment =  {"phoneNumber": group.phoneNumber,
                         "amount": amount,
                         #"comment": "Hello World",
                         "loadAmount" : "50.0",
                         "creditCardId": user1_creditcard,
                         "loadFee": "0.50"}

        state, header, data = sendMoney(self.usertoken_usr1, data_payment)
        if state == 200:
            print "Payment succedeed"
        else:
            print "Payment failed"

    def cancelPayment(self):
        pass

class TestApp(App):
    def build(self):
        return RootWidget()
        #return Phone()

if __name__ == '__main__':
    TestApp().run()


"""
TextInput:
    on_text: app.search(args[1])

Opacity:
spellbtn.opacity = 0'
"""

def checkbalance(self, dt):
        """Try to update balance stats"""
        return

def transferfunds(self):
    """initiate transfer of funds to new address"""