# Global variables
isLogged = False
ownerName = ""
userName = ""

# Getters and setters

def set_is_logged(status: bool) -> None:
    """
    Sets the login status.
    
    Parameters:
    status (bool): The login status to set.
    
    Return:
    None
    """
    global isLogged
    isLogged = status

    return

def get_is_logged() -> bool:
    """
    Gets the current login status.
    
    Parameters:
    None
    
    Returns:
    bool: The current login status.
    """
    return isLogged

def set_username(username: str) -> None:
    """
    Sets the username.
    
    Parameters:
    username (str): The username to set.
    
    Return:
    None
    """
    global userName
    userName = username
    
    return

def get_username() -> str:
    """
    Gets the current username.
    
    Parameter:
    None
    
    Returns:
    userName (str): The current username.
    """
    return userName

def set_ownername(ownername: str) -> None:
    """
    Sets the owner's name.
    
    Parameters:
    ownername (str): The owner's name to set.
    
    Return:
    None
    """
    global ownerName
    ownerName = ownername
    
    return

def get_ownername() -> str:
    """
    Gets the current owner's name.
    
    Parameter:
    None
    
    Returns:
    ownerName (str): The current owner's name.
    """
    return ownerName
