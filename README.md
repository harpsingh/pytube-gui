# PyTube-GUI
A simple GUI wrapper written around [pytube](https://pypi.org/project/pytube/) library to download audio and video streams from YouTube

![image](https://user-images.githubusercontent.com/19989521/154816259-204ecf30-31bd-4843-b57d-0712f7630735.png)

Please note that this can only download videos mostly upto 720p in quality because of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH). The more higher quality streams are split into separate video and audio streams. This application downloads only the highest quality stream that has BOTH video and audio. I have written a [separate application](https://github.com/harpsingh/youtube-downloader) that downloads video and audio separately and merges them using ffmpeg.

## Usage
* Download `python-gui.zip` from the `releases` folder in [repository](https://github.com/harpsingh/pytube-gui/blob/main/releases/pytube-gui.zip)
* Extract the zipped file to a folder and run `python-gui.exe`
* Please note that Windows will warn you that it is an unrecognized app as it has not been signed. You can click on More Info > Run anyway.
