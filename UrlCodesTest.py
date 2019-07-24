#Getting Information From websites User codes
#import urllib.request
#webUrl = urllib.request.urlopen('https://www.youtube.com/user/guru99com')
#print("result code:" + str(webUrl.getcode()))

import urllib.request
# Open a connection to a Url using urllib
webUrl = urllib.request.urlopen('https://www.youtube.com/user/davidsandoval')
print("result code:" + str(webUrl.getcode()))

data = webUrl.read()
print(data)
