import translators as ts
import argparse


def parse_arguments():
    """解析命令行參數"""
    argparser = argparse.ArgumentParser(description="翻譯字幕文件")
    argparser.add_argument(
        "-s",
        "--source_language",
        type=str,
        help="The source language to be translated",
        default="en",
    )
    argparser.add_argument(
        "-t",
        "--to_language",
        type=str,
        help="The target language to be translated",
        default="zh-Hant",
    )
    argparser.add_argument(
        "-e",
        "--engine",
        type=str,
        help="The translation engine to be used",
        default="bing",
    )
    argparser.add_argument(
        "-f",
        "--file_path",
        type=str,
        help="The path to the subtitle file to be translated",
        required=True,
    )
    argparser.add_argument(
        "-o",
        "--output",
        type=str,
        help="The path to save the translated subtitle file",
        required=True,
    )
    return argparser.parse_args()


def translate(line, source_language, to_language, engine):
    translatedLine = ts.translate_text(
        line,
        str=engine,
        from_language=source_language,
        to_language=to_language,
    )
    # print(f"Translating:\n {line.strip()} ->\n {translatedLine.strip()}")
    print(f"{translatedLine.strip()}")
    return translatedLine

def is_subtitle(line):
    if line != '\n' and not line[0].isdigit():
        return True
    return False


def batch_translate(lines, source_language, to_language, engine):
    """批量翻譯"""
    subtitles = ""
    translated_lineNum = []
    for i in range(len(lines)):
        if(is_subtitle(lines[i])):
            subtitles = subtitles+lines[i]
            translated_lineNum.append(i)

    translated_lines=translate(subtitles, source_language, to_language, engine).split("\n")
    
    
    for i in range(len(translated_lineNum)):
        lines[translated_lineNum[i]] = translated_lines[i] + "\n"
    
    return lines


def translate_file(file_path, output_path, source_language, to_language, engine):
    """翻譯文件"""
    with open(output_path, "w", encoding="utf-8") as wf:
        with open(file_path, "r", encoding="utf-8") as rf:
            lines = rf.readlines()
            batch_size = 30
            for i in range(0, len(lines), batch_size):
                batch = lines[i:i + batch_size]
                translatedLine = batch_translate(
                    batch, source_language, to_language, engine
                )
                
                wf.writelines(translatedLine)



def main():
    """主函數"""
    args = parse_arguments()
    translate_file(
        args.file_path, args.output, args.source_language, args.to_language, args.engine
    )


if __name__ == "__main__":
    main()
