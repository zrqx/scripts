import os
import sys
import time
import datetime
import requests
import subprocess

def connection_established():
    try:
        response = requests.get('https://google.com')
        return True
    except:
        return False

def read_config(path):
    directories = []
    with open(path,'r') as f:
        for line in f:
            directories.append(line.replace('\n',''))
    return directories

def changes_exist(path):
    try:
        os.chdir(path)
        git_status_process = subprocess.Popen(['git','status'], stdout=subprocess.PIPE)
        wc_process = subprocess.Popen(['wc','-l'], stdin=git_status_process.stdout, stdout=subprocess.PIPE)
        wc_process.wait()
        response_length = wc_process.stdout.read().decode('utf-8')
    except:
        print('Error while Checking for Changes')
        pass
    else:
        git_status_process.stdout.close()
        wc_process.stdout.close()

        if (int(response_length) > 4):
            print("Changes Exist")
            return True
        else:
            print("No Changes")
            return False
    
def perform_operations(path):
    os.chdir(path)
    now = datetime.datetime.now()
    commit_message = f"Updated on {now.strftime('%d %B %Y')} at {now.strftime('%I:%M %p')}"
    try:
        subprocess.call(['git','add','.'])
        subprocess.call(['git','commit','-m',commit_message])
        subprocess.call(['git','push'])
    except:
        pass
    else:
        print('Git Push Success')

def main():
    if connection_established():
        print('Connection Established')
        directories = read_config(sys.argv[1])
        for directory in directories:
            if changes_exist(directory):
                perform_operations(directory)

if connection_established():
    main()
else:
    print('No Connection Established')
    time.sleep(300)
    main()
