import subprocess
import argparse

argparser = argparse.ArgumentParser(description="Extract audio from video file")
argparser.add_argument(
    "-v", "--video", help="Path to the video file", default="input_video.mp4"
)
argparser.add_argument(
    "-o", "--output", help="Path to the output audio file", default="output_audio.mp3"
)

args = argparser.parse_args()


def extract_audio(video_path, audio_output_path):
    """
    從影片檔案中分離音軌並保存為音訊檔案。

    :param video_path: 影片檔案的路徑
    :param audio_output_path: 輸出音訊檔案的路徑
    """
    try:
        # 使用 ffmpeg 命令分離音軌
        command = [
            "ffmpeg",
            "-i",
            video_path,
            "-q:a",
            "0",
            "-map",
            "a",
            audio_output_path,
        ]
        subprocess.run(command, check=True)
        print(f"音軌已成功分離並保存到 {audio_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"分離音軌時發生錯誤: {e}")

def audioTowav(audio_file):
    try:
        command = [
            "ffmpeg",
            "-i",
            audio_file,
            "-acodec",
            "pcm_s16le",
            "-ac",
            "1",
            "-ar",
            "48000",
            audio_file + ".wav",
        ]
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"轉換音訊檔案時發生錯誤: {e}")

# 使用範例
video_file = args.video
audio_file = args.output
extract_audio(video_file, audio_file)
audioTowav(audio_file)
