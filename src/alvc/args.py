import shlex

from . import commands

def parse(argv: list[str]) -> tuple[str | None, list[str]]:
    if not argv:
        return None, []
    
    return argv[0].lower(), argv[1:]

def run(argv: list[str]) -> int:
    name, args = parse(argv)
    if name is None:
        return 0
    
    if name not in commands.COMMANDS:
        print(name + ": is not a valid command")
        return 1
    
    function, _ = commands.COMMANDS[name]
    return function(args)

def run_line(line: str) -> int:
    try:
        argv = shlex.split(line)
    except ValueError as e:
        print("error: " + str(e))
        return 1
    
    return run(argv)