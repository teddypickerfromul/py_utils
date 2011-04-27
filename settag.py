#!/usr/bin/python	

import os
import eyeD3
import glob

tag = eyeD3.Tag()
filepaths = glob.glob("/home/teddy/test/*.mp3")
for filePath in filepaths:
    str = os.path.basename(filePath)
    artist = str[0:str.find("-")-1]
    title = str[str.find("-")+2:str.find(".")]
    tag.link(filePath)
    tag.setVersion(eyeD3.ID3_V2_4)
    tag.setTextEncoding(eyeD3.UTF_8_ENCODING)
    tag.setArtist(artist)
    tag.setTitle(title)
    tag.setAlbum("collection")
    tag.update()


