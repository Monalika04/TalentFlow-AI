import os
from dotenv import load_dotenv
from google import genai

# Load .env from project root
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("API Key Found:", bool(api_key))
print("=" * 50)

if not api_key:
    raise Exception("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

# Try models one by one
models = [
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-flash-latest",
]

for model in models:
    print(f"\nTrying model: {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Say hello in one sentence."
        )

        print("\nSUCCESS!")
        print("Model:", model)
        print("Response:")
        print(response.text)
        break

    except Exception as e:
        print("FAILED")
        print(e)