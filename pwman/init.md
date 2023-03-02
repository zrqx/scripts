# Pwman | Password Manager Utility
23 Aug 2022

## I/O

> -s Service Name -i Identifier (Optional if Link is provided) -p Password -e Encrpytion -l Link to Service

```bash
# Example 1:
input: pwman -s google -i firstmail@gmail.com -p google1 -e almond
output: 32g8dje3

input: pwman -s instagram
output: Found 2 Instagram/ {service} account/s
1. email: sjs@y.com pass: 3hr2db372d
2. email: diw@ds.com pass: 932basg2

input: pwman -s devfolio -p iwritecode -l google,phone -i zrqx -e mango
output: Link to Service - Found 5 Google accounts. Choose one from the options
1.deo@gmail.com 2.dihk@gmail.com
>> 2
output: hfh322g7

input: pwman -s phone -i 9353731466
output: Added {arg} to {service} 

## Commands
- empty with args
- addenc - Add a type of encryption. Opens the config file, where a function need to be added.
```
import libraries
salt = 'c38u3duhe82e92wejiwqy902e3274'

enc = {
  'enc_name': 'Description goes here'
}

def enc_name(string):
  string.concat(salt)
  string.replace('A',4)
  hash(string)
  decorate(add @A1)
  maxlength(20)  
  return pass
  
```
- listenc - lists encryption methods with their descriptions


## Algorithm
1. Accept command line arguments and check whether it is a GET request or POST request based on args count. argc?
2. If args count is 2, it is GET. Else it maybe is a POST or an invalid request.
3. If GET, lookup the arg in the db/file and encrypt the password, return it.
