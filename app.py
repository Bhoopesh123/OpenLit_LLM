import requests
import openlit

# ==============================
# Initialize OpenLIT (Observability)
# ==============================
# OpenLIT automatically instruments the 'google' provider
openlit.init()

# Replace with your OpenRouter API key
API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "arcee-ai/trinity-large-preview:free",
    "messages": [
        {"role": "user", "content": "Say hi and hello"}
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)
# keep container alive
while True:
    time.sleep(60)