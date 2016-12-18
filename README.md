# Chapter-Fixer
A python script for fixing chapter file. (Last Updated: Dec 2016)

## Synopsis
A script that I use personally for automating tedious **search-and-replace**/**copy-and-paste** processes
in chapter files.

## Motivation
*I like to learn by doing.* Last summer (2016), I played around with Unix shell by writing a (.bat) script
that encodes ordered chapters (OC) anime videos using H264 encoder. A (.xml) chapter file is created during 
the process to keep track of the chapters in the video. It works fine for the most part, but while linking 
the opening and ending songs to the episode file, the script can't find the length of the songs and writes 
"Unable" in the chapter file instead of the correct timing.

So, I have to manually open the .xml file. Find "Unable" and manually replace it with the correct timing, 
which is usually 1min 30s. (00:01:30.000). There are a lot of episodes, and you can imagine how annoying it is
to edit the chapter file after each encode. In Dec 2016, I was back in NYC for the winter break, and I thought 
I might write a script and put it up on GitHub so that I can learn Python and how to use GitHub.

## Installation
Put fix_chapter.py in the same folder as the chapter files you want to edit.

## Usage
Make sure you have Python installed on your computer. Double click fix_chapter.py script, or open it with
Python Launcher. A terminal will pop up and ask you the episode number of the chapter file you want to edit.
Enter the number, hit enter, and the chapter file for that episode will be fixed. Tada!

## License
MIT License
Copyright (c) 2016 Thawsitt Naing
