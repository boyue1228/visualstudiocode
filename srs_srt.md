# SRS server 
- Requirement: FFMPEG compile with libsrt enable 
- Install srt first, standard srt installation folder is /usr/lib but SRS needs /usr/lib64, manually created by ln -sf 
- First checkout 4.0release source
- Then configure --with-srt option 
- use python ./research/api-server/server.py 8085 , this is a nice option to have 
- TS duck module for improvement

