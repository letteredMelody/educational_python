body = input()
shot = body.replace(' ', '')
body = body.split()

del(body[shot.find('1'): shot.rfind('1') + 1])

print(' '.join(body))