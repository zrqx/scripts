import subprocess
import click
@click.command()

@click.option('list', type=click.Path(exists=True))

def sampleFunction(list):
    with open(list, 'r') as filehandle:
        for line in filehandle:
            print(line)
            # package_name = line[:-1]
            # packages.append(package_name)

def main():
    sampleFunction(list)

main()
# with open('package_list.txt', 'r') as filehandle:
#     for line in filehandle:
#         package_name = line[:-1]
#         packages.append(package_name)

# while count < len(packages):
#     print("[*] Uninstalling " + packages[count])
#     subprocess.call(["adb","uninstall","--user","0", packages[count]])
#     count += 1
