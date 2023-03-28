passwd = 'asdf'
crypto =""
for j in passwd:
    crypto = crypto + "".join(chr((ord(j)-97+3)%26+97))
print(crypto)
