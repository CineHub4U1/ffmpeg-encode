#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "20288183")
    API_HASH = config("API_HASH", "c552d415c8c88ac267891e1d01deaa57")
    BOT_TOKEN = config("BOT_TOKEN", "5929336845:AAEot0q2AHflpowNzYBO6L1aZ2Gb_Esc_zA")
    DEV = 1322549723
    OWNER = config("OWNER", "1164918935")
    FFMPEG = config(
        "FFMPEG",
        default='-hide_banner -preset veryfast -c:v libx265 -hide_banner -vf scale=1280:-2 -x265-params no-info=1:loglevel=2:bframes=8:range=limited:aq-mode=3:psy-rd=2 -pix_fmt yuv420p10le  -dst_range 1 -colorspace:v bt709 -color_primaries:v bt709 -color_trc:v bt709 -b:v 750k -maxrate 1500k -bufsize 1500k  -r 23.976 -map 0:v -c:a libopus -b:a 64k -ac 2 -vbr on -map 0:a:0 -c:s copy  -map 0:s? -metadata: 'title= Encoded By DaddyCooL' -metadata:s:a: 'title=DaddyCooL' -metadata:s:v: 'title=Encoded By DaddyCooL'
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/cc878234da5eaddafc37f.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
