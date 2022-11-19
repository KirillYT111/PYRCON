from rcon.source import Client
import yaml
print('PYRCON 2')
print('Loading the configuration file...\n')
#
with open('rcon.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
    servername = prime_service['servername']
    serverip = prime_service['serverip']
    rconport = prime_service['rconport']
    rconpassword = prime_service['rconpassword']
    onliallowcmd = prime_service['onliallowcmd']
    allowcmds = prime_service['allowcmds']
    commandslimit = prime_service['commandslimit']
    discordnotify = prime_service['discordnotify']
    chenelname = prime_service['chenelname']
print('Loading the language...')
with open('lang.yml','r') as file:
  prime_service = yaml.safe_load(file)
  connecting = prime_service['connecting']
  connectingsit = connecting.split(sep='/servername/')
  disconnect0 = prime_service['disconnect0']
  disconnect1 = prime_service['disconnect1']
  ckrashprotect = prime_service['ckrashprotect']
  noavalibecmd = prime_service['notavalibecmd']
  connected = prime_service['connected']
  lang = prime_service['lang']
print(f'Loaded {lang}.\n')
print(connectingsit[0] + servername + connectingsit[1] + '\n')
with Client(serverip, rconport, passwd = rconpassword) as client:
    if discordnotify == 'true':
        response = client.run(f'discordbroadcast {chenelname} {connected}')
        print(response)
    print('\nИспользуйте .disconnect для отключения\nИспользуйте .krash чтобы предотвратить краш\n')
    #
    for number in range(commandslimit):
        rconcmd = input('rconcmd >')
        if rconcmd == '.disconnect':
            response = client.run(f'discordbroadcast {chenelname} {disconnect1}')
            print(response)
            exit(disconnect0)
        elif rconcmd == '.krash':
          response = client.run('whitelist on')
          print(response)
          response = client.run('kickall')
          print(response)
          response = client.run(f'say {ckrashprotect}')
          print(response)
        else:
          if onliallowcmd == 'true':
            if rconcmd in allowcmds:
              response = client.run(rconcmd)
              print(response)
            else:
              print(noavalibecmd)
          else:
            response = client.run(rconcmd)
            print(response)
