from urllib.request import urlopen
html=urlopen("https://www.truecaller.com/search/in/8888001430")
bsObj=BeautifulSoup(html.read())
print(bsObj.div)
