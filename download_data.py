import gdown
import os

url = "https://drive.google.com/drive/folders/1gTuDiZS3TOXP7zx-AyN5ViAS9U-vOsgB?usp=sharing"
output = "new_trained_data.zip"

if not os.path.exists("new_trained_data"):
    print("Downloading dataset...")
    gdown.download(url, output, quiet=False)
    
    print("Extracting...")
    import zipfile
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall("new_trained_data")
    
    print("Done!")
else:
    print("Data already exists.")
