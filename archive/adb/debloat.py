import subprocess
import sys

packages = []

with open(sys.argv[1],'r') as f:
    for line in f:
        app, pkg = map(str,line.replace('\n','').split(' '))
        packages.append({
            'name': app,
            'id': pkg
        })

for package in packages:
    response = subprocess.call(["adb","uninstall","--user","0",package['id'],">","2>/dev/null"])
    print(f"{package['name']} - {'Error' if response else 'Success'}")
