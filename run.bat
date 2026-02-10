@echo off
cd /d "%~dp0"
echo Starting Research and Blog Crew...
echo.
.venv\Scripts\python.exe -c "from research_and_blog_crew.main import run; run()"
echo.
echo Crew execution completed!
pause
