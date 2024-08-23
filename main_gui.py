import tkinter as tk
from tkinter import ttk
from logic import *

class MainWindow:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("视频音频转文字工具")
        self.main.geometry("600x350")
        
        self.style = ttk.Style()
        self.style.configure("LabelFrame", font=(None, 25))
        self.style.configure("TButton", font=(None, 14))
        self.style.configure("TLabel", font=(None, 14))
        self.style.configure("TCombobox", font=(None, 14))

        self.frames = {
            'input_frame': self.__create_input_frame(),
            'model_frame': self.__create_model_frame(),
            'trans_frame': self.__create_trans_frame(),
            #'func_frame': self.__create_func_frame(),
        }
        
        self.widgets = {
            #视频文件路径
            'get_video_path_label': self.__create_video_path_label(),
            "get_video_path_entry": self.__create_video_path_entry(),
            #模型选择 
            'model_select_label': self.__create_model_select_label(),
            "model_select_combobox": self.__create_model_select_combobox(),
            #转换操作
            'device_select_label': self.__create__device_select_label(),
            'device_select_combobox': self.__create_device_select_combobox(),
            'trans_button': self.__create_trans_button(),
            #附加功能（暂时未开发）
            #'translation_label': self.__translation_label(),
            #'translation_Checkbutton': self.__translation_Checkbutton(),
        }
        
        self.main.mainloop()

    #视频文件路径父框架
    def __create_input_frame(self):
        input_frame_title_label = ttk.Label(self.main, text="视频文件路径", font=(None, 14))
        input_frame = ttk.LabelFrame(self.main, padding="13", labelwidget=input_frame_title_label)
        input_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        return input_frame
    
    #视频文件路径标签
    def __create_video_path_label(self):
        video_path_label = ttk.Label(self.frames['input_frame'], text="请输入视频文件路径：")
        video_path_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        return video_path_label
    
    #视频文件路径输入框
    def __create_video_path_entry(self):
        video_path_entry = ttk.Entry(self.frames["input_frame"], width=30, font=(None, 14))
        video_path_entry.grid(row=0, column=1, padx=(0, 20), sticky="ew")
        return video_path_entry

    #模型选择父框架
    def __create_model_frame(self):
        model_frame_title_label = ttk.Label(self.main, text="模型选择", font=(None, 14))
        model_frame = ttk.LabelFrame(self.main, padding="13", labelwidget=model_frame_title_label)
        model_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="ew")
        return model_frame
    
    #模型选择标签
    def __create_model_select_label(self):
        model_select_label = ttk.Label(self.frames['model_frame'], text="选择语音转文字模型：")
        model_select_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        return model_select_label
    
    #模型选择下拉框
    def __create_model_select_combobox(self):
        model_select_combobox = ttk.Combobox(self.frames["model_frame"], values=get_model_name("./models"))
        model_select_combobox.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        return model_select_combobox
    
    #转换操作父框架
    def __create_trans_frame(self):
        trans_frame_title_label = ttk.Label(self.main, text="转换操作", font=(None, 14))
        trans_frame = ttk.LabelFrame(self.main, padding="10", labelwidget=trans_frame_title_label)
        trans_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        return trans_frame
    
    #设备选择标签
    def __create__device_select_label(self):
        device_select_label = ttk.Label(self.frames['trans_frame'], text="选择设备：")
        device_select_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        return device_select_label
    
    #设备选择下拉框
    def __create_device_select_combobox(self):
        device_select_combobox = ttk.Combobox(self.frames["trans_frame"], values=["CPU", "CUDA"], width=10)
        device_select_combobox.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        return device_select_combobox
    
    #转换按钮
    def __create_trans_button(self):
        trans_button = ttk.Button(
            self.frames['trans_frame'], 
            text="转换", 
            width=25,
            padding=3,
            command=self.__trans_button_command
        )
        trans_button.grid(row=0, column=2, padx=5, pady=10)
        return trans_button
    
    #转换按钮点击事件，开始进行转换操作
    def __trans_button_command(self):
        video_path = self.widgets["get_video_path_entry"].get()
        model_name = self.widgets["model_select_combobox"].get()
        device_name = self.widgets["device_select_combobox"].get().lower()
        video_to_text(model_file=model_name, device_model=device_name, video_path=video_path)

"""
    def __create_func_frame(self):
        func_frame = ttk.LabelFrame(self.main, text="功能选择", padding="10")
        func_frame.grid(row=0, column=1, rowspan=2)
        return func_frame
  
    def __translation_label(self):
        translation_label = ttk.Label(self.frames['func_frame'], text="是否翻译为中文")
        translation_label.grid(row=0)
        return translation_label
    
    def __translation_Checkbutton(self):
        translation_Checkbutton = ttk.Checkbutton(self.frames['func_frame'])
        translation_Checkbutton.grid(row=0, column=1)
        return translation_Checkbutton
"""


if __name__ == '__main__':
    win = MainWindow()