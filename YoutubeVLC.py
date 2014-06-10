import json
import urllib
import subprocess
import os
from optparse import OptionParser
from time import sleep

base_url = 'https://gdata.youtube.com/feeds/api/users/{}/newsubscriptionvideos?v=2&alt=json'

parser = OptionParser()
parser.add_option('-u', '--user', dest='user', help='Specify the user to search recent videos for.',
                  default=None)
parser.add_option("--vlc", "--set-vlc", dest="vlc_path",
                  help="Specify the VLC media player path.", default="\"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe\"")
parser.add_option("-v", "--v", "--verbose", dest="verbose", default=False,
                  help="Whether or not to print VLC output")
parser.add_option("--xt", '--exclude-title', dest='exclude_title', default=None,
                  help='Specifies text that should be excluding when searching for videos.')
parser.add_option('--it', '--include-title', dest='include_title', default=None,
                  help='Specifies text that will be included in titles of any found videos.')
parser.add_option("--xa", '--exclude-author', dest='exclude_author', default=None,
                  help='Specifies an author that should be excluding when searching for videos.')
parser.add_option('--ia', '--include-author', dest='include_author', default=None,
                  help='Specifies the only author to be searched for')
(options, args) = parser.parse_args()

exclude = options.exclude_title.split(',') if options.exclude_title is not None else None
include = options.include_title.split(',') if options.include_title is not None else None
include_author = options.include_author.split(',') if options.include_author is not None else None
exclude_author = options.exclude_author.split(',') if options.exclude_author is not None else None
username = options.user

if username is None:
    print "Must specify a Youtube username to get the videos for!"
    exit()

sleep(1)


def get_vids_string(user):
    data = urllib.urlopen(base_url.format(user))
    json_data = json.loads(data.read())
    return json_data


def get_entries(user):
    return get_vids_string(user)['feed']['entry']


def get_links(user):
    links = []
    for entry in get_entries(user):
        author = entry['author'][0]['name']['$t']
        link = entry['link'][0]['href']
        title = entry['title']['$t']
        if exclude is not None and check_list(exclude, title):
            continue
        if exclude_author is not None and check_list(exclude_author, author):
            continue
        if include is not None and not check_list(include, title):
            continue
        if include_author is not None and not check_list(include_author, author):
            continue
        print u"Found video for {} at the URL {} with the title {}".format(author, link, title)
        links.append(link)
    return links


def check_list(search, string):
    for item in search:
        if item.lower() in string.lower():
            return True
        if item.lower() == string.lower():
            return True
    return False


path = options.vlc_path
verbose = options.verbose

video_links = get_links(username)

if len(video_links) == 0:
    print u'No videos were found for the specified user and parameters.'
    exit()

cmd_line = ''
try:
    cmd_line = ' '.join(video_links)
except ValueError:
    print('Failed to retrieve data for the user {}. Make sure their subscriptions are public.'.format(username))
    exit()

if not verbose:
    FNULL = open(os.devnull, 'w')
    subprocess.call(path + cmd_line, stdout=FNULL, stderr=subprocess.STDOUT)
else:
    subprocess.call(path + cmd_line)
