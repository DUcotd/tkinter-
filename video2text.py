import tkinter as tk
from tkinter import ttk
import os
import threading
from moviepy.editor import VideoFileClip
from logic import *

class MainWindow:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("视频音频转文字工具")
        self.main.geometry("800x350")
        
        self.frames = {
            'input_frame': self.__create_input_frame(),
            'model_frame': self.__create_model_frame(),
            'trans_frame': self.__create_trans_frame(),
            #'func_frame': self.__create_func_frame(),
        }
        
        self.widgets = {
            'model_select_label': self.__create_model_select_label(),
            "model_select_combobox": self.__model_select_combobox(),
            'get_video_path_label': self.__get_video_path_label(),
            'device_select_label': self.__device_select_label(),
            'device_select_combobox': self.__device_select_combobox(),
            'trans_button': self.__trans_button(),
            #'translation_label': self.__translation_label(),
            #'translation_Checkbutton': self.__translation_Checkbutton(),
            "get_video_path_entry": self.__get_video_path_entry()
        }
        
        self.main.mainloop()


    def __create_input_frame(self):
        input_frame = ttk.LabelFrame(self.main, text="视频文件路径", padding="10")
        input_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        return input_frame
    
    def __create_model_frame(self):
        model_frame = ttk.LabelFrame(self.main, text="模型选择", padding="10")
        model_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="ew")
        return model_frame
    
    def __create_trans_frame(self):
        trans_frame = ttk.LabelFrame(self.main, text="转换操作", padding="10")
        trans_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        return trans_frame
    
    def __create_func_frame(self):
        func_frame = ttk.LabelFrame(self.main, text="功能选择", padding="10")
        func_frame.grid(row=0, column=1, rowspan=2)
        return func_frame
    
    def __create_model_select_label(self):
        model_select_label = ttk.Label(self.frames['model_frame'], text="选择语音转文字模型：")
        model_select_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        return model_select_label

    def __model_select_combobox(self):
        model_select_combobox = ttk.Combobox(self.frames["model_frame"], values=get_model_name("./models"))  # 示例模型
        model_select_combobox.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        return model_select_combobox
    
    def __get_video_path_label(self):
        get_video_path_label = ttk.Label(self.frames['input_frame'], text="请输入视频文件路径：")
        get_video_path_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        return get_video_path_label
    
    def __get_video_path_entry(self):
        get_video_path_entry = ttk.Entry(self.frames["input_frame"], width=50)
        get_video_path_entry.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        return get_video_path_entry
    def __device_select_label(self):
        device_select_label = ttk.Label(self.frames['trans_frame'], text="选择设备：")
        device_select_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        return device_select_label
    
    def __device_select_combobox(self):
        device_select_combobox = ttk.Combobox(self.frames["trans_frame"], values=["CPU", "CUDA"])
        device_select_combobox.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        return device_select_combobox
    
    def __trans_button(self):
        trans_button = ttk.Button(
            self.frames['trans_frame'], 
            text="转换", 
            command=self.__trans_button_command
        )
        trans_button.grid(row=0, column=2, padx=5, pady=10)
        return trans_button


    def __trans_button_command(self):
        model_name = self.widgets["model_select_combobox"].get()
        device_name = self.widgets["device_select_combobox"].get().lower()
        video_path = self.widgets["get_video_path_entry"].get()
        video_to_text(model_file=model_name, device_model=device_name, video_path=video_path)

    #def __translation_label(self):
        translation_label = ttk.Label(self.frames['func_frame'], text="是否翻译为中文")
        translation_label.grid(row=0)
        return translation_label
    
    #def __translation_Checkbutton(self):
        translation_Checkbutton = ttk.Checkbutton(self.frames['func_frame'])
        translation_Checkbutton.grid(row=0, column=1)
        return translation_Checkbutton

if __name__ == "__main__":
    win = MainWindow()
    