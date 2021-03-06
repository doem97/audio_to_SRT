#Usage: rename the anyname.wav file as audio.wav
#run python get_srt.py and the subtitle will be generated to ./work_dir/audio.srt

import webapi
import json
import sys


def millitotime(millis):
    millis = int(millis)
    short_milli = millis%1000
    short_milli = int(short_milli)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    return "%02d:%02d:%02d,%03d" % (hours, minutes, seconds, short_milli)

if __name__ == '__main__':
    APPID = sys.argv[1]
    Secret_key = sys.argv[2]
    workdir_au = r"./work_dir/audio.wav"
    outputdir_srt = workdir_au.replace('wav','srt')
    result=webapi.run(workdir_au, APPID, Secret_key)
    alist=result['data'][1:-1].split('},{')
    lenth_w=len(alist)
    for i in range(1,lenth_w-1):
        alist[i]='{'+alist[i]+'}'
    alist[0]=alist[0]+'}'
    alist[lenth_w-1]='{'+alist[lenth_w-1]
    with open(outputdir_srt,'a') as f:
        for i in range(lenth_w):
            currentp=json.loads(alist[i])
            f.write('{}\r\n'.format(i+1)) # For windows usage, add '\r' to enable CRLF
            timea=millitotime(currentp['bg'])
            timeb=millitotime(currentp['ed'])
            sentence=currentp['onebest']
            f.write("{} --> {}\r\n".format(timea,timeb))
            f.write("{}\r\n".format(sentence))
            f.write('\r\n')

