from google import genai
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=API_KEY)


from google import genai
from google.genai import types
from PIL import Image


prompt = ("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme")



response = client.models.generate_content(
    model="gemini-2.-flash-image",
    contents=[prompt],
)




image_name = 'generated_image.png'


# parse response object, print the text part and save the other part
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save(image_name)
