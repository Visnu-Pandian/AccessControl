import os
from helper.globals import set_is_logged, get_is_logged, set_username, get_username, set_ownername, get_ownername

MasterList = {"all_friends": [], "all_lists": [], "all_pictures": [], }

def add_to_masterlist(listname: str) -> None:
    """
    Adds a new list to the masterlist.
    
    Parameter:
    listname (str): Name of new list to add.
    
    Return:
    None
    """
    global MasterList
    MasterList[listname] = []
    
    return

def pic_to_masterlist(picname: str, username: str, listname: str="nil", perm1: str="rw", perm2: str="--", perm3: str="--") -> None:
    """
    Special case of adding new list.
    Adds a new picture to the masterlist.
    
    Parameter:
    picname (str): Name of new picture to add.
    username (str): Name of owner of picture.
    listname (str): Optional, name of list to add.
    perm1 (str): Optional, picture owner permissions.
    perm2 (str): Optional, picture list permissions.
    perm3 (str): Optional, picture public permissions.
    
    Return:
    None
    """
    global MasterList
    MasterList[picname] = [username, listname, perm1, perm2, perm3]

    return

def get_masterlist() -> dict:
    """
    Returns current masterlist.
    
    Parameter:
    None
    
    Return:
    MasterList (dict): Current masterlist.
    """
    return MasterList

def add_to_list_in_masterlist(listname: str, itemname:str) -> None:
    """
    Adds item to nested list in masterlist.
    
    Parameter:
    listname (str): Name of nested list.
    itemname (str): Name of itemt to add to nested list.
    
    Return:
    None
    """
    global MasterList
    MasterList[listname].append(itemname.strip())
    
    return

def get_list_from_masterlist(listname: str) -> list[str]:
    """
    Returns a nested list from masterlist.
    
    Parameter:
    listname (str): Name of nested list to return.
    
    Return:
    nestedList (list[str]): Nested list.
    """
    nestedList = MasterList[listname]
    return nestedList

def remove_from_masterlist(listname: str, parentname: str) -> None:
    """
    Deletes a list from the masterlist.
    
    Paramter:
    listname (str): Name of list to remove.
    parentname (str): Name of parent list to remove the list from.
    
    Return:
    None
    """
    global MasterList
    
    del MasterList[listname]
    MasterList[parentname].remove(listname)
    
    return

def remove_file(filename: str) -> None:
    """
    Deletes a file from the active directory.
    
    Parameter:
    filename (str): Name of file to delete.
    
    Return:
    None
    """
    try:
        os.remove(filename)
        updatelog(f"File {filename} deleted.")
    except FileNotFoundError:
        updatelog(f"File {filename} not found.")
    except Exception as e:
        updatelog(f"An error occurred while deleting file {filename}: {e}")
        
    return

def remove_picture(picname: str) -> None:
    """
    Deletes a picture from the directory.
    
    Parameter:
    picname (str): Name of picture to delete.
    
    Return:
    None
    """
    remove_file(f"{picname}.txt")
    return
    
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
