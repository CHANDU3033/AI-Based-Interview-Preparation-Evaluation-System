@echo off
echo Pushing changes to both GitHub accounts (main and gh-pages)...
cd /d %~dp0
echo.
echo [1/4] Pushing main to origin (kaswitha100)...
git push origin main
echo.
echo [2/4] Pushing gh-pages to origin (kaswitha100)...
git push origin main:gh-pages --force
echo.
echo [3/4] Pushing main to chandu_origin (CHANDU3033)...
git push chandu_origin main --force
echo.
echo [4/4] Pushing gh-pages to chandu_origin (CHANDU3033)...
git push chandu_origin main:gh-pages --force
echo.
echo Done! All branches (main and gh-pages) updated on both GitHub accounts.
pause
