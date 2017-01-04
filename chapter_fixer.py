# Chapter_fixer (v1.1)
# --------------------
# Author: Thawsitt Naing
# Date: Dec 2016
# Description: A simple Python script that does search and replace. Replaces all occurences of
# the string 'Unable' in the chapter file with the correct timing (eg: '00:01:37.000').

'''
Pre-condition: The script is placed in the same folder as the chapter file to edit.
The chapter file should be in the following format: <name><ep. num>_Chapter.xml
You have to type in the episode number. For example, we are going to edit a chapter file
called 'aot1_Chapter.xml'

Post-condition: All occurences of the string 'Unable' in the chapter file will be replaced
with the correct timing supplied in the script. (eg: 00:01:30). The original (unfixed) chapter
file will be saved with the suffix '_backup.xml'
'''
import os


def main():
    """ Fixes the chapter file by replacing all instances of 'unable' with the correct timing. """

    # You need to edit the following 3 values if you are using the script for the first time.
    title = 'Yuri on ice!!'     # edit anime title
    episode_name = 'yuri'       # edit name of the video file.
    timing = '00:01:37.000'     # edit Correct Time

    print('-----------------------------------------------')
    print('Fix chapter file for: ' + title)
    print('-----------------------------------------------')

    episode_num = input("Enter episode number: ")
    file_to_open = episode_name + str(episode_num) + '_Chapter.xml'
    file_to_write = episode_name + str(episode_num) + '_Chapter_Edited.xml'

    f_in = open(file_to_open, 'r')
    f_out = open(file_to_write, 'w')

    for line in f_in:
        f_out.write(line.replace('Unable', timing))

    f_in.close()
    f_out.close()

    backup_file = episode_name + str(episode_num) + '_Chapter_backup.xml'
    os.rename(file_to_open, backup_file)
    os.rename(file_to_write, file_to_open)

    print('Done!')


if __name__ == '__main__':
    main()
