from flask import Flask, jsonify, request, abort
import requests
import json

application = Flask(__name__)

@application.route('/')
def filler():
    return 'Carbon Server'

accounts = [
    {
        'id': 1,
        "first_name": u'Bob',
        "last_name": u'Bob',
        "email": u'sealteam6@cap1.com',
        'phone': 12345678,
        'wifi_address': 123456789,
        'card_number': 1234567890,
    
    },
    {
        'id': 2,
        "first_name": u'Jax',
        "last_name": u'Jax',
        "email": u'sealteam6@cap3.com',
        'phone': 12,
        'wifi_address': 8,
        'card_number': 9,
    
    },
    {
        'id': 3,
        "first_name": u'Jax',
        "last_name": u'Jax',
        "email": u'sealteam6@cap3.com',
        'phone': 10,
        'wifi_address': 4,
        'card_number': 5,
    
    }
]

@application.route('/todo/api/v1.0/accounts', methods=['GET'])
def get_accounts():
    return jsonify({'accounts': accounts})

@application.route('/todo/api/v1.0/accounts/<int:account_id>', methods = ['GET'])
def get_account(account_id):
    account = filter(lambda t: t['id'] == account_id, accounts)
    if len(account) == 0:
        abort(404)
    return jsonify( { 'account': account[0] } )

@application.route('/todo/api/v1.0/wifi_address/<int:account_card_number>', methods = ['GET'])
def get_wifi_address(account_card_number):
    account = filter(lambda x: x['card_number'] == account_card_number, accounts)
    if len(account) == 0:
        abort(404)
    return jsonify( { 'account': account[0] } )

@application.route('/todo/api/v1.0/accounts', methods = ['POST'])
def create_account():
    #if not request.json or not 'first_name' in request.json:
        #abort(400)
    account = {
        'id': accounts[-1]['id'] + 1,
        'first_name': request.json['first_name'],
        'last_name': request.json.get('last_name', ""),
        'phone': request.json.get('phone', ""),
        'wifi_address': request.json.get('wifi_address', ""),
        'card_number': request.json.get('card_number', ""),
        'email': request.json.get('email', ""),
    }
    accounts.append(account)
    return jsonify( { 'account': account } ), 201

if __name__ == '__main__':
    application.run(debug=True)