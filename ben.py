a = 0
if a == 1:
    print('Goodbye, ' + str(name) + '.')

print('Hello! I am a bot and my name is Ben.')
print('What is your name?')

#Things that bot knows:
namememory = list ()
goodpoints = 0
badpoints = 0

realname = input()
nickname = realname[0] + realname[1]
name=realname
namememory.append(name)

def greeting():
    print('Hello, ' + str(name) + ', welcome to Bos website!')

import cgitb cgitb.enable()
start_response('200 OK', [('Content-Type', 'text/html')])

#Ben gets to know u
print(greeting())

#Ben determains what to call you
while True:
    print('Mind if i call you ' + str(nickname) + '?')
    print('Yes or no?')
    isnicknameokay = input()

    if isnicknameokay == 'no':
        print('Great! I like you, ' + str(nickname) + '.')
        name = nickname
        break

    if isnicknameokay == 'yes':
        print('Okay, ' + str(realname) +  ' :(')
        print('Do you have any other nickname in mind? (answer yes or no)')
        othernickname = input()
        if othernickname == 'no':
            name = realname
            break
        if othernickname == 'yes':
            print('What is your preferred nickname?')
            newnickname = input()
            name = newnickname
            print(str(name) + '... I like it! (Even though youre not as creative as me)')
            break

    else:
        print('Answer the goddamn question (with small letters and without spaces)')

print('You are cool, ' + str(name) + '.')
