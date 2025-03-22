#!/usr/bin/env python3
import sys
from commands import *
from helper import *

def execute_commands_from_file(file_path: str) -> None:
    """
    Accepts input from a text and executes commands.
    
    Parameter:
    file_path (str) The path of file with commands in it.
    
    Return:
    None
    """
    command_map = {
        "friendadd": friendadd,
        "viewby": viewby,
        "logout": logout,
        "listadd": listadd,
        "friendlist": friendlist,
        "postpicture": postpicture,
        "chlst": chlst,
        "chmod": chmod,
        "chown": chown,
        "readcomments": readcomments,
        "writecomments": writecomments,
        "end": end
    }

    try:
        with open(file_path, 'r') as file:
            updatelog(f"Opening file: {file_path}")
            commands_list = file.readlines()
        
        if not commands_list:
            updatelog("The input file is empty. Terminating the program.")
            return
            
        first_command = obtain_command(commands_list[0].strip())
        if first_command != "friendadd":
            updatelog("The first command must be 'friendadd'. Terminating the program.")
            return
        
        for command_line in commands_list:
            command, argument = obtain_command(command_line.strip())
            
            if command in command_map:
                updatelog(f"Executing command: {command} with arguments: {argument}")
                command_map[command](argument)
            else:
                updatelog(f"Unknown command: {command}")
    except FileNotFoundError:
        updatelog(f"File not found: {file_path}")
    except Exception as e:
        updatelog(f"An error occurred: {e}")

# __main__

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: access <commands_file>")
    else:
        clean_directory()
        commands_file = sys.argv[1]
        execute_commands_from_file(commands_file)
