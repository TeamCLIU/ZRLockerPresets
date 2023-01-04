# >>> SAVE CURRENT LOCKER AS A PRESET FUNCTION
# !!! MAKE SURE YOU DON'T ALREADY HAVE A PRESET SAVED AS "saved_preset.json" TO AVOID OVERWRITING

import os, winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_READ)

outfit = winreg.QueryValueEx(key, "cosmeticSlotOutfitSkin_h3392416802")[0]
backpack = winreg.QueryValueEx(key, "cosmeticSlotBackpackSkin_h2300351525")[0]
melee = winreg.QueryValueEx(key, "cosmeticSlotMeleeSkin_h3037021715")[0]
parachute = winreg.QueryValueEx(key, "cosmeticSlotParachuteSkin_h661321818")[0]

file = open(f"{os.path.realpath(os.path.dirname(__file__))}/presets/saved_preset.json", "w")
file.writelines(['{ "outfit": ' + f'{outfit}' + ', "backpack": ' f'{backpack}' + ', "melee": ' + f'{melee}' + ', "parachute":' + f'{parachute}' + '}'])
file.close()

print('Preset saved as saved_preset.json')
