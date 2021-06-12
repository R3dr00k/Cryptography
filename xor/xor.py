#!/usr/bin/python
import sys
import re

binary_car = ['0','1'," "]
int_car = ['0','1','2','3','4','5','6','7','8','9',' ']
hex_car = [' ','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']


def check_format(string):
    if all(item in binary_car for item in list(string)):
        type = 'bin'
    elif all(item in int_car for item in list(string)):
        type = 'int'  
    elif all(item in hex_car for item in list(string)):
        type = 'hex'
    else:
        type = 'ascii'

    return type

def dechiffre(msg , key, type_msg , type_key,output='int',file_msg=False, file_key=False):

    if file_msg :
        with open(msg, 'r') as f:
            msg = f.read()[:-1]
           
    if file_key :
        with open(key, 'r') as f:
            key = f.read()[:-1]
           

    if type_msg == 'int' and type_key == 'int':
        base = 10
    elif type_msg == 'hex' and type_key == 'hex':
        base = 16
    elif type_msg == 'bin' and type_key == 'bin':
        base = 2

    value = []

    if type_msg == type_key:
        if type_msg == 'ascii':
            if len(key) > len(msg):
                cle = key[:len(msg)]

            cle = list(key)
            msg = list(msg)
        
            for i ,lettre in enumerate(msg):
                xor = ord(lettre) ^ ord(cle[i % len(cle)])
                value.append(int(xor))
        
        elif type_msg == 'int' or type_msg == 'hex' or type_msg == 'bin':
            if len(key) > len(msg):
                cle = key[:len(msg)]

            msg = msg.split(" ")
            cle = cle.split(" ")

            for c,i in enumerate(msg):
                xor = int(i, base) ^ int(cle[c % len(cle)], base)
                value.append(xor)

        else:
            print('The format is incorrect !!')
            sys.exit()

    else:
        msg2 = []
        key2 = []
        if type_msg == 'ascii':
            for lettre in msg:
                msg2.append(ord(lettre))
        elif type_msg == 'hex':
            msg_hex = msg.split(" ")
            for i in msg_hex:
                msg2.append(int(i , 16))
        elif type_msg == 'bin':
            msg_bin = msg.split(" ")
            for i in msg_bin:
                msg2.append(int(i , 2))

        elif type_msg == 'int':
            msg_int = msg.split(" ")
            for i in msg_int:
                msg2.append(int(i))
        

        if type_key == 'ascii':
            for lettre in key:
                key2.append(ord(lettre))
        elif type_key == 'hex':
            key_hex = key.split(" ")
            for i in key_hex:
                key2.append(int(i , 16))
        elif type_key == 'bin':
            key_bin = key.split(" ")
            for i in key_bin:
                key2.append(int(i , 2))

        elif type_key == 'int':
            key_int = key.split(" ")
            for i in key_int:
                key2.append(int(i))
        

    

        if len(key2) > len(msg2):
            key2 = key2[:len(msg2)]

        for count,i in enumerate(msg2):
            xor = i ^ key2[count % len(key2)]
            value.append(xor)


    if output == 'int':
        valeur = [str(i) for i in value]
        return valeur 

    elif output == 'ascii':
        mot = [chr(i) for i in value]
        return mot

    elif output == 'hex':
        hexa = [hex(i)[2:] for i in value]
        return hexa
    elif output == 'bin':
        binar = [bin(i)[2:] for i in value]
        return binar

if __name__ == '__main__':
    string_arg = sys.argv
    
    correct_form = ['int', 'hex', 'bin' ,'ascii']

    if string_arg[1] == '--help':
        with open('doc', 'r') as f:
            content = f.read()
            print(content)
        sys.exit()

    
    if len(sys.argv ) == 1:
        print('You must use the parameters ( -m , -k, -t ,-o ) . For more detail use --help !')
        sys.exit()

    try:
        if '-m' in string_arg or '-fm' in string_arg: 
            

            if '-m' in string_arg and '-fm' in string_arg:
                print('You cannot specify these two parameters at the same time (-m , -fm)!')
                sys.exit()

            if '-m' in string_arg:
                message = string_arg[string_arg.index('-m') + 1]
                file_msg = False

                if re.search(r'-[a-z]' , message) :
                    print("You must specify the value of -m (message)!")
                    sys.exit()
            
            if '-fm' in string_arg:
                message = string_arg[string_arg.index('-fm') + 1]
                file_msg = True
                if re.search(r'-[a-z]' , message) :
                    print("You must specify the value of -fm (file message)!")
                    sys.exit()
            
        if '-k' in string_arg or '-fk' in string_arg: 
            

            if '-k' in string_arg and '-fk' in string_arg:
                print("You cannot specify these two parameters at the same time (-k , -fk)!")
                sys.exit()

            if '-k' in string_arg :
                key = string_arg[string_arg.index('-k') + 1]
                file_key = False
                if re.search(r'-[a-z]' , key) :
                    print("You must specify the value of -k (key)!")
                    sys.exit()

            if '-fk' in string_arg :
                key = string_arg[string_arg.index('-fk') + 1]
                file_key = True
                if re.search(r'-[a-z]' , key) :
                    print("You must specify the value of -fk (file key)!")
                    sys.exit()


        if '-mt' in string_arg : 
            type_msg = string_arg[string_arg.index('-mt') + 1]

            if re.search(r'-[a-z]' , type_msg) :
                print("You must specify the value of -mt (message type)!")
                sys.exit()
            if type_msg not in correct_form:
                print("The value of the message type is incorrect !")
                sys.exit()
        else:
            type_msg = check_format(message)

        if '-kt' in string_arg : 
            type_key = string_arg[string_arg.index('-kt') + 1]

            if re.search(r'-[a-z]' , type_key) :
                print("You must specify the value of -kt ( key type)")
                sys.exit()
            if type_key not in correct_form:
                print("The value of key type in input is incorrect !")
                sys.exit()
        else:
            
            type_key = check_format(key)


        if '-o' in string_arg :
            output = string_arg[string_arg.index('-o') + 1]

            if re.search(r'-[a-z]' , output) :
                print("You must specify the value of -o (output)")
                sys.exit()
            if output not in correct_form :
                print("The value of output is incorrect !")
                sys.exit()

    except IndexError:
         print("You must specify the necessary parameters ( -m , -k ) and their values \nFor more detail refer to --help")
         sys.exit()

    
    if 'output' in globals():
        print(" ".join(dechiffre(message , key , type_msg, type_key , output ,file_msg , file_key)))
    else:
        print(" ".join(dechiffre(message , key , type_msg , type_key , file_msg, file_key)))