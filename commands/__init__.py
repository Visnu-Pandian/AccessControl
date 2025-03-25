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

def friendlist(args: str) -> None:
    """
    Adds a friend to a list.
    Can only be executed by the profile owner.
    If the friend or list does not exist, displays an error message.

    Example use: friendlist friendname listname
    
    Parameter:
    args (str): Combination of friendname and listname with a space in between.
    
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
    parts = args.split(' ', 1)
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
    
    # If valid list name and friend name
    add_to_list_in_masterlist(listname, friendname)
    return

def postpicture(picname: str) -> None:
    """
    Posts a unique picture to the user's profile.
    The profile owner or a friend must be viewing the profile to execute this command.
    The owner of the file is set to the person currently viewing the profile.
    No list is associated with the picture at first.
    Default permissions are rw -- --.

    Example use: postpicture picturename.txt
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return

    picname = picname.replace(".txt", "")
    picname = picname.strip()
    
    # Check for valid name
    if (not checkValid(picname)) or (picname == "nil"):
        updatelog(f"Invalid picture name entered: {picname}. Name cannot be used.")
        return
    
    all_pictures = get_list_from_masterlist("all_pictures")
    
    # Check for pre-existing name
    for pic in all_pictures:
        if picname == pic:
            updatelog(f"{picname} is not available.")
            return
    
    # If valid picture name
    with open(f"{picname}.txt", 'w') as picture:
        picture.write(f"{picname}\n")
    
    pic_to_masterlist(picname, get_username())
    add_to_list_in_masterlist("all_pictures", picname)
    updatelog(f"Post created: {picname}.")
    return

def chlst(args: str) -> None:
    """
    Changes the list associated with a picture.

    When being viewed by a friend, owned pictures can only be assigned lists to which the owner belongs.
    Profile owners can change the list associated with a file to any valid list.
    
    To dissociate a picture from all lists, use "nil" as the listname.
    
    Example use: chlst picturename.txt listname
    
    Parameters:
    args (str): Combination of picture name and list name.
    
    Return:
    None
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return

    # Separating args
    parts = args.split(' ', 1)
    picname = parts[0].replace(".txt", "").strip()
    listname = parts[1].strip()
    
    pictures = get_list_from_masterlist("all_pictures")
    lists = get_list_from_masterlist("all_lists")
    
    # Check for valid name
    if (not checkValid(picname)) or (picname == "nil"):
        updatelog(f"Invalid picture name entered: {picname}. Name cannot be used.")
        return
    # Check if it exists
    if picname not in pictures:
        updatelog(f"{picname} does not exist.")
        return
    
    # Check for valid name
    if not checkValid(listname):
        updatelog(f"Invalid picture name entered: {picname}. Name cannot be used.")
        return
    # Check if it exists
    if listname not in lists:
        updatelog(f"{listname} does not exist.")
        return
    
    # If valid picture and valid list
    picture = get_list_from_masterlist(picname)
    selected_list = get_list_from_masterlist(listname)
    username = get_username()
    
    # Check permissions
    if (username == get_ownername()):
        
        # Deleting old picture data and adding new instance
        remove_from_masterlist(picname, "all_pictures")
        pic_to_masterlist(picname, picture[1], listname, picture[3], picture[4], picture[5])
        add_to_list_in_masterlist("all_pictures", picname)
        updatelog(f"Changed list associated with picture {picname}: {listname}.")
        
    elif (username == picture[0].strip()):
        
        # If user is part of selected list
        if username in selected_list:
            
            remove_from_masterlist(picname, "all_pictures")
            pic_to_masterlist(picname, listname)
            add_to_list_in_masterlist("all_pictures", picname)
            updatelog(f"Changed list associated with picture {picname}: {listname}.")
            
        # If user is not a part of selected list
        else:
            updatelog(f"You do not have permission to add list {listname} to picture {picname}.")
    else:
        updatelog(f"You do not have permission to edit this photo: {picname}.")
    
    return

def chmod(args: str) -> None:
    """
    Changes the access permissions associated with a picture.
    
    First rw are profile owner permissions
    Second rw are designated permissions
    Third rw are public permissions
    
    Example use: chmod picturename.txt rw r- --
    
    Parameter:
    args (str): Combination of picture name and permissions
    
    Return:
    None
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return
    
    # Separating args
    parts = args.split(' ', 3)
    picname = parts[0].replace(".txt", "").strip()
    ownerperms = parts[1].strip()
    posterperms = parts[2].strip()
    publicperms = parts[3].strip()
    
    pictures = get_list_from_masterlist("all_pictures")
    valid_perms = ["rw", "r-", "-w", "--"]
    permlist = [ownerperms, posterperms, publicperms]
    
    # Check for valid name
    if (not checkValid(picname)) or (picname == "nil"):
        updatelog(f"Invalid picture name entered: {picname}. Name cannot be used.")
        return
    # Check if it exists
    if picname not in pictures:
        updatelog(f"{picname} does not exist.")
        return
    
    # Check for valid perms
    for perm in permlist:
        if perm not in valid_perms:
            updatelog(f"Invalid permissions entered: {perm}.")
            return
    
    # If valid picture and valid perm values
    picture = get_list_from_masterlist(picname)
    username = get_username()
    
    # Check permissions
    if (username == get_ownername()) or (username == picture[0].strip()):
        
        # Deleting old picture data and adding new instance
        remove_from_masterlist(picname, "all_pictures")
        pic_to_masterlist(picname, picture[0], picture[1], ownerperms, posterperms, publicperms)
        add_to_list_in_masterlist("all_pictures", picname)
        updatelog(f"Permissions of picture {picname} changed to: {ownerperms}, {posterperms}, {publicperms}.")
        
    else:
        updatelog(f"You do not have permission to edit this photo: {picname}.")
    
    return
    
