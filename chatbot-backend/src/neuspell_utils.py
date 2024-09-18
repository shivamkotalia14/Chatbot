import gdown
import os

# List of file URLs from the Google Drive folder
file_urls = [
    "https://drive.google.com/uc?id=1e23On5jwjYd8vCYt8kzxm_xgn8OoB-qn",
    "https://drive.google.com/uc?id=1aTvTxtchNRfrwcnyXcSWURvC1V-7_IY9",
    "https://drive.google.com/uc?id=1LZFXvSHUFRrtG1TW14rl4Y8Y1yCTCugD",
    "https://drive.google.com/uc?id=13FnCUPAG-P0-rFIRNewHYXZzwp4HBIjr",
    "https://drive.google.com/uc?id=12wPZCl04-00-6YhsX7EE1cEGYZtgGUvk",
    "https://drive.google.com/uc?id=11Bo86aI0MxAU1MHpF-eYfAHg3HqiT9me",
]

# Local folder to store the downloaded files
base_output_folder = os.path.join(os.getcwd(), "neuspell", "data", "checkpoints")
sub_folder = "subwordbert-probwordnoise"

# Full path to the subfolder
output_folder = os.path.join(base_output_folder, sub_folder)

# Create the base and sub-folder if they don't exist
os.makedirs(output_folder, exist_ok=True)

# Function to download each file with a custom name
def download_file(file_url, output_folder, custom_name):
    output_path = os.path.join(output_folder, custom_name)
    gdown.download(file_url, output_path, quiet=False)

# Custom names for the downloaded files
custom_names = ["progress_retrain_from_epoch8.txt", "progress.txt", "progress_retrain_from_epoch12.txt", "model.pth-001.tar", "pytorch_model.bin", "vocab.pkl"]

# Download all files from the file_urls list with custom names
for url, name in zip(file_urls, custom_names):
    download_file(url, output_folder, name)

print("Download completed!")