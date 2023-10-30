@ECHO off
cls
:start
cls
ECHO.
ECHO 1. Send File
ECHO 2. Receive File
ECHO 3. Encrypt Upload
ECHO 4. Decrypt Download


set choice=
set /p choice=Type the number to print text.
if not '%choice%'=='' set choice=%choice:~0,1%

if '%choice%'=='1' goto send
if '%choice%'=='2' goto receive
if '%choice%'=='3' goto encrypt
if '%choice%'=='4' goto decrypt

ECHO "%choice%" is not valid, try again
ECHO.
goto start


:send
cls
ECHO FILE SENDER
ECHO.
set key=
set salt=
set file=
set filename=

ECHO Enter Password:
set /p key=
ECHO Enter Salt Key:
set /p salt=

ECHO Generating Hash code...

ECHO Select file to send (In the File folder):
set /p file=

ECHO File Name:
set /p filename=

ECHO.
ECHO Sending File to the client...
ECHO.
ECHO.
python sender.py --key %key% --salt %salt% --file %file% --filename %filename%

pause
goto start

:receive
cls
set key=
set salt=
ECHO FILE RECEIVER
ECHO.
ECHO Enter Password:
set /p key=
ECHO Enter Salt Key:
set /p salt=

ECHO Generating Hash code...
ECHO. 
ECHO Waiting for the sender...

python receiver.py --key %key% --salt %salt%

ECHO File Successfully received!
ECHO. 
pause
goto start

:encrypt
ECHO TEST

goto end

:decrypt

goto end

:end
pause
