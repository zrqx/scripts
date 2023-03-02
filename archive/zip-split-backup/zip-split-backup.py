import subprocess
import os

archive_number = input("Enter the Archive Number --> ")
current_timestamp = input("Enter the current date and month. [ddmmm] --> ")
operand_directory = input("Absolute path to the operand directory --> ")
backup_directory = input('Absolute path to Backup directory --> ')
splitfiles = []

def preserve_a_copy(directory):
  subprocess.call(['tree',directory,'-o',f'{backup_directory}/arc-tree-{archive_number}-{current_timestamp[2:]}.txt'])
  subprocess.call(['cp','-r',directory,f'{backup_directory}/backup-{archive_number}-{current_timestamp[2:]}-untouched'])

def create_splits():
    for file in os.listdir():
      subprocess.call(['zip','-r',f'{file}.zip',f'{file}'])
      subprocess.call(['mkdir',f'split-{file}'])
      subprocess.call(['mv',f'{file}.zip',f'split-{file}'])
      subprocess.call(['split','-n','3',f'split-{file}/{file}.zip',f'split-{file}/arc{archive_number}{file[0:3]}'])
      subprocess.call(['rm','-rf',file,f'split-{file}/{file}.zip'])

def distribute_splits(directory):
  splitfiles = os.listdir(directory)
  splitfiles.sort()
  subprocess.call(['cp',f'{operand_directory}/{directory}/{splitfiles[0]}',f'{operand_directory}/{directory}/{splitfiles[1]}',f'{operand_directory}/{directory}/{splitfiles[2]}',f'arc-{archive_number}-host-{current_timestamp[2:]}'])
  subprocess.call(['cp',f'{operand_directory}/{directory}/{splitfiles[0]}',f'{operand_directory}/{directory}/{splitfiles[1]}',f'arc-{archive_number}-drive-{current_timestamp[2:]}'])
  subprocess.call(['cp',f'{operand_directory}/{directory}/{splitfiles[1]}',f'{operand_directory}/{directory}/{splitfiles[2]}',f'arc-{archive_number}-msft-{current_timestamp[2:]}'])

def create_multiple_backups():
  subprocess.call(['mkdir',f'arc-{archive_number}-drive-{current_timestamp[2:]}',f'arc-{archive_number}-msft-{current_timestamp[2:]}',f'arc-{archive_number}-host-{current_timestamp[2:]}'])
  for directory in os.listdir():
    if directory.startswith('arc') != True:
      distribute_splits(directory)
      subprocess.call(['rm','-rf',f'{operand_directory}/{directory}'])

def main():
  os.chdir(operand_directory)
  preserve_a_copy(operand_directory)
  create_splits()
  create_multiple_backups()

main()
