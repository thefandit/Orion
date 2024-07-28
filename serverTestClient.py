from flask import Flask
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')
    sio.emit('connection', {'auth_type' : 'new_login', 'token' : 'none', 'login_hash' : 'NOTSECUREHASH'}) # valid authentication types are new_login (proceed through authentication) or token (use a given token to establish authentication).
    