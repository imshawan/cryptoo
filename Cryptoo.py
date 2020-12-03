"""Encrypter and Decrypter using python's built-in modules
    Dev: Shawan Mandal
"""
import base64
import os
import time
from time import sleep
from colored import fg
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
color = fg(14)
color1 = fg(11)
color2 = fg(10)
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = color1 + fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
# A List of Items
items = list(range(0, 57))
l = len(items)

count='0'
while(count == '0'):
    os.system('cls')
    print(" ")
    print(color1 + "\n\n                      ########################")
    print("                      #        CRYPTO        #")
    print("                      ########################")
    time.sleep(0.02)
    print(" ")

    print(color + "                      1. Encrypt a file")
    print("                      2. Decrypt a file")
    print("                      3. Exit")
    print(" ")
    ans = input("                      ENTER SELECTION.... ")

    if ans == '1':
        print("")
        p = os.getcwd()
        print("                  Enter the filename to be encrypted: ")
        input_file = input("                  %s\\" %p)
        newdir = "Encrypted-DATA"
        path = os.path.join(p, newdir)
        if not os.path.exists(path):
            os.makedirs(path)
            print("                  Directory '%s' Created successfully" %newdir)
        else:
            pass
        output_file = os.path.abspath(path + "\en-" + input_file)
        try:
            with open(input_file, 'rb') as f:
                data = f.read()  # Read the bytes of the input file
            password_provided = input("                  Enter Encryption Key: ")  # This is input in the form of a string
            password = password_provided.encode()  # Convert to type bytes
            salt = b'|\xd8\x99M\xc0C\xee->o\xf8\x90w\xd1\xc50'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
            with open(output_file, 'wb') as f:
                f.write(encrypted)             # Write the encrypted bytes to the output file
            printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            for i, item in enumerate(items):
                time.sleep(0.03)
                # Update Progress Bar
                printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            print(color + "                  Successfully Encrypted!")
            print("                  Output file can be found at: \n                  %s" %output_file)
        except FileNotFoundError:
            print("                  No Such File Exists!")
        input("                  Press any key to continue...")
    elif ans == '2':
        print("")
        p = os.getcwd()
        newdir = "Decrypted-DATA"
        path = os.path.join(p, newdir)
        if not os.path.exists(path):
            os.makedirs(path)
            pass
        else:
            pass
        print("                  Enter the Filename to decrypted: ")
        inputfile = input("                  %s\\"%path)
        input_file = os.path.abspath(path + "\%s" %inputfile)
        output_file = os.path.abspath(path + "\dec-" + inputfile)
        try:
            with open(input_file, 'rb') as f:
                data = f.read()  # Read the bytes of the encrypted file
            password_provided = input("                  Enter your Decryption Key: ")  # This is input in the form of a string
            password = password_provided.encode()  # Convert to type bytes
            salt = b'|\xd8\x99M\xc0C\xee->o\xf8\x90w\xd1\xc50'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            fernet = Fernet(key)
            try:
                decrypted = fernet.decrypt(data)
                with open(output_file, 'wb') as f:
                    f.write(decrypted)  # Write the decrypted bytes to the output file
                    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
                    for i, item in enumerate(items):
                        time.sleep(0.03)
                        # Update Progress Bar
                        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
                print(color + "                  Successfully decrypted")
                print("                  Output file can be found at: \n                  %s" %output_file)
            except InvalidToken as e:
                print("                  Invalid Key - Decryption Terminated")
        except FileNotFoundError:
            print("                  No such file exists!")
        input("                  Press any key to continue...")
    elif ans == '3':
        print("                  Exiting...")
        time.sleep(0.8)
        exit()
    else:
        print("                  Invalid Choice!")
        print("                  Terminating...")
        time.sleep(0.8)
        count='1'
    
