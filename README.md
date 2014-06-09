YoutubeToVLC
============

A Python script that generates a VLC playlist of the latest videos from your favorite Youtubers!


This script will retrieve the latest videos from your youtube subsciptions based on your parameters and open VLC Media Player with the videos in a playlist.


### Requirements
* Python 2.7
* VLC Media Player

### Running
* Install Python 2.7
* Execute the command 'python YoutubeVLC.py --user <user>' -- Replace <user> with your Youtube name.


### Flags
* --exclude-title <> Allows you to specify text that will exclude videos if found in the title
* --include-title <> Only include videos where the text contains this phrase
* --include-author <> Only include videos from this author
* --exclude-author <> Exclude videos from this author
* --user <> Specify the user to retrieve the latest subsciptions from
* --vlc-path <> Specify the path to your VLC Media Player instance. Defaults to: C:/Program Files (x86)/VideoLAN/VLC/vlc.exe
* --verbose <> Specify whether or not to print annoying VLC output.

