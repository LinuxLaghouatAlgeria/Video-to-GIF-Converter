from flask import Flask, render_template, request, send_file, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from moviepy.editor import VideoFileClip
import os
import tempfile
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200MB max
app.config['DESKTOP_APPS'] = {
    'windows': '../releases/Windows/videotogif-setup.exe',
    'linux': '../releases/Linux/videotogif-1.0.0-Linux.deb'
}

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return jsonify({'error': 'لم يتم اختيار ملف'}), 400
    
    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'لم يتم اختيار ملف'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'نوع الملف غير مدعوم'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        clip = VideoFileClip(filepath)
        duration = clip.duration
        clip.close()
        
        return jsonify({
            'success': True,
            'filename': filename,
            'duration': duration
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/convert', methods=['POST'])
def convert_to_gif():
    data = request.json
    filename = data.get('filename')
    start_time = float(data.get('start_time', 0))
    end_time = float(data.get('end_time', 15))
    fps = int(data.get('fps', 10))
    width = int(data.get('width', 320))
    height = int(data.get('height', 240))
    
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_filename = f"output_{int(time.time())}.gif"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    
    try:
        clip = VideoFileClip(input_path)
        subclip = clip.subclip(start_time, end_time)
        subclip = subclip.resize((width, height))
        subclip.write_gif(output_path, fps=fps)
        clip.close()
        
        return jsonify({
            'success': True,
            'gif_filename': output_filename
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
        os.path.join(app.config['UPLOAD_FOLDER'], filename),
        as_attachment=True,
        download_name=filename
    )

@app.route('/download/<platform>')
def download_desktop_app(platform):
    if platform not in app.config['DESKTOP_APPS']:
        return "نسخة غير متوفرة", 404
        
    app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                           app.config['DESKTOP_APPS'][platform])
    
    if not os.path.exists(app_path):
        return "الملف غير موجود", 404
        
    filename = os.path.basename(app_path)
    return send_file(app_path, 
                    as_attachment=True,
                    download_name=filename)

@app.context_processor
def inject_developer_info():
    return {
        'developer': 'Linux Laghouat',
        'facebook': 'https://www.facebook.com/LinuxLaghouatAlgeria',
        'youtube': 'https://www.youtube.com/@linuxlaghouat',
        'blog': 'https://linuxlaghouat.blogspot.com/',
        'twitter': 'https://x.com/linuxlaghouat',
        'year': '2025'
    }

if __name__ == '__main__':
    app.run(debug=True)