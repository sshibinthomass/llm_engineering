import os
import requests
from dotenv import load_dotenv

load_dotenv()

workspace = os.getenv("BL_WORKSPACE")
api_key = os.getenv("BL_API_KEY")

if not workspace or not api_key:
    raise ValueError("BL_WORKSPACE or BL_API_KEY not found in .env file.")

# The URL format for deployed Blaxel model endpoints
model_name = "black-forest-labs-flux-1-schnell-2"
url = f"https://run.blaxel.ai/{workspace}/models/{model_name}"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "inputs": "Race car and Bike on track"
}

if __name__ == "__main__":
    print(f"Sending prompt to Blaxel endpoint: {url}...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        output_path = "output_blaxel.png"
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Success. Image saved to {output_path}")
    else:
        print(f"Error {response.status_code}: {response.text}")
