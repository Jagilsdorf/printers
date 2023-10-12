@echo off
net session >nul 2>&1
if %errorlevel% == 0 (
    echo Running as administrator.
) else (
    echo Running as standard user.
)
pause
