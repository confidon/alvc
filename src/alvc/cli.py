from . import commands

def main():
    
    active = True;
    
    while active:
        print()
        command = input("$ ")
        
        if command[0:4] == "exit":
            break
        if command[0:4] == "help":
            commands.help_command()

        if command not in commands.command_dict:
            print(command + ": is not a valid command.")
        pass
    
