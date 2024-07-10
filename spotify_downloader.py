from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pytube import Search, YouTube
import msvcrt
import time

def get_songs_and_authors_from_spotify(playlist_url):
    browser = webdriver.Chrome()
    browser.get(playlist_url)
    
    songs_and_authors = set()

    while True:
        print("Press Enter when the program reaches the end of the playlist")
        ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)

        song_name_elems = browser.find_elements(By.CSS_SELECTOR, ".Type__TypeElement-sc-goli3j-0.fZDcWX.t_yrXoUO3qGsJS4Y6iXX.standalone-ellipsis-one-line")
        author_name_elems = browser.find_elements(By.CSS_SELECTOR, ".Type__TypeElement-sc-goli3j-0.bDHxRN.rq2VQ5mb9SDAFWbBIUIn.standalone-ellipsis-one-line")

        for song, author in zip(song_name_elems, author_name_elems):
            songs_and_authors.add((song.text, author.text))

        if msvcrt.kbhit() and msvcrt.getch() == b'\r':
            break

    browser.quit()
    print(len(songs_and_authors))
    return songs_and_authors

def download_from_youtube(song_and_author):
    search_query = f"{song_and_author[0]} {song_and_author[1]}"
    search_results = Search(search_query)
    
    first_result = search_results.results[0]
    
    yt = YouTube(first_result.watch_url)
    ys = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    ys.download()

playlist_url = input("Enter the Spotify playlist URL: ")
songs_and_authors = get_songs_and_authors_from_spotify(playlist_url)

for song_and_author in songs_and_authors:
    song_name, author_name = song_and_author
    print(f"Downloading '{song_name}' by '{author_name}' from YouTube...")
    try:
        download_from_youtube(song_and_author)
    except:
        print(f"Exception occurred while downloading '{song_name}' by '{author_name}'.")
    else:
        print(f"'{song_name}' by '{author_name}' downloaded successfully!")