# AccessControl

The project "AccessControl" implements a simplified version of Facebook called "MyFacebook," focusing on access control mechanisms via the use of dictionaries and lists. The project code is seperated into 4 different python files across the directory, but they all work locally with each other.

## How to run

>> python access.py <inputfile.txt>

This will run the entire program by reading in the pre-written commands from your desired text file.

## How it works

### access.py

The program works by first reading in the contents of the input file using the code in access.py, after which identified commands are passed through a command map which references functions present in other files (namely, /commands/__init__.py).

If there are any errors in the file's syntax or the first command is not "friendadd", it is immediately identified in access.py and the program will make a record of it in the audit logs.

Assuming that the input file has perfect syntax and all inputs are valid, functionality is passed to /commands/__init__.py.

### /commands/__init__.py

This file contains all of the required functions for "AccessControl" to function. Each function is accompanied with comments and examples on how to use them, as well as parameters and return values.

In order to achieve its functionality, this file takes helper methods from /helper/__init__.py and /helper/globals.py and uses them to perform smaller tasks such as user verification, data structure management and update files.

### /helper/__init__.py

The core of the project. This file contains the data structure used to maintain the entire program i.e. the masterlist. The masterlist is actually a large dictionary of lists, each of which reference each other in order for the program to function.

#### Masterlist Hierarchy

Below is a simplified chart representing the hierarchy of the masterlist:

| Key          | Value                            |
|--------------|----------------------------------|
| all_friends  | [Names of all friends...]        |
| all_lists    | [Names of all other lists]       |
| all_pictures | [Names of all pictures/posts]    |
| [List name]  | [Contents...]                    |
| [List name]  | [Contents...]                    |
...

And so on. The first three keys are shorthand lists which maintain the names of all friends as well as other lists within the masterlist for ease of access. Any other lists and pictures can be added in by the user using the commands provided within the program.

List items are stored as key:value pairs with the list name being keys and their listed contents being the values.

The masterlist is managed and referenced using a number of helper methods, each of which have their own decriptions, parameters and return types listed under their function headers.

In summary, the helper methods can be used to add lists and pictures to the masterlist, remove lists and pictures from the masterlist, access the entire masterlist, access specific lists from the masterlist.

There are also other helper methods which are used to perform other functions such as updating the audit log, checking for invalid characters in names,  separating commands and arguments from input strings to name a few.

### /helper/globals.py

The globals.py file is used to maintain all other global variables besides the masterlist, such as the name of the owner, name of the current user and their current login status. It contains getters and setters for all of the relevant variables and is referenced frequently throughout the rest of the project.

## Wrapping up

Once the program has completed its main functions and the end() function has been called, the program proceeds to write all of its collected data into the relevant files "lists.txt" & "pictures.txt". It should be noted that both "friends.txt" & "audit.txt" are updated in real time as the program goes through its functions due to the book-keeping purpose of audit.txt and friends.txt being directly referenced in the program as part of the user verification before login.
