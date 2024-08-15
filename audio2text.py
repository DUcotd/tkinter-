import os
import torch
from transformers import pipeline
def trans_audio(audio_file, model_file, device_select):
    try:

        pipe = pipeline("automatic-speech-recognition", model=f"models\{model_file}", device=device_select)
        
        # 直接使用音频路径
        text = pipe(audio_file)
        
        # 构造输出文件路径
        outputfile = os.path.join(audio_file[:-4] + ".txt")
        
        # 写入文件
        with open(outputfile, "w") as file:
            file.write(str(text["text"]))
            
    except Exception as e:
        print(f"An error occurred: {e}")
