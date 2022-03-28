import configparser

conf = configparser.ConfigParser()
conf.read('settings.ini')


APIPassword = conf['aukabu']['APIPassword']
Token = conf['aukabu']['Token']
Password = conf['aukabu']['Password']

print(Token)
