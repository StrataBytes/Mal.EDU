@echo off
setlocal

::@StrataBytes, Github. GPLv3

:: Delete the scheduled tasks
schtasks /delete /tn "MicrosoftEssentialsLogin" /f
schtasks /delete /tn "EssentialsContinuous" /f

:: Remove the executable from the Startup folder
set ExeName=csrss.exe
if exist "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\%csrss.exe%" (
    del "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\%csrss.exe%"
    echo Removed %ExeName% from Startup.
) else (
    echo Could not find %ExeName% in Startup. It might have been moved or deleted. (Did you rename it?!)
)

echo Scheduled tasks and executable cleanup complete.
pause

:end
