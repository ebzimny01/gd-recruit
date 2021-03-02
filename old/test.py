import sys
import configparser

config = configparser.ConfigParser()
configfile = config.read('config.ini')
if  configfile == []:
    print("config.ini file not found")
    print("Creating config.ini . . . ")
    config['WISCreds'] = {
                    'Username' : '',
                    'Password' : ''
                    }
    with open("config.ini", 'w') as file:
        config.write(file)
else:
    print("config.ini file found")

username = config['WISCreds']['username']
password = config['WISCreds']['password']

config.set('WISCreds', 'username', 'edz')
config.set('WISCreds', 'password', '12345678')
with open("config.ini", 'w') as file:
    config.write(file)
print("ez")