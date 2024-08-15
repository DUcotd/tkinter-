from moviepy.editor import VideoFileClip
from audio2text import trans_audio
import threading
import os
def safe_extract_audio(video_file, audio_file):
    try:
        clip = VideoFileClip(video_file)
        audio = clip.audio
        audio.write_audiofile(audio_file)
        audio.close()
        clip.close()
    except Exception as e:
        print(f"Error extracting audio: {e}")

def get_video_path(get_video_path_entry):
    string = get_video_path_entry.get().strip()
    if string[0] == '"' and string[-1] == '"':
        string = string[1:-1]
    if not string:
        raise ValueError("Video path is empty.")
    print(string)
    return string

def add_audio_extension(video_file):
    audio_file = video_file[:-4]
    return f"{audio_file}.wav"

def video_to_text(model_select_combobox, device_select_combobox):
    try:
        model_file = model_select_combobox.get()
        video_path = get_video_path()
        audio_path = add_audio_extension(video_path)
        device_model = device_select_combobox.get().lower()
        if not os.path.exists(audio_path):
            thread0 = threading.Thread(target=safe_extract_audio, args=(video_path, audio_path))
            thread0.start()
        thread1 = threading.Thread(target=trans_audio, args=(audio_path, model_file, device_model))
        thread1.start()
    except Exception as e:
        print(f"Error processing audio: {e}")

#模型选择
def get_model_name(model_path):
    for root, dirs, files in os.walk(model_path):
        # 返回顶层子文件夹
        return dirs