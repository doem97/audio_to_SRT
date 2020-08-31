This tool generates `.srt` format subtitle from audios.

# Usage

## STEP 1 Clone this script to your local folder

```
apt-get -y update
apt-get -y install git
git clone https://github.com/doem97/audio_to_SRT.git
cd ./audio_to_SRT
```

## STEP 2 Get XUNFEI cloud certification

This script calls XUNFEI api. You should first get a XUNFEI cloud account at https://console.xfyun.cn/services/lfasr. Go to 语音识别 - 语音转写 to get your APPID and SecretKey.

## STEP 3 Get sound track from video

You can get `.wav` audio from video file using `ffmpeg`. 

E.g. below shows how to get the sound track from `sample.mp4` using sampling rate 16K.

```ffmpeg -i sample.mp4 -ar 16000 audio.wav```

**if you want to use other format rather than `.wav` such as `.mp3` or `.prm`, you should change code block in `get_srt.py`*

## STEP 4 Put sound track

Put `audio.wav` file to ./work_dir/

## STEP 5 Run and get subtitle

Run auto-environment build script `config_env.sh` and then run main script `get_srt.py` to get the srt. As follow:

```
chmod +x config_env.sh
./config_env.sh
source ./xunfei_venv/bin/activate
python get_srt.py APPID SECRET-KEY
```

in which the APPID and SECRET-KEY are gotten in STEP 2. E.g. python get_srt.py 1j3i3g fjiwgo23jio23t8932tj

and it will generate subtitle at `./work_dir/audio.srt`

