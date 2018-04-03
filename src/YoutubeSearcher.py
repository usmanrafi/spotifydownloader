import bs4
import urllib.request as req

import YoutubeDownloader as ytdl

def dl(link, name, output="mp4"):
	ytdl.download(["https://www.youtube.com/watch?v=Ce8p0VcTbuA", "Chopin.%(ext)s" , "mp3"])


def main(name):

	url = "https://www.youtube.com/results?search_query="
	name = name.split(' ')
	for word in name:
		url += word + "+"
	url = url[:-1]	# removing the last +

	src = req.urlopen(url)
	soup = bs4.BeautifulSoup(src, 'lxml')

	vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
		
	print ('https://www.youtube.com' + vid['href'])
	

main("Mad World")