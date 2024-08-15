import tkinter as tk
from tkinter import ttk
import os
import threading
from moviepy.editor import VideoFileClip
from audio2text import trans_audio

def safe_extract_audio(video_file, audio_file):
    try:
        clip = VideoFileClip(video_file)
        audio = clip.audio
        audio.write_audiofile(audio_file)
        audio.close()
        clip.close()
    except Exception as e:
        print(f"Error extracting audio: {e}")


def get_video_path():
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


def video_to_text():
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


# 创建主窗口
main = tk.Tk()
main.title("视频音频转文字工具")
main.geometry("600x350")  # 增加高度以容纳更多组件

# 设置样式
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12))
style.configure('TCombobox', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10)
style.configure('TLabelFrame', font=('Helvetica', 12, 'bold'), padding=10)

# 创建框架
input_frame = ttk.LabelFrame(main, text="视频文件路径", padding="10")
input_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

model_frame = ttk.LabelFrame(main, text="模型选择", padding="10")
model_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="ew")

trans_frame = ttk.LabelFrame(main, text="转换操作", padding="10")
trans_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

# 模型选择框
model_select_label = ttk.Label(model_frame, text="选择语音转文字模型：")
model_select_label.grid(row=0, column=0, padx=(0, 10), sticky="w")

model_select_combobox = ttk.Combobox(model_frame, values=get_model_name("./models"))  # 示例模型
model_select_combobox.grid(row=0, column=1, padx=(0, 10), sticky="ew")

# 标签
get_video_path_label = ttk.Label(input_frame, text="请输入视频文件路径：")
get_video_path_label.grid(row=0, column=0, padx=(0, 10), sticky="w")

# 输入框
get_video_path_entry = ttk.Entry(input_frame, width=50)
get_video_path_entry.grid(row=0, column=1, padx=(0, 10), sticky="ew")

# 设备选择框和标签
device_select_label = ttk.Label(trans_frame, text="选择设备：")
device_select_label.grid(row=0, column=0, padx=(0, 10), sticky="w")

device_select_combobox = ttk.Combobox(trans_frame, values=["CPU", "CUDA"])
device_select_combobox.grid(row=0, column=1, padx=(0, 10), sticky="ew")

# 按钮
trans_button = ttk.Button(trans_frame, text="转换", command=video_to_text)
trans_button.grid(row=0, column=2, padx=5, pady=10)

# 确保输入框和下拉框填充
input_frame.columnconfigure(1, weight=1)
model_frame.columnconfigure(1, weight=1)
trans_frame.columnconfigure(1, weight=1)

# 运行主循环
main.mainloop()