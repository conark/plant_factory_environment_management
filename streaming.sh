#!/bin/bash
NUM=`ps aux | grep ffmpeg | grep -v grep | wc -l`
if [ $NUM -gt 0 ]; then
        echo "Already running."
        exit
fi

ffmpeg \
        -f alsa -thread_queue_size 8192 \
        -i plughw:1 -f v4l2 \
        -thread_queue_size 8192 \
        -input_format yuyv422 -video_size 640x480 \
        -framerate 30 -i /dev/video0 \
        -vsync 1 -g 16 \
        -c:a aac -b:a 128k -ar 44100 -af "volume=5dB" \
        -f flv rtmp://a.rtmp.youtube.com/live2/pfk7-mp2g-c68r-v1vm-9byk 


        # /dev/null 2>&1 </dev/null &-c:v h264_omx -b:v 768k -bufsize 768k 

# stream_key="pfk7-mp2g-c68r-v1vm-9byk"
# audio_file="music/bgm.mp3"

# while true
# do
#   ffmpeg -stream_loop -1 -i "${audio_file}" \
#   -f v4l2 -s 1280x768 -r 10 -i /dev/video0 -vcodec libx264 -vf \
#   drawtext="fontfile=/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf:x=2:y=2:fontsize=32:fontcolor=white:box=1:boxcolor=black@0.4:text='%{localtime} Sapporo Sta.'" \
#   -pix_fmt yuv420p -preset ultrafast -r 15 -g 30 -b:v 750k \
#   -acodec aac -ar 44100 -threads 0 -b:a 128k -bufsize 512k \
#   -f flv rtmp://a.rtmp.youtube.com/live2/${stream_key}　
# done
