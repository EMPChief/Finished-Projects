import os
import subprocess
import tempfile
from pysubs2 import SSAFile

def convert_mkv_to_srt_with_subtitles(input_folder, output_folder, ffmpeg_path):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mkv"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".mkv", "_subtitled.srt"))

            temp_dir = tempfile.mkdtemp()

            try:
                subtitle_file = os.path.join(temp_dir, "subtitles.ass")
                cmd_extract_subtitles = [
                    ffmpeg_path,
                    '-i', input_file,
                    '-map', '0:s:0',
                    subtitle_file
                ]
                subprocess.run(cmd_extract_subtitles, check=True)

                subs = SSAFile.load(subtitle_file)
                subs.save(output_file, format_='srt')

                print(f"Conversion successful. Output file: {output_file}")
            except Exception as e:
                print(f"Error during conversion of {input_file}: {e}")
            finally:
                if os.path.exists(subtitle_file):
                    os.remove(subtitle_file)
                os.rmdir(temp_dir)

if __name__ == "__main__":
    input_folder = r'C:\Users\bjorn\Downloads\hannibal\Hannibal 2013 Season 1 Complete 720p'
    output_folder = r'C:\Users\bjorn\Downloads\hannibal\test'
    ffmpeg_path = r'C:\Users\bjorn\Documents\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe'

    convert_mkv_to_srt_with_subtitles(input_folder, output_folder, ffmpeg_path)
