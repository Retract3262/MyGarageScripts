import base64
import os
import re

PATH = r"" 
# Path to the directory containing files to extract PNG images from
# C:\Users\<USER>\AppData\LocalLow\Viking\My Garage\save1 as an example

if __name__ == "__main__":

    png_list = []
    png_counter = 1

    for f in os.listdir(PATH):

        if os.path.isdir(os.path.join(PATH, f)):
            continue

        with open(os.path.join(PATH, f), "rb") as fp:
            matches = re.findall(b'iVBORw0KGgo[a-zA-Z0-9+/=]*', fp.read())
            for match in matches:
                if len(match) > 4:
                    png_list.append(match)

    os.makedirs(os.path.join(PATH, "images"), exist_ok=True)

    for png in png_list:
        png_data = base64.b64decode(png)
        with open(os.path.join(PATH, "images", f"{png_counter}.png"), "wb") as out_fp:
            out_fp.write(png_data)
        png_counter += 1

    print(f"Found {png_counter} total png images")
