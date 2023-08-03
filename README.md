
# YouTube Most Popular Video Titles Scraper

This is a Python script that makes API requests to the YouTube API, retrieves the most popular video titles, and saves them to a SQLite database. This application is a simple example of how to interact with web APIs and databases using Python.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.x)
- pip (Python package manager)

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory using the terminal or command prompt.
3. Install the required dependencies by running:

```bash
pip install requests pandas sqlalchemy
```

## Configuration

To use the YouTube API, you will need an API key. Follow these steps to obtain an API key:

1. Go to the Google Developers Console: https://console.developers.google.com/
2. Create a new project or select an existing one.
3. In the sidebar, navigate to "APIs & Services" > "Library".
4. Search for "YouTube Data API v3" and enable it for your project.
5. In the sidebar, navigate to "APIs & Services" > "Credentials".
6. Click on "Create credentials" and select "API key".
7. Copy the API key and set it as an environment variable with the name "YOUTUBE_API_KEY".

## Usage

1. Open the terminal or command prompt.
2. Navigate to the project directory.
3. Run the Python script by executing:

```bash
python youtube_scraper.py
```

The script will make API requests to the YouTube API, retrieve the most popular video titles, and save them to a SQLite database named "data_base_name.db".

## Retrieving Video Titles from the Database

If you want to retrieve the video titles from the database, you can use the following command:

```bash
python youtube_scraper.py retrieve
```

The script will connect to the database and display the retrieved video titles in the terminal.

## Note

- This application is intended for learning purposes and may require additional error handling and optimizations for production use.
- Make sure to keep your API key secure and do not share it publicly.
- For large-scale applications, consider using appropriate rate limiting and caching strategies to avoid API rate limits and improve performance.

## Contributors

This project was developed by Biruk8.

Feel free to contribute or provide feedback to improve this YouTube Most Popular Video Titles Scraper.

**Enjoy coding!**
