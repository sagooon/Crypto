# Crypto

Cryptography is the science of protecting information by encoding it into a secure format. Crypto is an information security tool used for encrypting and decrypting confidential data to prevent it being exploited by third party between the communication channel. It is based on the basic function of cryptography machine. It is an uncomplicated script with less than 25 lines of code. It uses a secrect key code with 39 minimum characters including numbers and alphabets for the data encryption and decryption. Data encrypted with a key code can be decrypted by the same key code only. In such way the third party between a communication channel cannot access to confidential data. It's not so advanced but can be used for general purpose. It was developed by [SaGoOn](http://sagooon.renderforestsites.com).


![crypto](https://user-images.githubusercontent.com/74248485/99026212-962e4600-2592-11eb-860c-82c460e3f30f.png)


## Requirements

Latest version of [python](https://python.org) must be installed on your system. A secret key code must be generated using every characters from 0 to 9 and a to z which must be at least 39 characters of code. You can also use other symbols. The key code in the script must be modified manually for changing it. Code modification can be done just by replacing the code in the variable named 'keys'. We recommend you to use [visual code studio](https://code.visualstudio.com/) as the text editor for programming. Also install python in visual code studio from extension panel. Make sure you setup these requirements.


## Key code

~~~
ml4hu9rscg085iv1byxf6tzp3jdn2koe7aqw #
~~~




## Basic Execution

```

def crypto():
    keys = "ml4hu9rscg085iv1byxf6tzp3jdn2koe7aqw #"
    value = keys[-1] + keys[0:-1]
    
    encryptDict = dict(zip(keys, value))
    decryptDict = dict(zip(value, keys))

    message = input("Data to proceed : ")
    mode = input("Mode : encrypt (E) OR decrypt (D) : ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter] 
                                for letter in message.lower()]) 
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter] 
                                for letter in message.lower()])
    else: 
        print("Error : Enter the correct choice : ")
                
    return newMessage.capitalize()



print(crypto())
