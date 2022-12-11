import os
import m3u8
import requests
import urllib.parse

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
try:
    m3u8_obj = m3u8.loads(response.text)
except m3u8.exceptions.M3U8Error as e:
    print("Error: failed to parse the .m3u8 file")
    exit(1)

# Ask the user for the name of the MP4 file
mp4_filename = input("Enter the name of the MP4 file to save the live stream to: ")

# Check if the file already exists
if os.path.exists(mp4_filename):
    # Prompt the user to choose a different file name or overwrite the existing file
    choice = input("The file already exists. Do you want to overwrite it? [y/n] ")
    if choice.lower() != 'y':
        print("Please choose a different file name.")
        exit(1)

# Print the information about the stream
print(m3u8_obj.data)

# Save the stream to an MP4 file
with open(mp4_filename, 'wb') as f:
    while True:
        # Download and save the segments of the live stream
        for i, segment in enumerate(m3u8_obj.data['segments']):
            # Fetch the segment
            url = urllib.parse.urljoin(m3u8_url, segment['uri'])
            response = requests.get(url)

            # Check the response status code
            if response.status_code != 200:
                print("Error: failed to download segment {}".format(i))
                exit(1)

            # Write the segment to the file
            f.write(response.content)

            # Show progress
            print("Downloaded segment {} of {}".format(i + 1, len(m3u8_obj.data['segments'])))

        # Check if the live stream has ended
        if m3u8_obj.is_endlist:
            # The live stream has ended, so we can stop the loop
            break

        # The live stream hasn't ended yet, so we need to
        # fetch the next set of segments
        response = requests.get(m3u8_url)
        m3u8_obj = m3u8.loads(response.text)
