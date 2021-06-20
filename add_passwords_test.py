# check that text file exists just in case
import os.path

def check_existence():
    if os.path.exists('passwords.txt'):
        pass
    else:
        file = open('passwords.txt', 'w')
        print('Creating new file...')
        file.close()

# function can be used to append passwords.txt
def append_file():
   
    # opens file for appending
    with open('passwords.txt', 'a') as file:
        
        print('\n')

        # get user input for info
        user_in = input('Enter username: ')
        pass_in = input('Enter password: ') 
        web_in = input ('Enter website address or title: ')

        # setup how info will be appended to the file
        user = 'Username: ' + user_in + '\n'
        passw = 'Password: ' + pass_in + '\n'
        web = 'Website: ' + web_in + '\n'

        # append info to passwords.txt then close
        file.write('-------------------------------------- \n')
        file.write(user)
        file.write(passw)
        file.write(web)
        file.write('-------------------------------------- \n')
        file.write('\n')
        file.close() 

# function for reading paswords.txt
def read_file():
    
    with open('passwords.txt', 'r') as file:

        # read and output file contents
        content = file.read()
        file.close()
        print(content)

# make functions execute upon calling add_passwords.py
if __name__ == '__main__':
    check_existence()
    append_file()
    read_file()
