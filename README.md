# 🎵 Billboard Top 100 to Spotify Playlist 🎶

This project is all about blending web scraping with the power of Spotify! Ever wondered what the top songs were on a specific day in history? With this tool, you can scrape the Billboard Hot 100 chart for any given date and instantly create a private Spotify playlist filled with those hits! 🚀

## 💡 Features

- **🗓️ Time Travel Through Music:** Input any date in `YYYY-MM-DD` format, and the tool fetches the top 100 songs from the Billboard Hot 100 chart on that day.
- **🖥️ Web Scraping Magic:** Leverages the power of BeautifulSoup to extract song titles directly from the Billboard website.
- **🎶 Spotify Integration:** Using the `spotipy` library, it creates a personal Spotify playlist and adds all the songs automatically!
- **🛠️ Custom Playlist:** The playlist is private by default, but you can easily tweak it to fit your needs.

## 🚀 How It Works

1. **Choose a Date:** The program prompts you to input a specific date (in `YYYY-MM-DD` format) for which you want to fetch the [top 100 Billboard songs](https://www.billboard.com/charts/hot-100/).
2. **Scrape the Songs:** The script uses [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to grab the song titles from the Billboard website for the specified date.
3. **Create Spotify Playlist:** It authenticates with Spotify (using the Spotify Web API) and creates a private playlist.
4. **Add Songs to Playlist:** The program searches for each track on Spotify and automatically adds them to your freshly created playlist! 🎧

## 🧰 Requirements

- **[Python 3.x](https://www.python.org/downloads/)**
- **[Spotify Account](https://developer.spotify.com/)** with developer [credentials](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow) (Client ID and Client Secret).
- **Spotify API Access** via the [spotipy](https://spotipy.readthedocs.io/en/2.24.0/) library.
- **[Billboard](https://www.billboard.com/charts/hot-100/) Website Access** for scraping the top  Hot 100 songs.

## 📦 Installation

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/ImanGholamii/Spotify_api_python_web_scraping_billboard.com.git
   ```

2. **Install Dependencies**:  
   In the project directory, run:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:  
   Create a `.env` file and include your Spotify credentials:  
   ```bash
   CLIENT_ID='your_spotify_client_id'
   CLIENT_SECRET='your_spotify_client_secret'
   ```

## 🎮 Usage

1. **Run the Script**:  
   In your terminal, navigate to the project directory and run:  
   ```bash
   python main.py
   ```

2. **Input a Date**:  
   When prompted, enter a date in `YYYY-MM-DD` format (e.g., `2020-05-15`) to retrieve the Billboard Hot 100 for that day.

3. **Enjoy Your Playlist**:  
   The script will create a playlist on your Spotify account titled "PyPlaylist," filled with all the songs from the Billboard Top 100 on that specific day!
   `You can change the title simply.`

## 🛠️ Project Structure

```bash
billboard-to-spotify-playlist/
│
├── main.py                        # Main Python script for the project 📝
├── requirements.txt               # Required Python packages 📦
├── README.md                      # Project documentation 📄
└── .env                           # Your secret environment variables 🔑
```

## 📝 Notes

- The Billboard website uses pagination and has a lot of redundant HTML elements, but the [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) library helps navigate through this to extract the song titles accurately.
- Spotify API might not find all the songs, depending on the availability of tracks, so some songs might not be added to the playlist.
- The playlist is private by default, but you can change this behavior by adjusting the Spotify API settings in the code.

## 🙌 Acknowledgements

Special thanks to the developers of Python, Spotipy, bs4 and Dr Angela Yu, and inspiration from password management best practices.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to enhance the project. Contributions are always welcome! 🛠️

## 📜 License

This project is licensed under the **[MIT License](https://github.com/ImanGholamii/Spotify_api_python_web_scraping_billboard.com/blob/main/LICENSE)** ⚖️.

## ⭐️ Support

If you like this project, please give it a ⭐️ on [GitHub!](https://github.com/ImanGholamii/Spotify_api_python_web_scraping_billboard.com)

---

🎶 **Time to relive the hits of the past!** Create your own custom playlist based on the top 100 songs of any day in history with just a few clicks!
