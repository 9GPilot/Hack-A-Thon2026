from battlePromptStringGenerate import BattlePromptStringGenerate
from game_state import Game
from gemini_functions import generate_enemies_locations_GEMINI_API, generate_save_image_GEMINI_API, is_reasonable_solution_GEMINI_API







def initialize_gamestate(userInitParagraph: str):
    


    enemies, locations = generate_enemies_locations_GEMINI_API(userInitParagraph)


    #generate the 3 images
    image_prompt_1 = BattlePromptStringGenerate(locations[0], enemies[0]).get_prompt_string()
    generate_save_image_GEMINI_API(image_prompt_1, "prompt_1_image")
    image_prompt_2 = BattlePromptStringGenerate(locations[1], enemies[1]).get_prompt_string()
    generate_save_image_GEMINI_API(image_prompt_2, "prompt_2_image")
    image_prompt_3 = BattlePromptStringGenerate(locations[2], enemies[2]).get_prompt_string()
    generate_save_image_GEMINI_API(image_prompt_3, "prompt_3_image")





    #create the gamestate object and add stages
    game = Game()
    game.add_stage("prompt_1_image.png", locations[0], enemies[0])
    game.add_stage("prompt_2_image.png", locations[1], enemies[1])
    game.add_stage("prompt_3_image.png", locations[2], enemies[2])

    return game



    