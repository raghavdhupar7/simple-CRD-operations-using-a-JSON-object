import time           #importing desired modules
import sys 
import json     

try:
    f = open("savedFile.txt", "r")    #Reading a file as stated in the question The file name should be the same as "savedFile.txt" 
    for x in f:               # the JSON object must be str, not 'TextIOWrapper'  that's why converting it to normal string
        s = x
    hash = json.loads(s)     # the result is a Python dictionary
    for x in f:
        s = x
    print(hash)
except:
    hash = dict()  #creating a dictionary if no file is provided

def create(key, value, timeout = 0): #create function with key, value, and timeout is given as parameters (timeout is taken 0 incase nothing is coming from the main function)
    if key not in hash:
        if len(hash) < 1024**3 and value <= 16*(1024**2):  #file size constraint which is 1GB and value contraint which is 16KB
            if timeout == 0:       # This means no Timeout was provided and it is considering it as a 0
                l = [value, timeout]
            else:
                l = [value, time.time() + timeout]    # If the timeout is given we are adding that timeout with the current time value of the system
            if len(key) <= 32:           # Key size contraint which is 32 Characters
                hash[key] = l 
        print("successfully added the Key-value pair")   #if the key-value pair is successfully added
    else:
        print("\n")
        print("Error!!!!!! " + "This Key Already Exists") #Error, if the key-value pair is not successfully added
        time.sleep(2)                                     #sleeping because giving some time to the user to read the output clearly

def read(key):   #read function with key is given as a parameter 
    if key in hash:        #checking if that key is already present or not
        temp = hash[key]      #taking another variable temp and using this variable only for the further operations
        if temp[1] != 0:        #the 1st element is present in the key that means the timeout value was also present 
            if time.time() < temp[1]:      #checking if the timeout got expired or not 
                res = str(key) + ":" + str(temp[0])      #if it isnt expired then executing this and returning the res
                return res
            else:
                print("Error!!!!!!! " + "Time-To-Live for a key has expired")   #if it's expired then printing the error message
        else:        #if the timeout was'nt present in the beginning then executing this part 
            res = str(key) + ":" + str(temp[0])     #just normal retrival of the Key-Value pair
            return res
    else:
        print("Error!!!!!!!!!! " + "This Key Doesnt Exists. Please enter a new one.")       #if the key is not present then printing the Error

def delete(key):    #delete function with key is given as a parameter 
    if key in hash:        #checking if that key is already present or not
        temp = hash[key]      #taking another variable temp and using this variable only for the further operations
        if temp[1] != 0:        #the 1st element is present in the key that means the timeout value was also present
            if time.time() < temp[1]:      #checking if the timeout got expired or not 
                del hash[key]                   #if it isnt expired then executing this and deleting the key-value pair      
                print("Successful", "Key is Deleted successfully")    #and printing that it got deleted 
            else:
                print("Error", "Time-To-Live for this key has expired")   #if it's expired then printing the error message
        else:           #if the timeout was'nt present in the beginning then executing this part 
            del hash[key]   #just normal retrival and deletion of the Key-Value pair
            print("Successful", "Key is Deleted successfully")     

def returning():     #Using this function to return our key-value pair which is stored in dict
    return hash      #and we will use this dictionary to write the data into a output file.


if __name__ == "__main__":    #Main function in which the input is taken.
    
    flag = False                  #We will use this flag to check if we have added ANY key-pair or not, cuz that way we will able to export the data. It will get clear in next part of the code.
    
    while True:                      #The program will run infinitely UNLESS it is force stopped OR QUIT/EXIT is provided in the input
        print("\n")
        print("\n")
        print("\n")
        print("WHAT DO YOU WANNA DO?\n")       #Taking normal inputs to execute Create, Read, and Delete operations.
        print("1. Create a Key\n")
        print("2. Read a Key\n")
        print("3. Delete a Key\n")
        if flag == True:               #The Flag was False in the beginning so if its True only then we will show this choice.
            print("4. Quit and save this program\n")      
        t = input()
        t = t.rstrip()

        if t == '1':          #Creating a Key-value pair
            print("\n")
            print("\n")
            print("\n")
            print("Enter Key with its Value and with its TTL value(optional)\n") 
            print("\n")
            print("\n")
            print("\n")
            arr = [v for v in input().split()]           #taking input and splitting it and storing it in an array. for ex: if input = RAGHAV 20 100, arr will be ["RAGHAV", "20", "100"]
            if len(arr) == 3:  #if length of arr is equal to 3, that means timeout is also provided
                create(arr[0], int(arr[1]), int(arr[2]))    #executing create function and passing key, value and timeout as parameters
            elif len(arr) == 2:   #if length of arr is equal to 2, that means timeout is not provided
                create(arr[0], int(arr[1]))             #executing create function and passing key,and value as parameters
            else:                #if length of arr is other than 3 or 2 that means input is given wrongly and printing the error
                print("input is wrongly given. Please enter the input carefully")
            flag = True
            continue


        elif t == '2':          #Reading a Key-value pair
            print("Enter Key you are looking for\n")
            s = input()        #taking an input in form of string and storing it in a variable name 's'
            s = s.rstrip()
            print("\n")
            print("\n")
            ans = read(s)       #executing read function and passing key as a parameter.
            print(ans)          #printing the output we get from the read function
            print("\n")
            print("\n")
            print("\n")


        elif t == '3':          #Deleting a Key-value pair
            print("Enter Key you want to delete\n")
            s = input()         #taking an input in form of string and storing it in a variable name 's'
            s = s.rstrip()
            delete(s)            #executing delete function and passing key as a parameter.
            time.sleep(2)         #making the program to sleep for 2 seconds as it get messier because of the excessive use of the print statements 


        elif t == '4' and flag == True:           #Writing all key-value pairs in a output file.
            print("Exiting and saving the Key-Value pairs in a file")
            dictionary = returning()        #calling the returning function which will return our hash/dictionary
            try:                            #using Try and Except, in case of any internal error comes 
                file = open('savedFile.txt', 'wt')         #statement to create a new file.
                y = json.dumps(dictionary)                  #using dumps to convert the dictionary into JSON string 
                # the result is a JSON string:  
                file.write(y)                               #writing the JSON string to the file.
                file.close()                                #closing the file
            except:
                print("Unable to write to file")            #if any error comes we will print this error 
                print("\n")
            sys.exit()


        elif t != "QUIT" or input()!= "Quit" or input()!= "quit" or input()!= "Exit" or input()!= "EXIT" or input()!= "Q" or input()!= "q" or input()!= "exit":
            print("Incorrect Option!!!!!!\n")    #all these statements handles if any other input is given other than 1, 2, 3 
            print("\n")
        time.sleep(2)                 #sleeping, because why not? 