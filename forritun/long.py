import urllib   # the lib that handles the url stuff
import re

d = urllib.request.urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')

print(max([l for l in str(d.read(), "utf-8").split("\n") if not re.search("[gkmqvwxzio]", l.lower())], key=len))