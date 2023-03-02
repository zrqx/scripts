import os
import subprocess

file_array0 = []
file_array1 = []
bin0 = []
bin1 =[]
count = 0

path_zero = input('enter the absolute path to first directory >  ')
path_one = input('enter the absolute path to second directory >  ')
print('')
# copying the contents of first folder to an array
os.chdir(path_zero)
print(os.getcwd())
file_array0 = os.listdir()
print(file_array0)
# copying the contents of second folder to another array
os.chdir(path_one)
print(os.getcwd())
file_array1 = os.listdir()
print(file_array1)
# comparing every element of first folder with every other element of second folder
for one in file_array0:
    for another in file_array1:
        if one == another:
            # if a file exists in both the folders, both bin arrays will be appended with its name
            bin0.append(one)
            bin1.append(another)
            break
# the files present in bin0 and bin1 arrays are removed from file_array0 and file_array1 respectively
for each in bin0:
    file_array0.remove(each)
for each in bin1:
    file_array1.remove(each)
# the remaining files present in file_array0 and file_array1 are moved to second folder and first folder respectively
for each in file_array0:
    source_file = path_zero + '/' + each
    print('[+] Copying ' + each + ' to ' + path_one)
    subprocess.call(['cp',source_file,path_one])
    count += 1
for each in file_array1:
    source_file = path_one + '/' + each
    print('[+] Copying ' + each + ' to ' + path_zero)
    subprocess.call(['cp',source_file,path_zero])
    count += 1
# verbose to summarise the operation
print('')
if count == 0:
    print('[*] files are in sync already !')
elif count == 1:
    print('[*] one file is copied across the folders')
else:
    print('[*] total of ' + str(count) + ' files are copied across the folders')


