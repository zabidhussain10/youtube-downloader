from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = yt.title.replace(" ", "_") + ".mp4"
        stream.download(output_path="static/downloads", filename=filename)
        download_url = url_for('static', filename=f"downloads/{filename}")
        return render_template('index.html', success=True, download_url=download_url, title=yt.title)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    os.makedirs("static/downloads", exist_ok=True)
    app.run(host='0.0.0.0', port=10000)
