import os
from helper import *

def friendadd(friendname: str) -> None:
    """
    Creates a friend with a specified name and stores them in the master list of friends.txt.
    This friend is part of no other lists initially.
    
    Example use: friendadd friendname
    
    Parameter:
    friendname (str): Name of friend to add.
    
    Return:
    None
    """
    friendname = friendname.strip()
    
    # Check for valid name
    if not checkValid(friendname):
        updatelog(f"Invalid name entered: {friendname}. Name was not added to the list.")
        return

    # Check for empty file AKA first call
    if os.stat("friends.txt").st_size == 0:
        set_ownername(friendname)
        
        with open("friends.txt", 'a') as file:
            file.write(f"{friendname}\n")
            updatelog(f"{friendname} was added as owner. View profile to make additional changes.")
    
    # Can only be called by the owner
    elif (get_username() != get_ownername()):
        updatelog(f"{get_username} does not have permission to invoke this method.")
        return
    
    # When called by the owner
    else:
        
        with open("friends.txt", 'r') as file:
            friends = file.readlines()
        
        # Checking for pre-existing friend
        for friend in friends:
            if friendname == friend.strip():
                updatelog(f"{friendname} already exists in the friends list.")
                return
        
        with open("friends.txt", 'a') as file:
            
            file.write(f"{friendname}\n")
            updatelog(f"{friendname} was added as friend.")

    # Only reached in cases 1 and 4 AKA new profile or owner adding a unique friend
    add_to_list_in_masterlist("all_friends", friendname)
    return

def viewby(friendname: str) -> None:
    """
    Attempts to view a profile as a given user.
    
    Example use: viewby friendname
    
    Parameter:
    friendname (str): Name of friend to log in as.
    
    Return:
    None
    """
    # Check logged in status
    if get_is_logged():
        updatelog(f"Current user: {get_username()}. Must first log out to change user.")
        return
    
    friendname = friendname.strip()
    
    # Check for valid name
    if not checkValid(friendname):
        updatelog(f"Invalid name entered: {friendname}. Name cannot be used.")
        return
    
    # Check if friend exists in list
    with open("friends.txt", 'r') as file:
        friends = file.readlines()
    
    for friend in friends:
        # If friend found in list
        if friendname == friend.strip():
            set_is_logged(True)
            set_username(friendname)
            updatelog(f"Viewing profile of {get_ownername()} as {friendname}.")
            return
    
    # If friend does not exist
    updatelog(f"Could not find {friendname} in the friends list.")
    return

def logout() -> None:
    """
    Logs out the current user from viewing a profile.
    
    Example use: logout
    
    Parameter:
    None
    
    Return:
    None
    """
    # Check logged in status
    if isLogged:
        updatelog(f"User {get_username()} has been logged out.")
        set_is_logged(False)
        set_username("")
    else:
        updatelog("No user has been logged in.")
    
    return
    
def listadd(listname: str) -> None:
    """
    Creates a unique empty list to which friends may be added.
    Can only be executed by the profile owner.
    
    Example use: listadd listname
    
    Parameter:
    listname (str): Name of list to add.
    
    Return:
    None
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return
    # Check if owner
    elif (get_username() != get_ownername()):
        updatelog("Only profile owner can use this command.")
        return
    
    listname = listname.strip()
    
    # Check for valid name
    if (not checkValid(listname)) or (listname == "nil"):
        updatelog(f"Invalid name entered: {listname}. Name cannot be used.")
        return
    
    
    all_lists = get_list_from_masterlist("all_lists")
    
    # Check for pre-existing name
    for item in all_lists:
        if listname == item:
            updatelog(f"{listname} is not available.")
            return
    
    # If unique list name
    add_to_masterlist(listname)
    add_to_list_in_masterlist("all_lists", listname)
    updatelog(f"Registered {listname}.")
    return

def friendlist(arg: str) -> None:
    """
    Adds a friend to a list.
    Can only be executed by the profile owner.
    If the friend or list does not exist, displays an error message.

    Example use: friendlist friendname listname
    
    Parameter:
    arg (str): Combination of friendname and listname with a space in between.
    
    Return:
    None
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return
    # Check if owner
    elif (get_username() != get_ownername()):
        updatelog("Only profile owner can use this command.")
        return
    
    # Separating args
    parts = arg.split(' ', 1)
    friendname = parts[0].strip()
    listname = parts[1].strip()
    
    # Finding reference lists
    friends = get_list_from_masterlist("all_friends")
    lists = get_list_from_masterlist("all_lists")
    
    # Check for valid name
    if (not checkValid(friendname)) or (friendname == "nil"):
        updatelog(f"Invalid friend name entered: {friendname}. Name cannot be used.")
        return
    # Check if it exists
    if friendname not in friends:
        updatelog(f"{friendname} is not part of the friends list.")
        return
        
    # Check for valid name
    if (not checkValid(listname)) or (listname == "nil"):
        updatelog(f"Invalid list name entered: {listname}. Name cannot be used.")
        return
    # Check if it exists
    if listname not in lists:
        updatelog(f"{listname} list does not exist.")
        return
    
    # if valid list name and friend name
    add_to_list_in_masterlist(listname, friendname)
    return

def postpicture(arg: str) -> None:
    """
    Posts a unique picture to the user's profile.
    The profile owner or a friend must be viewing the profile to execute this command.
    The owner of the file is set to the person currently viewing the profile.
    No list is associated with the picture at first.
    Default permissions are rw -- --.

    Example use: postpicture picturename.txt
    """

def chlst(arg: str) -> None:
    """
    Changes the list associated with a picture.
    The profile owner or a friend must be viewing the profile to execute this command.
    
    When being viewed by a friend, owned pictures can only be assigned lists to which the owner belongs.
    Profile owners can change the list associated with a file to any valid list.
    
    To dissociate a picture from all lists, use "nil" as the listname.
    If the specified picture or list does not exist, displays an error message.
    
    Example use: chlst picturename.txt listname
    """

def chmod(arg: str) -> None:
    """
    Changes the access permissions associated with a picture.
    
    First rw are profile owner permissions
    Second rw are designated permissions
    Third rw are public permissions
    
    Example use: chmod picturename.txt rw r- --
    """
    
def chown(arg: str) -> None:
    """
    Changes the owner of a file.
    This command can only be executed by the owner of a profile.
    If the specified picture or friendname does not exist, displays an error message.
    
    Example use: chown picturename.txt friendname
    """

def readcomments(arg: str) -> None:
    """
    Displays name and comments on the picture.
    Access is granted on the basis of r permissions associated with the list.
    If the picture doesn't exist, displays an error.
    
    Example use: readcomments picture.txt
    """
    
def writecomments(arg: str) -> None:
    """
    Allows viewing the picture and adding a comment to it.
    Access is granted on the basis of w permissions associated with the list.
    If the picture doesn't exist, displays an error.
    
    Example use: writecomments picturename.txt sometext
    """
    
def end() -> None:
    """
    Exits the program.

    Example use: end
    """