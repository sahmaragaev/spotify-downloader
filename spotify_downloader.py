import requests
from bs4 import BeautifulSoup
from pytube import Search, YouTube

def get_songs_and_authors_from_spotify(playlist_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(playlist_url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to load page {playlist_url}")

    soup = BeautifulSoup(response.content, 'html.parser')

    songs_and_authors = set()

    song_name_elems = soup.select(".track-name")
    author_name_elems = soup.select(".artists-albums > span")

    for song, author in zip(song_name_elems, author_name_elems):
        songs_and_authors.add((song.text.strip(), author.text.strip()))

    return songs_and_authors

def download_from_youtube(song_and_author):
    search_query = f"{song_and_author[0]} {song_and_author[1]}"
    search_results = Search(search_query)

    first_result = search_results.results[0]

    yt = YouTube(first_result.watch_url)
    ys = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    ys.download()

playlist_url = input("Enter the Spotify playlist URL: ")
try:
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
except Exception as e:
    print(f"Error: {e}")
