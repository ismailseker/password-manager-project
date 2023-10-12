master_pwd = input("Enter the master's password: ")

def add():
    name = input('Account name: ')
    password = input('Password: ')

    with open ('password.txt','a') as f:
        f.write(name + '|' + password + '\n')

def view():
    with open ('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            acc,passw = data.split("|")
            print("Account: ",acc," Password: ",passw)



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