def chown(args: str) -> None:
    """
    Changes the owner of a file.
    This command can only be executed by the owner of a profile.
    If the specified picture or friendname does not exist, displays an error message.
    
    Example use: chown picturename.txt friendname
    
    Parameter:
    args (str): Combination of picture name and new owner name.
    
    Return:
    None
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return
    
    # Separating args
    parts = args.split(' ', 1)
    picname = parts[0].replace(".txt", "").strip()
    friendname = parts[1].strip()
    
    username = get_username()
    
    # Only profile owner can use this function
    if (username != get_ownername()):
        updatelog(f"You do not have permission to edit the owner of this photo: {picname}.")
        return

    pictures = get_list_from_masterlist("all_pictures")
    friends = get_list_from_masterlist("all_lists")
    
    # Check for valid name
    if (not checkValid(picname)) or (picname == "nil"):
        updatelog(f"Invalid picture name entered: {picname}. Name cannot be used.")
        return
    # Check if it exists
    if picname not in pictures:
        updatelog(f"{picname} does not exist.")
        return

    # Check for valid name
    if (not checkValid(friendname)) or (friendname == "nil"):
        updatelog(f"Invalid friendname entered: {picname}. Name cannot be used.")
        return
    # Check if it exists
    if friendname not in friends:
        updatelog(f"{friendname} is not part of the friends list.")
        return
    
    # If valid picture and valid friendname
    picture = get_list_from_masterlist(picname)
    
    # Deleting old picture data and adding new instance
    remove_from_masterlist(picname, "all_pictures")
    pic_to_masterlist(picname, friendname, picture[1], picture[2], picture[3], picture[4])
    add_to_list_in_masterlist("all_pictures", picname)
    updatelog(f"Owner of picture {picname} changed to friend {friendname}.")
    
    return

def readcomments(picname: str) -> None:
    """
    Displays name and comments on the picture.
    Access is granted on the basis of r permissions associated with the list.
    If the picture doesn't exist, displays an error.
    
    Example use: readcomments picture.txt
    
    Parameter:
    picname (str): Name of picture to read comments on.
    
    Return:
    None
    """
    # Check logged in
    if not isLogged:
        updatelog("Must be logged in to use this command.")
        return
    
    picname = picname.replace(".txt", "").strip()
    
    pictures = get_list_from_masterlist("all_pictures")
    # Check for valid name
    if (not checkValid(picname)) or (picname == "nil"):
        updatelog(f"Invalid picture name entered: {picname}. Name cannot be used.")
        return
    # Check if it exists
    if picname not in pictures:
        updatelog(f"{picname} does not exist.")
        return
    
    # Getting permissions
    picture = get_list_from_masterlist(picname)
    picowner = picture[0]
    piclist = picture[1]
    ownerperms = picture[2]
    listperms = picture[3]
    publicperms = picture[4]
    username = get_username()
    
    # Checking permissions
    if username == get_ownername():
        pass
    elif (username == picowner):
        if (ownerperms[0] == "r"):
            pass
        else:
            updatelog(f"User {username} does not have read permissions on this photo: {picname}.txt.")
    elif (username in piclist):
        if (listperms[0] == "r"):
            pass
        else:
            updatelog(f"User {username} does not have read permissions on this photo: {picname}.txt.")
    elif (publicperms[0] == "r"):
        pass
    else:
        updatelog(f"User {username} does not have read permissions on this photo: {picname}.txt.")
    
    with open(f"{picname}.txt", 'r') as file:
        lines = file.readlines()
    
    
    updatelog(f"Reading picture {picname} as {username}.")
    for line in lines:
        print(f"{line}\n")
    
    return
    
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