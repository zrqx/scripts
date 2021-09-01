import subprocess

packages = []
count = 0

with open('package_list.txt', 'r') as filehandle:
    for line in filehandle:
        package_name = line[:-1]
        packages.append(package_name)

while count < len(packages):
    print("[*] Uninstalling " + packages[count])
    subprocess.call(["adb","uninstall","--user","0", packages[count]])
    count += 1
