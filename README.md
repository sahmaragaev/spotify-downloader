# Spotify Playlist Song Downloader (No Selenium Version)

This project scrapes songs and their authors from a Spotify playlist without using Selenium. It uses `beautifulsoup4` for scraping the playlist and `pytube` to search and download the songs from YouTube.

## Features

- Scrape song names and author names from a Spotify playlist without browser automation.
- Search for the song on YouTube using the song and author names.
- Download the highest quality available version of the song from YouTube.

## Requirements

### Python Libraries:
- `beautifulsoup4`: For HTML parsing and scraping.
- `requests`: For sending HTTP requests to the Spotify playlist URL.
- `pytube`: For searching and downloading YouTube videos.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
