import telnetlib


def telnet_test(host: str, port=23, command='status'):
    '''Host must be given as a string. The function will
    connect to a telnet session on the default port unless
    otherwise specified. It will issue the command "status"
    unless the command argument is given'''
    session = telnetlib.Telnet(host, port)
    while True:
        command = command + '\n'
        if command == 'exit':
            break
        else:
            try:
                session.write(command.encode('UTF-8'))
            except Exception as e:
                print(f"somethign went wrong: {e}")
            try:
                response = session.read_all().decode('UTF-8')
            except Exception as f:
                print(f"Something went wroing: {f}")
        command = input('What else would you like to do?\ntype "exit" if you want to quit: ')
    session.close()
    return response
