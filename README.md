# Assignment for Software Engineering Intern Role (Backend) at Leap

I've Tried creating a Simple Create, Read and Delete program for Key-value pair using Dictionary data-structure in Python.
It was a simple, learing, yet a fun Assignment which made me learn new things such as how to use time(), sleep() and JSON modules of sys and Json library resp.

# what does sleep module do?
The sleep() function suspends (waits) execution of the current thread for a given number of seconds.

# what does time module do?
The sleep() function suspends (waits) execution of the current thread for a given number of seconds.

# What does JSON modules do?
We can Use it to directly convert our string type key-pairs to dictionary and can perform operations like READ, CREATE and DELETE very easily.

# The data store will support the following functional requirements.
1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key isalways a string - capped at 32 chars. The value is always a JSON object - capped at 16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7. Appropriate error responses always be returned to a lenient if it uses the data store in unexpected ways or breaches any limits.

# Explanation of the program (explanation is also provided in the code itself) 


CREATE FUNCTION:
    We will add the main functionality after the checks which is to Add the key wrt its value and timeout(if given)

READ FUNCTION:
    We will add the main functionality after the checks which is to Read the key wrt its value.

DELETE FUNCTION:
    We will add the main functionality after the checks which is to Delete the key.
    
RETURNING FUNCTION:
    Returning the whole dictionary in the form of JSON string object so that we can write it into the ouput file. 

MAIN FUNCTION:
    We will add the main functionality after the checks and Inputs taken. This is an operational code with options/commands are provided at each step. So adding Main function was a necessity.