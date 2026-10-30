import sys

from . import args


def main():
    
    if len(sys.argv) > 1:
        sys.exit(args.run(sys.argv[1:]))
        
    repl()
        
def repl():
    
    while True:
        print()
        try:
            line = input("$ ")
        except (EOFError, KeyboardInterrupt):
            break
        args.run_line(line)
    
        
    