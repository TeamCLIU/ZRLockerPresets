# >>> NEW PRESET CREATOR FUNCTION
# !!! MAKE SURE YOU DON'T ALREADY HAVE A PRESET SAVED AS "new_preset.json" TO AVOID OVERWRITING
import os

file = open(f"{os.path.realpath(os.path.dirname(__file__))}/presets/new_preset.json", "w")
file.writelines(['{ "outfit": 0, "backpack": 0, "melee": 0, "parachute": 0 }'])
file.close()
