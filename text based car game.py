#simple text based car game
user = input()

while True:
    if user.lower() == 'help':
        user = str(input('start - to start the car\nstop - to stop the car\nquit - to exit\n'))
    if user.lower() == 'start':
        user = str(input('the car has been started\n'))
    if user.lower() == 'stop':
        user = str(input('the car has been stopped\n'))
    if user.lower() == 'quit':
        break
    else:
        print('I dont understand that')
        user = input()