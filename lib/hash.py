from pwdlib import PasswordHash


passHash = PasswordHash.recommended()

def HasPassword(password:str)->str:
    return passHash.hash(password)

def VerifyPassword(password:str, hashPassword:str)->bool:
    return passHash.verify(password,hashPassword)

