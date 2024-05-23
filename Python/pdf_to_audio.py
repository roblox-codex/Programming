import PyPDF2
import pyttsx3

# Prompt user for the PDF file name
pdf_filename = input("Enter the PDF file name (including extension): ").strip()

# Open the PDF file
try:
    with open(pdf_filename, 'rb') as pdf_file:
      
        # Create a PdfFileReader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Get an engine instance for the speech synthesis
        speak = pyttsx3.init()  
      
        # Iterate through each page and read the text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                speak.say(text)
                speak.runAndWait()       

        # Stop the speech engine
        speak.stop()      
        print("Audiobook creation completed.")
      
except FileNotFoundError:
    print("The specified file was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
