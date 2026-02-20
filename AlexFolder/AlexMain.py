from google import genai

client = genai.Client(api_key="AIzaSyBTN8tUf-yC3PCnHefwnxQHJBnm1TEuhDM")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)