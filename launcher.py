#!/usr/bin/env python3
from pathlib import Path
import os, sys, subprocess, platform, stat

GUIDE = """Usage: python launcher.py [install|run|test|help]

install - Full setup ( venv -> deps -> launcher )
run     - Run the application via launcher
test    - Runs full test of all backend scripts
help    - Shows this display
"""

def main():
    
    # Init class
    appLauncher = AppLauncher()
    
    # check system args
    if len(sys.argv) < 2:
        print(GUIDE)
        
    try:
        command = sys.argv[1]
    except Exception as r:
        print(r)
        command = "None"
        
    selection = ''
        
    if command == "test":
        try:
            selection = sys.argv[2]
        except Exception as r:
            print(r)

    
    match(command):
        case "install":
            print("Running installation...")
            appLauncher._installation()
        case "run":
            print("Attempting to run app...")
        case "test":
            if selection != '':
                match (selection):
                    case 'help':
                        appLauncher.available_tests()
                        return
                    case _:
                        appLauncher.test_single(selection)
                        return
            print("Testing backend scripts...")
            appLauncher.tests()
        case "help":
            print(GUIDE)
        case _:
            print(f"Unknown command: {command}")
   
class AppLauncher:
    
    def __init__(self):
        # Initiate file directories
        self.projectRoot    = Path.cwd()
        self.backendDir     = self.projectRoot / "backend"
        self.frontendDir    = self.projectRoot / "frontend"
        
        # Get OS
        self.OS             = platform.system()
        
        self.python3        = None
        
    def _setup_venv(self):
        """Creates a new virtual environment"""
        
        venvPath = self.backendDir / "venv"
        
        if venvPath.exists():
            print(f"Venv {venvPath} already exists, skipping...")
            return
    
        print(f"Creating venv at {venvPath}...")
        try:
            subprocess.run([sys.executable, '-m', 'venv', str(venvPath)])
            print("Successfuly created")
        except Exception as err:
            print(err)
            
            
    def _setup_dependencies(self):
        """Installs dependencies from requirements.txt"""
        
        if "Windows" in self.OS:
            print("OS is windows, setting up via venv/Scripts/")
            pip = self.backendDir / "venv" / "Scripts" / "pip.exe"
        else:
            print("OS is linux/mac, setting up via venv/bin/")
            pip = self.backendDir / "venv" / "bin" / "pip"
            
        if not pip.exists():
            print("Virtual environment does not exist...")
            return
        
        requirements = self.projectRoot / "requirements.txt"
        
        if not requirements.exists():
            print("[requirements.txt] does not exist...")
            return
        
        print("Installing dependencies...")
        try:
            subprocess.run([str(pip), 'install', '-r', str(requirements)])
            print("Successfuly installed")
        except Exception as err:
            print(err)
            
            
    def _windows_launcher(self):
        content = """@echo off
REM Auto-generated startup script for web ui
echo Starting App...

REM Check if venv exists
if not exist "backend\\venv\\Scripts\\python.exe" (
    echo Virtual environment not found. Running setup...
    python launcher.py install
)

REM Activate venv and run app
call backend\\venv\\Scripts\\activate
python backend\\src\\app.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Application exited with error. Press any key to close.
    pause > nul
)
"""
        # create and write file
        batch_file = self.projectRoot / "lumina.bat"
        batch_file.write_text(content)
        
        print(f"Created launcher at {batch_file}")
            
            
    def _unix_launcher(self):
        content = """#!/bin/bash
# Auto-generated startup script for web ui
echo "Starting App..."

# Check if venv exists
if [ ! -f "backend/venv/bin/python" ]; then
    echo "Virtual environment not found. Running setup..."
    python3 launcher.py install
fi

# Activate venv and run app
source backend/venv/bin/activate
python backend/src/app.py

# Keep terminal open if there's an error
if [ $? -ne 0 ]; then
    echo ""
    echo "Application exited with error. Press Enter to close."
    read
fi
"""
        # create and write sh file
        sh_file = self.projectRoot / "lumina.sh"
        sh_file.write_text(content)
        
        # make executable
        match(input("Do you want to chmod? [Y/n]").lower()):
            case "y":
                sh_file.chmod(sh_file.stat().st_mode  | stat.S_IEXEC)
                print("Added to chmod")
            case _:
                pass
            
        print(f"Created launcher at {sh_file}")
            
    def _create_launcher(self):
        """Creates the necessary bash or batch launchers"""
            
        if "Windows" in self.OS:
            self._windows_launcher()
        else:
            self._unix_launcher()
    
    def _installation(self):
        
        self._setup_venv()
        self._setup_dependencies()
        self._create_launcher()
        
        
    def test_single(self, name):
        
        self._get_python()
        
        try:
            print(f"\033[32mRunning test: {name}\033[0m")
            subprocess.run([self.python3, '-m', f"backend.tests.{name}_test"], check=True)
        except Exception as ERR:
            print(ERR)
        
        
    def tests(self):
        
        _test_folder = self.backendDir / "tests"
        
        test_files = []
        successful = 0
        failed = 0
        
        self._get_python()
        
        for file in os.listdir(_test_folder):
            if file.endswith('test.py'):
                test_files.append(_test_folder / file)
                
                print(f"\033[32mRunning test: {file}    ---------------------------\033[0m")
                try:
                    subprocess.run([self.python3, '-m', f"backend.tests.{file.split('.')[0]}"], check=True)
                    successful += 1
                    
                except Exception as ERR:
                    print(ERR)
                    failed += 1
                print(f"\033[32mFinishing subprocess    ---------------------------\033[0m\n")
                
        print("Sucessful:", successful, "\nFailed:\t  ", failed)
    
    def _get_python(self):
        
        if 'Windows' in self.OS:
            self.python3 = self.backendDir / "venv" / "Scripts" / "python3"
        else: 
            self.python3 = self.backendDir / "venv" / "bin" / "python3"

    
    def available_tests(self):
        
        _test_folder = self.backendDir / "tests"
        
        print("Available tests:")
        
        for file in os.listdir(_test_folder):
            if file.endswith('test.py'):
                print(f"\t{file.split('_')[0]} - {file}")
        
            
if __name__=="__main__":
    main()
