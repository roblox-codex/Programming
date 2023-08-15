#pip install google-cloud-translate


from google.cloud import translate

def translate_text(text, target_language="en"):
    # Replace with Google Cloud API key
    api_key = "YOUR_API_KEY"
    client = translate.TranslationServiceClient()

    parent = f"projects/YOUR_PROJECT_ID"

    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        target_language_code=target_language,
    )

    translated_text = response.translations[0].translated_text
    return translated_text

def main():
    while True:
        original_text = input("Enter text to translate (or 'exit' to quit): ")
        if original_text.lower() == "exit":
            print("Exiting...")
            break

        target_language = input("Enter target language code (e.g., 'es' for Spanish): ")
        translated_text = translate_text(original_text, target_language)

        print("Translated text:", translated_text)
        print()

if __name__ == "__main__":
    main()
