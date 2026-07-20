@echo off
setlocal EnableExtensions
cd /d "%~dp0"
if exist build\classes rmdir /s /q build\classes
if exist dist\language-variants rmdir /s /q dist\language-variants
mkdir build\classes
mkdir dist\language-variants
javac -encoding UTF-8 -d build\classes AICodingEditor.java
if errorlevel 1 exit /b 1

call :build English English_Default
if errorlevel 1 exit /b 1
call :build Traditional_Chinese Traditional_Chinese_Default
if errorlevel 1 exit /b 1
call :build Simplified_Chinese Simplified_Chinese_Default
if errorlevel 1 exit /b 1

copy /y "Language_Defaults\English\AICodingEditor_Default_Language.properties" "AICodingEditor_Default_Language.properties" >nul
echo Built all language variants in %CD%\dist\language-variants
exit /b 0

:build
copy /y "Language_Defaults\%~1\AICodingEditor_Default_Language.properties" "AICodingEditor_Default_Language.properties" >nul
jar cfm "dist\language-variants\AICodingEditor_V0.2.99-01a_%~2.jar" META-INF\MANIFEST.MF -C build\classes . AICodingEditor.java AICodingEditor_Default_Language.properties Manuals Examples
exit /b %errorlevel%
