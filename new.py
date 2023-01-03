# >>> NEW PRESET CREATOR FUNCTION
# !!! MAKE SURE YOU DON'T ALREADY HAVE A PRESET SAVED AS "preset.json" TO AVOID OVERWRITING

file = open("presets/preset.json", "w")
file.writelines(['{ "outfit": 0, "backpack": 0, "melee": 0, "parachute": 0 }'])
file.close()
