
# YouTube Popular Video Titles Viewer

This is a simple web application that retrieves and displays the most popular YouTube video titles using the YouTube Data API. The project is implemented with Python and Flask framework, allowing users to view a list of the top videos' titles.

![Screen Shot 2023-08-04 at 9 51 13 PM](https://github.com/Biruk8/APIYoutube/assets/140538603/538dd95c-9a83-44e5-a67d-46f9fe7d049d)

## Features

- Fetches data from the YouTube Data API to get the most popular video titles.
- Stores the video titles in a local SQLite database for quick retrieval.
- Provides a button to toggle the display of the video titles, offering a user-friendly interface.

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries using `pip`:

   ```bash
   pip install Flask pandas sqlalchemy requests
   ```

3. Set up your YouTube API key:
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project and enable the YouTube Data API v3.
   - Create an API key for the project.
   - Set the API key as an environment variable on your machine:

     **On Linux/MacOS**:

     ```bash
     export YOUTUBE_API_KEY=your_youtube_api_key_here
     ```

     **On Windows**:

     ```bash
     set YOUTUBE_API_KEY=your_youtube_api_key_here
     ```

## Usage

1. Ensure you have set up your YouTube API key as described in the Installation section.
2. Open a terminal and navigate to the project directory.
3. Run the Flask application using:

   ```bash
   python app.py
   ```

4. Access the application in your web browser by going to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
5. Click the "Display popular videos on YouTube now" button to see the most popular video titles.
ouTube API is subject to its usage policies, so make sure to review and comply with YouTube's API terms of service.

---
