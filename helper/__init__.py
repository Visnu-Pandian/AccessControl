def clean_directory() -> None:
    """
    Ensures clean directory on program start.
    Creates files if needed and empties existing files.
    
    Parameter:
    None
    
    Return:
    None
    """
    file_list = ["friends, audit, pictures, lists"]
    
    for file in file_list:
        new = open(f"{file}.txt", "w")
        new.close()

def obtain_command(string: str) -> str | str:
    """
    Bisects commands and arguments into separate strings.
    
    Parameter:
    string (str): The command line to be parsed.
    
    Return:
    parts[0] (str): The command.
    parts[1] (str): The arguments.
    """
    parts = string.split(" ", 1)
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
    
    print(arg)
