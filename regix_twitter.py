# lets create program where we want to extract the twitter username of an account from the given url 
url = input("URl: ").strip()
# now we know that the format of a url is https://twitter.com/yasirkhan so what we need to do is get rid of all the parts of url just before the username and the simple method to that will be :
# username = url.replace("https://twitter.com/","")
# print(f"username: {username}")
# this program might work in some cases but there are a dozan of cases where it doesn't work and is very fragile so instead we are going to use re package

import re

# username = re.search(r"(http(s)?\://)?twitter\.com/(\w+)", url) my own code and thinking
# print(username.group(3))
# # print(f"username: {username}")
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)#syntax of re.sub is re.sub(pattern,replicate,statement to be changed)
print(f"Username: {username}")