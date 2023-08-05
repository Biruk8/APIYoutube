from flask import Flask, render_template
import sqlalchemy as db
from ytbe import retrieve_from_database, makee_youtube_api_requests, save_video_titles_to_database, extract_video_titles

app = Flask(__name__)

@app.route('/')
def index():
    data = makee_youtube_api_requests()
    video_titles = extract_video_titles(data)
    save_video_titles_to_database(video_titles, 'data_base_name.db')


    df_video_titles = retrieve_from_database('data_base_name.db')
    video_titles2 = df_video_titles['video_title'].tolist()

    print(video_titles2)
    return render_template('index.html', video_titles=video_titles2)

if __name__ == '__main__':
    app.run(debug=True)
