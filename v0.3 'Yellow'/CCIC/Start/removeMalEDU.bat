@echo off
setlocal

echo MalEDU remover. This version is specific for CCIC.
::@StrataBytes, Github. GPLv3

:: Delete the scheduled tasks
schtasks /delete /tn "MicrosoftEssentialsLogin" /f
schtasks /delete /tn "EssentialsContinuous" /f

:: Remove the executable from the Startup folder
set ExeName=csrss.exe
if exist "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\%csrssQ.exe%" (
    del "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\%csrssQ.exe%"
    echo Removed %ExeName% from Startup.
) else (
    echo Could not find %ExeName% in Startup. It might have been moved or deleted. (Did you rename it?!)
)

echo Scheduled tasks and executable cleanup complete.
pause

:end
