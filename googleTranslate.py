from urllib import parse
import requests
import re
import html
import translators as ts
import sys

GOOGLE_TRANSLATE_URL = "http://translate.google.com/m?q=%s&tl=%s&sl=%s"


def translate(text, to_language="auto", text_language="auto"):
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text, to_language, text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if len(result) == 0:
        return ""
    return html.unescape(result[0])


# 添加程序入口
if __name__ == "__main__":
    if len(sys.argv) > 2:
        file_path = sys.argv[1]
        bing_or_google = sys.argv[2]
        # 获取文件名称
        transfile_path = file_path[: file_path.rfind(".")] + "-ch.srt"
        # 打开并逐行读取文件
        with open(transfile_path, "w", encoding="utf-8") as wf:
            with open(file_path, "r", encoding="utf-8") as f:
                # 按行读取文件
                lines = f.readlines()
                for line in lines:
                    # 如果非空且不是以数字开头
                    if line[0].isascii() and not line[0].isdigit() and line[0] != "\n":
                        # print(line)
                        if bing_or_google == "google":
                            line = translate(line, "zh-TW", "en")  # 汉语转英语
                        else:
                            line = ts.translate_text(
                                line, str="bing", from_language="en", to_language="zh"
                            )
                        line = line + "\n"
                    print(line)
                    wf.write(line)

    else:
        print("请提供文件路径和翻译引擎选择参数")
