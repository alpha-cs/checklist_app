@echo off
cd /d D:\_Programs\checklist_app
python -m unittest discover -s tests\unittest -p "test_*.py"
pause
