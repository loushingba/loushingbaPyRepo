# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:52:16 2020

@author: sanathoi
"""
import moviepy.editor 
video = moviepy.editor.VideoFileClip("washak2.mp4")
audio=video.audio
audio.write_audiofile("result.mp3")
