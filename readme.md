This tool generates `.srt` format subtitle from audios.

# Usage

## Get XUNFEI cloud certification

This script calls XUNFEI api. You should first get a XUNFEI cloud account at https://console.xfyun.cn/services/lfasr. Go to 语音识别 - 语音转写 to get your APPID and SecretKey.

Open `./webapi.py` and replace the "to-be-filled" fields with your APPID and SecretKey.

## Get sound track from video

You can get `.wav` audio from video file using `ffmpeg`. 

E.g. below shows how to get the sound track from `sample.mp4` using sampling rate 16K.

```ffmpeg -i sample.mp4 -ar 16000 audio.wav```

**if you want to use other format rather than `.wav` such as `.mp3` or `.prm`, you should change code block in `get_srt.py`*

## Put sound track

Put `audio.wav` file to ./work_dir/

## Run and get subtitle

Strongly recommend you to build a virtual python env for this project.

After installing all the dependences, run

```python get_srt.py```

and it will generate subtitle at `./work_dir/audio.srt`

