from cryptography.fernet import Fernet

def generateKey():
    return Fernet.generate_key()

def saveKeytofile(key):
    with open ('key.key', 'wb') as key_file:
        key_file.write(key)

def loadKeyfromfile():
    file = open ('key.key', 'rb')
    key = file.read()
    file.close()
    return key

def encrypt_pwd(password,key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password)
    return encrypted_password.encode('utf-8')

def decrypt_pwd(encrypted_password,key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password)

    return decrypted_password.decode()


master_pwd = input("Enter the master's password: ")
key = generateKey() + master_pwd.encode()
saveKeytofile(key)

def add():
    name = input('Account name: ')
    password = input('Password: ')
    with open ('password.txt','a') as f:
        f.write(name + '|' + encrypt_pwd(password,key) + '\n')

def view():
    with open ('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            acc,passw = data.split("|")
            print("Account: ",acc," Password: ",(decrypt_pwd(passw,key).encode()).decode())


while True:
    mode = input("Would you like to add new password or view existing ones (add/view), write q to quit program: ").lower()

    if mode == 'q':
        quit()

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print('Invalid mode.')
        continue 