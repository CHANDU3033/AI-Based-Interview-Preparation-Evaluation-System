@echo off
echo Pushing changes to both GitHub accounts...
cd /d %~dp0
echo.
echo [1/2] Pushing to origin (kaswitha100)...
git push origin main
echo.
echo [2/2] Pushing to chandu_origin (CHANDU3033)...
git push chandu_origin main
echo.
echo Done! Both GitHub repositories are updated.
pause
