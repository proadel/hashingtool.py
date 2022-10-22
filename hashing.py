import hashlib
from hashlib import * 
style = ''' 
by : Adel MD. Umbrella +967733477848
 _   _           _   _____           _ 
| | | |         | | |_   _|         | |
| |_| | __ _ ___| |__ | | ___   ___ | |
|  _  |/ _` / __| '_ \| |/ _ \ / _ \| |
| | | | (_| \__ \ | | | | (_) | (_) | |
\_| |_/\__,_|___/_| |_\_/\___/ \___/|_|
'''
print (style)
print ("===============================================")
print ("Hash Chaker[1] , Hash Length[2] , Hash Type[3]")
print ("MD5 Encrypt[4] , MD5 Decryption[5]")
print ("===============================================")

choose = input("Please Select [x] Option,or ENTER for Exit : ")
if choose == '1':
        print("This Option for Hash Chacker")
        hash1 = input("Enter Hash [1] : ")
        hash2 = input("Enter Hash [2] : ")
        if hash1 == hash2 :
                print("The Hash is Clean")
        else: 
                print("The Hash is Virus")
                
if choose == '2':
        print("This Option for Hash Length")
        length = input("Enter your Hash : ")
        print("Length Hash is :", len(length))
if choose == '3':
        print("This Option for Hash Type")
        hash = input("Enter your Hash :")
        length = len(hash)
        if length == 32 :
                print("The Hash is [MD5]")
        if length == 40 :
                print("The Hash is [sha1]")
        if length == 64 :
                print("The Hash is [sha256]")
if choose == '4':
        print("This Option for Text to MD5")
        word = input("Enter your Text : ")
        md5 = hashlib.md5(word.encode())
        print(md5.hexdigest())
if choose == '5':
        print("This Option for MD5 Decryption")
        hash = input("Enter your Hash : ")
        file = input("Write File Name : ")
        with open(file , mode='r') as f :
                 for line in f :
                         line = line.strip()
                         if md5(line.encode()).hexdigest() == hash :
                                 print("[-] Password Found :" +line)
                         else:
                                 print("Password can Not Found - work Hard Next Time")
