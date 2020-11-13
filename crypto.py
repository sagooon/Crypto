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


