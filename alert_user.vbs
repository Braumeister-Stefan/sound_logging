Dim strMessage, status, objShell

Set objShell = CreateObject("WScript.Shell")
strMessage = WScript.Arguments(0)
status = WScript.Arguments(1)

Set objSpeech = CreateObject("SAPI.SPVoice")

If status = "failed" Then
    ' Low pitch beep for failure
    objShell.Run "cmd /c @echo off & for /l %a in (1,1,2) do @echo \x07", 0, True
    objSpeech.Rate = -4  ' Much slower rate for failed
    objSpeech.Volume = 100  ' Full volume
Else
    ' High pitch beep for success
    objShell.Run "cmd /c @echo off & for /l %a in (1,1,2) do @echo \x07", 0, True
    objSpeech.Rate = 2  ' Faster rate for success
    objSpeech.Volume = 80  ' Slightly lower volume
End If

objSpeech.Speak strMessage