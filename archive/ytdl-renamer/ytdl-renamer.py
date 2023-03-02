import os

actual_filename = []
final_filename = []
video_title = []
video_id = []
count = 0

# store the video-title to an array
with open('title.txt','r') as f:
    for each in f:
        temp = each[:-1]
        video_title.append(temp)

# store video-ids to an array
with open('id.txt','r') as filehandle:
    for each in filehandle:
        temp = each[:-1]
        video_id.append(temp)

# cd into the target folder
os.chdir('/path/to/directory')
# store number of files to a variable
max_count = len(os.listdir())

# operations on filenames
while count < max_count:
    # emulating the actual filename and appending it to an array 
    actual_filename.append(video_title[count] + '-' + video_id[count] + '.mkv')
    # creating the final filename by cleaning the title text and replacing certain characters and appending it to an array & appending filename specific replace statements to the end. eg: .replace('-the-unwanted-text','')
    final_string = video_title[count].replace(' ','-').replace('.','-').replace(',','-').replace('|','-').replace('/','-').replace('&','-and-').replace('?','').replace("'","").replace('(','-').replace(')','-').replace('---','-').replace('--','-').lower()
    final_filename.append(str(count) + '-' + final_string + '.mkv')
    # rename the files
    os.rename(actual_filename[count],final_filename[count])
    count += 1
