from LSB_Technique import *
from rsa import *
option = str()
while option != 'quit':
    print("To perform LSB Technique , Press 1")
    print("To perform RSA Technique , Press 2")
    print("Type quit to exit")
    print('\n')
    option = input("Enter Command : ")
    if option == '1':
        print("To encrypt a message with the current key, type 'Encrypt'")
        print("To decrypt a message with the current key, type 'Decrypt'")
        print("Type back to go back")
        print('\n')
        choice = str()
        while choice != 'back':
            choice = input("Enter Command: ")
            if choice.lower() == 'encrypt':
                plain_image = input("Enter File Path: ")
                cipher_image = input("Enter the name with which the File is to be Saved: ")
                code_message=input("Enter the secret message: ")
                encoded_image = encode(image_name=plain_image,code_message=code_message)
                cv2.imwrite(cipher_image, encoded_image)
                print("\n")
            elif choice.lower() == 'decrypt':
                decoded_data = decode(cipher_image)
                print("Decoded data:", decoded_data)
                print("\n")
            else:
                if choice != 'back':
                    ii = random.randint(0, 6)
                    statements = ["Oops! Something went wrong", "Please read the directions again", "Didnt say the right word", "This input is UNACCEPTABLE!!","Was that even a word???", "Please follow the directions", "Just type 'help' if you are really that lost"]
                    print(statements[ii])
    elif option == '2':
        print("To redefine n,e, or d, type 'n','e',... etc.")
        print("To encrypt a message with the current key, type 'Encrypt'")
        print("To decrypt a message with the current key, type 'Decrypt'")
        print("Type back to go back")
        print('\n')
        print('\n')
        mm = str()
        mm = str()
        while mm != 'back':
            mm = input("Enter Command: ")
            if mm.lower() == 'encrypt':
                image = input("Enter File Path: ")
                cipher_image = "enc_" + image
                Encrypt(image)
            elif mm.lower() == 'decrypt':
                Decrypt(cipher_image)
            elif mm.lower() == 'n':
                try:
                    print('current n = ', n)
                    n1 = int(input(" Enter a value for n:"))
                    if	n1<2 :
                        print('Invalid input')
                    else :
                        n=n1
                        print('n set to :',n)
                except ValueError:
                    print('please enter a number')
            elif mm.lower() == 'e':
                try:
                    print('current e = ', e)
                    e1 = int(input(" Enter a value for e :"))
                    if	e1<= 2 or gcd(phi(n),e1)!=1:
                        print('Invalid input')
                    else :
                        e=e1
                        print('e set to :', e)
                except ValueError:
                    print('please enter a number')
            elif mm.lower() == 'd':
                try:
                    print('current d = ', d)
                    d1 = int(input(" Enter a value for d :"))
                    if d1 <= 0 and (e*d1)%phi(n)!=1:
                        print('Invalid input')
                    else:
                        d=d1
                        print('d set to :',d)
                except ValueError:
                    print('please enter a number')
            else:
                if mm != 'back':
                    ii = random.randint(0, 6)
                    statements = ["This cannot be done", "Read the directions again", "Didnt say the magic word", "This input is UNACCEPTABLE!!","Was that even a word???", "Please follow thedirections","Just type 'help' if you are really that lost"]
                    print(statements[ii])
    else:
        if option != 'quit':
            i = random.randint(0, 6)
            statements = ["Oops! Something went wrong", "Please read the directions again", "Didnt say the right word", "This input is UNACCEPTABLE!!","Was that even a word???", "Please follow the directions", "Just type 'help' if you are really that lost"]
            print(statements[i])