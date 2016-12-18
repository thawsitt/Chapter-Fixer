# Python Script
# Author: Thawsitt Naing 
# Date: Dec 2016
# Description: A simple Python script that does search and replace. Replaces the string 'Unable'
# with the correct timing (eg: '00:01:37.000') that needs to be manually edited. 

import os

# You need to edit the following 3 values. 

title = 'Yuri on ice!!'     # edit anime title
episode_name = 'yuri'       # edit Name.
timing = '00:01:37.000'     # edit Correct Time
  
print('-----------------------------')
print(title + ' Chapter Editor')
print('-----------------------------')

episode_num = input("Enter episode number: ")
file_to_open = episode_name + str(episode_num) + '_Chapter.xml'
file_to_write = episode_name + str(episode_num) + '_Chapter_Edited.xml'

f_in = open(file_to_open, 'r')
f_out = open(file_to_write, 'w')

for line in f_in:
    f_out.write(line.replace('Unable', timing))

f_in.close()
f_out.close()

os.remove(file_to_open)
os.rename(file_to_write, file_to_open)

print('Done!')