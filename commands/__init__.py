from helper import *

def friendadd(arg: str) -> None:
    """
    Creates a friend with a specified name and stores them in friends.txt.
    
    Example use: friendadd friendname
    """
    
    friendname = arg
    updatelog("test")

def viewby(arg: str) -> None:
    """
    Checks if the friend is in the friends list.
    If they are, they can view the user's profile.
    If not, displays an error message.
    Other commands can only be used when viewing a profile.
    
    Example use: viewby friendname
    """

def logout() -> None:
    """
    Logs out the current user from viewing a profile.
    
    Example use: logout
    """
    
def listadd(arg: str) -> None:
    """
    Creates a unique empty list to which friends may be added.
    Can only be executed by the profile owner.
    Lists cannot be created with the name "nil".
    
    Example use: listadd listname
    """

def friendlist(arg: str) -> None:
    """
    Adds a friend to a list.
    Can only be executed by the profile owner.
    If the friend or list does not exist, displays an error message.

    Example use: friendlist friendname listname
    """

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