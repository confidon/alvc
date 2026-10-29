# ALVC (Ableton Live Version Control)

Version control for Ableton Live

Similar to git


## Opening the CLI

### Using UV:

```powershell
uv run alvc
```

### Without uv (Windows PowerShell)

Requires Python 3.14 or newer.

```powershell
py -3.14 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
alvc
```
### Current Commands

```
$ help <command>

Prints information pertaining to the given command 
OR
Prints all available commands if no argument provided
```

```
$ exit

Exit the command line interface
```

