let currentFile = null;

document.getElementById('videoFile').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('video', file);

    try {
        document.getElementById('videoSettings').style.display = 'none';
        document.getElementById('result').style.display = 'none';
        
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            currentFile = data.filename;
            document.getElementById('videoDuration').textContent = Math.round(data.duration);
            document.getElementById('endTime').value = Math.min(15, Math.round(data.duration));
            document.getElementById('videoSettings').style.display = 'block';
        } else {
            alert('خطأ: ' + data.error);
        }
    } catch (error) {
        alert('حدث خطأ أثناء رفع الملف');
        console.error(error);
    }
});

document.getElementById('convertBtn').addEventListener('click', async () => {
    if (!currentFile) return;
    
    const settings = {
        filename: currentFile,
        start_time: document.getElementById('startTime').value,
        end_time: document.getElementById('endTime').value,
        fps: document.getElementById('fps').value,
        width: document.getElementById('width').value,
        height: document.getElementById('height').value
    };
    
    try {
        document.getElementById('progress').style.display = 'block';
        document.getElementById('convertBtn').disabled = true;
        
        const response = await fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(settings)
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('gifPreview').src = `/download/${data.gif_filename}`;
            document.getElementById('downloadBtn').href = `/download/${data.gif_filename}`;
            document.getElementById('result').style.display = 'block';
        } else {
            alert('خطأ: ' + data.error);
        }
    } catch (error) {
        alert('حدث خطأ أثناء التحويل');
        console.error(error);
    } finally {
        document.getElementById('progress').style.display = 'none';
        document.getElementById('convertBtn').disabled = false;
    }
});