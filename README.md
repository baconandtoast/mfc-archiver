# MFC-ACHIVER

This is a script to aid in downloading/recording a live streams from a URL of a `.m3u8` file and saves it to an MP4 file.

Specifically this was written for the website [MyFreeCams](https://www.myfreecams.com/)

## Requirements

- Python 3
- [m3u8](https://pypi.org/project/m3u8/)
- [requests](https://pypi.org/project/requests/)

## Usage

> python mfc-dl.py

The script will ask for the URL of the `.m3u8` file and the name of the MP4 file to save the live stream to. The MP4 file will be created in the current working directory.

## How to get URL for .m3u8

In the case of MyFreeCams, go to models live stream, open developer tools, go to network tab and search for .m3u8.

Should see a bunch of **chunklist_**, right click on one of those and copy link address.

## Note

If the MP4 file already exists, the script will prompt the user to choose a different file name or overwrite the existing file.

## Todo
- Need to add safer way of stopping recording.
- Possibly add GUI
