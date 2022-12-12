import os
import m3u8
import requests
import urllib.parse
import subprocess

# Download the segments of the live stream using ffmpeg
def download_segments(m3u8_obj, m3u8_url, mp4_filename):
    # Create the command for ffmpeg
    command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-c", "copy",
        mp4_filename
    ]

    # Call ffmpeg to download the segments and save the live stream to an MP4 file
    subprocess.run(command)

# Ask the user for the URL of the .m3u8 file
m3u8_url = input("Enter the URL of the .m3u8 file: ")

# Validate the URL
if not urllib.parse.urlparse(m3u8_url).scheme:
    print("Error: the URL is invalid")
    exit(1)

# Fetch the .m3u8 file
response = requests.get(m3u8_url)

# Check the response status code
if response.status_code != 200:
    print("Error: failed to fetch the .m3u8 file")
    exit(1)

# Parse the .m3u8 file
m3u8_obj = m3u8.loads(response.text)

# Ask the user for the name of the MP4 file
mp4_filename = input("Enter the name of the MP4 file to save the live stream to: ")

# Set the title of the terminal window to the name of the MP4 file
os.system('title ' + mp4_filename)

# Check if the file already exists
if os.path.exists(mp4_filename):
    # Prompt the user to choose a different file name or overwrite the existing file
    choice = input("The file already exists. Do you want to overwrite it? [y/n] ")
    if choice.lower() != 'y':
        print("Please choose a different file name.")
        exit(1)

# Download the segments of the live stream using ffmpeg
download_segments(m3u8_obj, m3u8_url, mp4_filename)
