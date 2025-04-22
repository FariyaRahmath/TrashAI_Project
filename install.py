import subprocess
import sys

# List of packages to install
packages = [
    'mysql-connector',
    'seaborn',
    'plotly',
    'imagehash',
    'opencv-python',
    'scikit-image',
    'flask'
]

# Upgrade pip
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# Install each package
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("All packages installed successfully.")
