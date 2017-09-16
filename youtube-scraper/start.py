from bs4 import BeautifulSoup
from requests import get
from pytube import YouTube, exceptions
import os
from random import randint

# youtube homepage link
youtube_link = "http://www.youtube.com"

# Place for future links. Set used to prevent duplication.
links_video = set()
links_channel = set()
links_playlist = set()
links_user = set()


def create_link(query):
    """Combine youtube link with given query"""

    query = query.replace(" ","+")
    yt_link = "https://www.youtube.com/results?search_query=" + query

    return yt_link


def get_html(url):
    """go to youtube.com search page and grab html code"""

    r = get(url)

    return r.text


def links_channel_get(channel):
    """grab all links from all found channels"""
    print("grab link from channel")

    found_links = set()

    return found_links


def links_playlist_get(playlist):
    """grab all links from playlist"""
    print("grab link from playlist")

    # list of found links on playlist
    found_links = set()

    # go through all links from links_playlist
    for link in playlist:

        link_get = get_html(link)

        soup = BeautifulSoup(link_get, 'lxml')

        for lnk in soup.find_all("a"):
            lnk = lnk.get("href")
            if "/watch?v=" in lnk:
                found_links.add(youtube_link + lnk)

    return found_links


def links_user_get(user):
    """grab all links from user page"""
    print("grab link from user")

    found_links = set()

    return found_links

def used_links(_link_):
    """store used links and don't download them again"""

    with open("links.txt", "r") as file_opened:
        old_links = file_opened.readlines()

    os.remove("links.txt")

    with open("links.txt", "a") as f:

        f.write(_link_ + "\n")

        for old_link in old_links:
            f.write(old_link)


def youtube_links_info(linklist):

    with open('links.txt', 'r') as f:
        old_links = f.readlines()

    print(" ")
    for link in linklist:
        if link not in old_links:
            try:
                link_info = YouTube(link)

                #check if the video is still available for downloading ex. blocked videos for copyright issues



                codec, resolution, quality = str(link_info.filter("mp4")[-1]).split("-")

                video = link_info.get(codec[-5:-2], resolution.strip())

                link_info.set_filename(str(randint(0,10000)) + "_" + str(link_info.filename))
                print("Downloading:", link_info.title)

                if not os.path.exists(os.getcwd() + '/videos/'):
                    os.makedirs('videos')

                video.download(os.path.join(os.getcwd()) + '/videos/')

                used_links(link)


            except exceptions.PytubeError:
                print("Wrong link")
                continue
            except exceptions.AgeRestricted:
                print("Wrong link - need to be logged in to download!")
                continue

def main():

    while True:
        # asks user for query
        query = input("What are you looking for? ")
        if all(item.isalpha() or item.isspace() for item in query):
            break

    # grab youtube search results
    page_html = get_html(create_link(query))

    soup = BeautifulSoup(page_html, "lxml")

    for link in soup.find_all("a"):
        if link:
            link = link.get("href")
            if "/watch?v=" in link:
                links_video.add(youtube_link + link)
            elif "/channel/" in link:
                links_channel.add(youtube_link + link)
            elif "/playlist?" in link:
                links_playlist.add(youtube_link + link)
            elif "/user/" in link:
                links_user.add(youtube_link + link)

    print(" ")
    print("Videos: ",len(links_video))
    print("Channels: ",len(links_channel))
    print("Playlists: ",len(links_playlist))
    print("Users: ",len(links_user))
    print(" ")

    # checks if links found and grabs more links
    if len(links_channel) > 0:
        links_channel.update(links_channel_get(links_channel))
    if len(links_playlist) > 0:
        links_video.update(links_playlist_get(links_playlist))
    if len(links_user) > 0:
        links_user.update(links_user_get(links_user))

    youtube_links_info(links_video)


if __name__ == '__main__':
    main()

