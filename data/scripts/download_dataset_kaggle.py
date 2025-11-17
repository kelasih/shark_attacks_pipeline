import os
import shutil
import subprocess
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the data directory relative to the project
data_dir = Path("../data").resolve()
data_dir.mkdir(parents=True, exist_ok=True)

# Kaggle dataset reference
dataset = "felipeesc/shark-attack-dataset"

# Get Kaggle credentials from environment
kaggle_username = os.getenv("KAGGLE_USERNAME")
kaggle_key = os.getenv("KAGGLE_KEY")

# Checks if the credentials are set up
if not kaggle_username or not kaggle_key:
    raise EnvironmentError(
        "❌ Missing Kaggle credentials. "
        "Please set KAGGLE_USERNAME and KAGGLE_KEY "
        "in your .env file or environment variables."
    )

os.environ['KAGGLE_USERNAME'] = kaggle_username
os.environ['KAGGLE_KEY'] = kaggle_key

# Check if the CSV already exists
csv_file = data_dir / "attacks.csv"
if csv_file.exists():
    print(f"✅ Dataset already exists at {csv_file}, skipping download.")
else:

    # Checks if Kaggle CLI is installed
    if not shutil.which("kaggle"):
        raise RuntimeError("❌ Kaggle CLI not found. Install it with: pip install kaggle")

    # Download and unzip the dataset to the data directory
    subprocess.run([
        "kaggle", "datasets", "download",
        "-d", dataset,
        "--unzip",
        "-p", str(data_dir)
    ], check=True)

    print(f"✅ Dataset downloaded and extracted to {data_dir}")