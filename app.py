from flask import Flask, render_template, request, send_file
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    
    buffer = BytesIO()
    stream.stream_to_buffer(buffer)
    buffer.seek(0)
    
    return send_file(
        buffer,
        as_attachment=True,
        download_name='video.mp4',
        mimetype='video/mp4'
    )

if __name__ == '__main__':
    app.run(debug=True)
