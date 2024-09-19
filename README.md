# Spotify Playlist Song Downloader and YouTube Downloader

This project automates the process of extracting songs and their authors from a Spotify playlist and then downloading those songs from YouTube as MP4 files. The project uses Selenium to scrape the Spotify playlist and Pytube to search and download the songs from YouTube.

## Features

- Scrape song names and author names from a Spotify playlist.
- Automate scrolling through the playlist until all songs are captured.
- Search for the song on YouTube using the song and author names.
- Download the highest quality available version of the song from YouTube.

## Requirements

### Python Libraries:
- `selenium`: For browser automation.
- `pytube`: For searching and downloading YouTube videos.
- `msvcrt`: For listening for user input to stop the scrolling.
- `time`: For adding delays during scrolling.

### Web Driver:
- **Google Chrome Driver**: Ensure that you have installed the ChromeDriver and it's accessible through your system's PATH. [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
