isLogged = False
ownerName = ""
userName = ""

MasterList = {"all_friends": [], "all_lists": [], }

def set_is_logged(arg: bool) -> None:
    global isLogged
    isLogged = arg
    
    return

def get_is_logged() -> bool:
    return isLogged

def set_username(arg: str) -> None:
    global userName
    userName = arg
    
    return

def get_username() -> str:
    return userName

def set_ownername(arg: str) -> None:
    global ownerName
    ownerName = arg
    
    return

def get_ownername() -> str:
    return ownerName

def add_to_masterlist(arg: str) -> None:
    global MasterList
    MasterList[arg] = []
    
    return

def get_masterlist() -> dict:
    return MasterList

def add_to_list_in_masterlist(arg: str, arg2:str) -> None:
    global MasterList
    MasterList[arg].append(arg2.strip())
    
    return

def get_list_from_masterlist(arg: str) -> list[str]:
    return MasterList[arg]

def clean_directory() -> None:
    """
    Ensures clean directory on program start.
    Creates files if needed and empties existing files.
    
    Parameter:
    None
    
    Return:
    None
    """
    file_list = ["friends", "audit", "pictures", "lists"]
    
    for file in file_list:
        new = open(f"{file}.txt", "w")
        new.close()

    return

def checkValid(arg: str) -> None:
    """
    Checks if the entered string is a valid input.
    
    Parameter:
    arg (str): The string to check.
    
    Return:
    True/False
    """
    characters = ["/:\f\t\n\v\r"]
    
    if len(arg.strip()) > 30:
        return False
    
    if any(char in arg for char in characters):
        return False
    
    return True
    
def obtain_command(arg: str) -> str | str:
    """
    Bisects commands and arguments into separate strings.
    
    Parameter:
    arg (str): The command line to be parsed.
    
    Return:
    parts[0] (str): The command.
    parts[1] (str): The arguments.
    """
    parts = arg.split(" ", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    else:
        return parts[0], ''

def updatelog(arg: str) -> None:
    """
    Updates audit log with new actions.
    
    Parameter:
    arg (str): Text to add to audit log.
    
    Return:
    None
    """
    with open("audit.txt", 'a') as file:
        file.write(arg + '\n')
    
    print(arg + '\n')
    
    return
