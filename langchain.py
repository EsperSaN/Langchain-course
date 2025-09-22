import os
from dotenv import load_dotenv

load_dotenv()


def main():
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in environment variables.")
    print(f"Gemini API Key: {gemini_api_key}")


if __name__ == "__main__":
    main()