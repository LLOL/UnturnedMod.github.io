Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c CFCF.py"
oShell.Run strArgs, 0, false