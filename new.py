# >>> NEW PRESET CREATOR FUNCTION
# !!! MAKE SURE YOU DON'T ALREADY HAVE A PRESET SAVED AS "new_preset.json" TO AVOID OVERWRITING
import json, os

preset = {
    "outfit": 0,
    "backpack": 0,
    "melee": 0,
    "parachute": 0,
    "emotes": [0,0,0,0,0,0],
    "sprays": [0,0,0,0]
}

with open(f"{os.path.realpath(os.path.dirname(__file__))}/presets/new_preset.json", "w") as file:
    file.write(json.dumps(preset))
