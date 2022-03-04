Website-blocker-python

This repo consist of a code of a simple website blocker project implemented in Python, It can be used to block certain websites during working time to reduce distraction thus improving productivity

The magic of this project lies on modifying the host file withing your computer that manages how you access the web.

Websites.txt

The Websites to be blocked are stored in a file "Websites.txt".The websites names are written in the file separated by comma.
For eg: www.facebook.com, www.instagram.com

Time.txt

The duration during which websites are to be blocked are stored in "Time.txt".
The starting time and ending time are provided in separated lines respectively.
The format  of the time is : Hour:Minute:Second
For eg: 9:30:15

Host File Location

Windows Host : "C:\Windows\System32\drivers\etc\hosts"
Linux Host : "/etc/hosts"
