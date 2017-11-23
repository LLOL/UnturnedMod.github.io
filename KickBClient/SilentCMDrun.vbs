Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c CCEE.bat"
oShell.Run strArgs, 0, false