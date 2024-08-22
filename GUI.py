import os
import tkinter as tk
from tkinter import ttk, filedialog
import subprocess


# 設置文件選擇
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        path_label.config(text=file_path)


# 調用whisper進行語音轉文字
def whisper():
    # 判斷是否選擇了文件
    if path_label.cget("text") == "文件路徑":
        # 彈出提示框
        tk.messagebox.showinfo(title="提示", message="請先選擇文件")
        return
    else:
        # 調用控制台激活虛擬環境whisper
        outpath = path_label.cget("text")
        # 找到文件夾路徑
        outpath = outpath[: outpath.rfind("/") + 1]
        print(outpath)
        # 獲得選擇的語言模型
        model = model_dropdown_value.get()
        # 合成命令行語句
        cmd = (
            'start cmd /k "conda activate whisper && whisper '
            + path_label.cget("text")
            + " --model "
            + model
            + " --language Japanese --task translate --output_format srt --output_dir "
            + outpath
            + ' && EXIT"'
        )
        print(cmd)
        # 執行命令行語句，結束後自動關閉
        subprocess.Popen(cmd, shell=True).wait()
        # 將字幕從英文翻譯成中文


# 添加程序入口
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Whisper字幕生成器")
    # 設置背景顏色
    root.config(bg="#F7EFE5")
    root.geometry("640x480")

    ################################語言模型選擇################################
    # 窗口的最上面空一行
    ttk.Label(root).pack(pady=10)
    # 創建行的模塊，以將模型選擇的標籤和下拉列表框放在一起
    model_row_frame = ttk.Frame(root)
    model_row_frame.pack(pady=10)
    # 創建模型標籤
    model_dropdown_label = ttk.Label(
        model_row_frame, text="選擇語言模型：", font=("微軟雅黑", 14)
    )
    model_dropdown_label.pack(side="left")
    # 創建模型選擇拉列表
    model_options = ["tiny", "base", "small", "medium", "large"]
    model_dropdown_value = tk.StringVar(value=model_options[0])
    model_dropdown = ttk.Combobox(
        model_row_frame,
        textvariable=model_dropdown_value,
        justify="center",
        values=model_options,
        width=20,
        foreground="#FD5825",
        font=("微軟雅黑", 14),
    )
    model_dropdown.pack(side="left", padx=10)
    ################################語言模型選擇################################
    # 創建行的模塊，以將語言選擇的標籤和下拉列表框放在一起
    language_row_frame = ttk.Frame(root)
    language_row_frame.pack(pady=10)
    # 創建模型標籤
    language_dropdown_label = ttk.Label(
        language_row_frame, text="選擇語音語種：", font=("微軟雅黑", 14)
    )
    language_dropdown_label.pack(side="left")
    # 創建語言選擇下拉列表
    language_options = ["日語", "英語", "中文"]
    language_dropdown_value = tk.StringVar(value=language_options[0])
    language_dropdown = ttk.Combobox(
        language_row_frame,
        textvariable=language_dropdown_value,
        justify="center",
        values=language_options,
        width=20,
        foreground="#FD5825",
        font=("微軟雅黑", 14),
    )
    language_dropdown.pack(side="left", padx=10)
    ################################語言模型選擇################################
    # 創建行的模塊，以將語言選擇的標籤和下拉列表框放在一起
    bing_or_google_row_frame = ttk.Frame(root)
    bing_or_google_row_frame.pack(pady=10)
    # 創建模型標籤
    bing_or_google_dropdown_label = ttk.Label(
        bing_or_google_row_frame, text="選擇翻譯引擎：", font=("微軟雅黑", 14)
    )
    bing_or_google_dropdown_label.pack(side="left")
    # 創建語言選擇下拉列表
    bing_or_google_options = ["必應", "谷歌翻譯（需要梯子）"]
    bing_or_google_dropdown_value = tk.StringVar(value=bing_or_google_options[0])
    bing_or_google_dropdown = ttk.Combobox(
        bing_or_google_row_frame,
        textvariable=bing_or_google_dropdown_value,
        justify="center",
        values=bing_or_google_options,
        width=20,
        foreground="#FD5825",
        font=("微軟雅黑", 14),
    )
    bing_or_google_dropdown.pack(side="left", padx=10)
    ################################視頻文件選擇################################
    # 創建文件選擇按鈕
    # 創建行的模塊，以將語言選擇的標籤和下拉列表框放在一起
    file_row_frame = ttk.Frame(root)
    file_row_frame.pack(pady=10)
    # 創建模型標籤
    filepath_label = ttk.Label(
        file_row_frame, text="選擇視頻文件：", font=("微軟雅黑", 14)
    )
    filepath_label.pack(side="left")
    filepath_button = tk.Button(
        file_row_frame,
        text="...",
        command=browse_file,
        width=10,
        bg="#3FABAF",
        fg="#F7EFE5",
        font=("微軟雅黑", 14, "bold"),
    )
    filepath_button.pack(side="left", padx=10)
    # 創建文件路徑標籤，標籤居中對齊
    path_label = ttk.Label(
        root, text="文件路徑", font=("微軟雅黑", 14), justify="center"
    )
    path_label.pack(pady=10)
    ################################Whisper語音轉字幕################################
    whisper_Trans_button = tk.Button(
        root,
        text="語音轉字幕",
        command=whisper,
        width=20,
        bg="#3FABAF",
        fg="#F7EFE5",
        font=("微軟雅黑", 14, "bold"),
    )
    whisper_Trans_button.pack(pady=10)
    ################################Whisper語音轉字幕################################
    merge_button = tk.Button(
        root,
        text="合併語音和字幕",
        width=20,
        bg="#3FABAF",
        fg="#F7EFE5",
        font=("微軟雅黑", 14, "bold"),
    )
    merge_button.pack(pady=10)
    root.mainloop()
