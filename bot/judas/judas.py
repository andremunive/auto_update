import os
import subprocess
import requests

REPO_URL = "https://github.com/andremunive/auto_update/tree/master"

def get_local_version():
    try:
        from myscript import __version__
        return __version__
    except ImportError:
        return None
    
def get_remote_version():
    response = requests.get(REPO_URL + "/bot/judas/version.txt")
    if response.status_code == 200:
        return response.text.strip()
    return None

def update_script():
    response = requests.get(REPO_URL + "/bot/judas/myscript.py")
    if response.status_code == 200:
        with open("myscript.py", 'w') as f:
            f.write(response.text)
        print("Script updated successfully.")
    else:
        print("Failed to update the script.")

def main():
    local_version = get_local_version()
    remote_version = get_remote_version()
    
    if remote_version and local_version != remote_version:
        print(f"Updating script from version {local_version} to {remote_version}.")
        update_script()
        print("Restarting script...")
        subprocess.call(['python', 'myscript.py'])
        exit()
    else:
        print(f"Running the latest version: {local_version}")
        from myscript import main as run_main
        run_main()

if __name__ == "__main__":
    main()