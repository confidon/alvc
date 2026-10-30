import sys

def help_command(args: list[str]) -> int:
    if not args:
        for name, (_, description) in COMMANDS.items():
            print(name + ": " + description + "\n")
        return 0
            
    name = args[0].lower()
    if name not in COMMANDS:
        print(name + ": not found")
        return 1
    print(name + ": " + COMMANDS[name][1])
    return 0
        
    
def exit_command(args: list[str]) -> int:
    sys.exit(0)

def echo_command(args: list[str]) -> int:
    print(" ".join(args))
    return 0
    

COMMANDS = {
    "help": (help_command, "Prints all the available commands OR provides documentation with a given command."),
    "exit": (exit_command, "Exits the cli"),
    "echo": (echo_command, "Prints the given text."),
#   "init": (init_command, "Initializes a new album/project. Usage: init <name>"),
}