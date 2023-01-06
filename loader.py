# >>> PRESET LOADER FUNCTION

import winreg, json, os
from time import *

preset_choice = input("Insert preset file name: ")

if preset_choice.endswith('.json'):
    preset_choice_formatted = preset_choice
else:
    preset_choice_formatted = f"{preset_choice}.json"

with open(f"{os.path.realpath(os.path.dirname(__file__))}/presets/{preset_choice_formatted}", "r") as file:
    preset_loaded = json.load(file)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)

def setV(slot, value):
    if value != -1:
        winreg.SetValueEx(key, slot, 0, winreg.REG_DWORD, value)

# SKINS
setV("cosmeticSlotOutfitSkin_h3392416802", preset_loaded['outfit'])
setV("cosmeticSlotBackpackSkin_h2300351525", preset_loaded['backpack'])
setV("cosmeticSlotMeleeSkin_h3037021715", preset_loaded['melee'])
setV("cosmeticSlotParachuteSkin_h661321818", preset_loaded['parachute'])
# EMOTES
setV("cosmeticSlotEmote1_h580670127", preset_loaded['emotes'][0])
setV("cosmeticSlotEmote2_h580670124", preset_loaded['emotes'][1])
setV("cosmeticSlotEmote3_h580670125", preset_loaded['emotes'][2])
setV("cosmeticSlotEmote4_h580670122", preset_loaded['emotes'][3])
setV("cosmeticSlotEmote5_h580670123", preset_loaded['emotes'][4])
setV("cosmeticSlotEmote6_h580670120", preset_loaded['emotes'][5])
# SPRAYS
setV("cosmeticSlotSpray1_h1274385104", preset_loaded['sprays'][0])
setV("cosmeticSlotSpray2_h1274385107", preset_loaded['sprays'][1])
setV("cosmeticSlotSpray3_h1274385106", preset_loaded['sprays'][2])
setV("cosmeticSlotSpray4_h1274385109", preset_loaded['sprays'][3])

print(f"Changed your locker items")

sleep(5)
