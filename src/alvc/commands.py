command_dict = {
    "help": "Prints all the available commands OR provides documentation with a given command.",
    "exit": "Exits the cli",
}


def help_command(command = None) -> None:
    
    if command != None:
        print(command_dict[command])
    else:
        for c in command_dict:
            print("\n" + c + ": " + command_dict[c])


