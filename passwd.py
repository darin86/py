import getpass

def encrypto(password):
    crypto=""
    for j in password:
        crypto = crypto+"".join(chr((ord(j)-97+3)%26+97))
    return crypto
name="root"
passwd=""