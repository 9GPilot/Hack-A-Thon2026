from google import genai
from dotenv import load_dotenv
load_dotenv()
import os
from google import genai
from google.genai import types
from PIL import Image
from BattlePromptStringGenerate import BattlePromptStringGenerate
import json
from pydantic import BaseModel
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("API_KEY"))










class LocationEnemiesData(BaseModel):
    enemies: list[str]
    locations: list[str]

def generate_enemies_locations_GEMINI_API(inputUserParagraph:str):
    
    prompt = f"""
    Based on this information: '{inputUserParagraph}', generate a list of 3 enemies the 
    user would be scared of and 3 locations they could relate to."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LocationEnemiesData, # Forces the AI to use our class structure
        ),
    )

    data = response.parsed
    
    return data.enemies, data.locations












class DefeatValidation(BaseModel):
    is_reasonable: bool

def is_reasonable_solution_GEMINI_API(enemy: str, location: str, solution: str):
    
    prompt = f"""
    Enemy: {enemy}
    Location: {location}
    Proposed Solution: {solution}
    
    Is this a reasonable way to defeat this enemy in a fantasy/game setting? 
    Return True if it makes sense, and False if it is impossible or illogical.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=DefeatValidation,
        ),
    )

    # Returns just the actual Python boolean
    return response.parsed.is_reasonable








def generate_save_image_GEMINI_API(inputString:str, file_name:str):

    image_name = file_name + '.png'

    #send request to api
    response = client.models.generate_content(
                    model="gemini-2.5-flash-image",
                    contents=[inputString],
                            )
    # parse response object/save image
    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(image_name)












prompt_2 = BattlePromptStringGenerate("dungeon", "goblin").get_prompt_string()

paragraph_input = ""

#TESTS
#generate_save_image(prompt_2, "prompt2")
enemies, locations = generate_enemies_locations_GEMINI_API("I work at an office and am afraid of animals!")
is_reasonable_solution_GEMINI_API(enemies[0], locations[0], "I will use bug spray!")
