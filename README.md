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

### Common Issues
* 'Must specify a Youtube username to get the videos for!' - Make sure to specify your Youtube username with --user <user> when running the program.
* 'No videos were found for the specified user and parameters.' - It's possible that you specified too many parameters to the point that no videos were found.
* 'Failed to retrieve data for the user {}. Make sure their subscriptions are public.' - If you are using a different user than yourself, this user's subscriptions may not be public. If you are using your own user, you can make your Youtube subscriptions public by using [this tutorial](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=5&cad=rja&uact=8&sqi=2&ved=0CEkQFjAE&url=http%3A%2F%2Fwww.twelveskip.com%2Ftutorials%2Fyoutube%2F1020%2Fmaking-subscription-private-on-youtube&ei=nBaVU8uuPJKWyASP0ICwCA&usg=AFQjCNEHtCx5ToAfkjH1ePQt18GtI0nlzg&sig2=pzm21nw4IPUqvyp_xbNSjg)

