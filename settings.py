'''
settings.py
Settings for the trivia bot
Created 6/22
Authored by Iazma 
'''

USER = ''
PASS = ''
ADMIN_ROLE = ''
CHANNEL_REQUIRED_MSG = 'This must be performed in a channel.'
UNAUTHORIZED_MSG = 'You don\'t have the required permissions to do that.'

try:
    from settingslocal import *
except ImportError:
    pass