# >>> SAVE CURRENT LOCKER AS A PRESET FUNCTION
# !!! MAKE SURE YOU DON'T ALREADY HAVE A PRESET SAVED AS "saved_preset.json" TO AVOID OVERWRITING

import os, winreg, json
from time import *

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_READ)

def getV(slot):
    return winreg.QueryValueEx(key, slot)[0]

outfit = getV("cosmeticSlotOutfitSkin_h3392416802")
backpack = getV("cosmeticSlotBackpackSkin_h2300351525")
melee = getV("cosmeticSlotMeleeSkin_h3037021715")
parachute = getV("cosmeticSlotParachuteSkin_h661321818")
emotes = [getV("cosmeticSlotEmote1_h580670127"), getV("cosmeticSlotEmote2_h580670124"), getV("cosmeticSlotEmote3_h580670125"), getV("cosmeticSlotEmote4_h580670122"), getV("cosmeticSlotEmote5_h580670123"), getV("cosmeticSlotEmote6_h580670120")]
sprays = [getV("cosmeticSlotSpray1_h1274385104"), getV("cosmeticSlotSpray2_h1274385107"), getV("cosmeticSlotSpray3_h1274385106"), getV("cosmeticSlotSpray4_h1274385109")]

preset = {
    "outfit": outfit,
    "backpack": backpack,
    "melee": melee,
    "parachute": parachute,
    "emojis": [emotes[0],emotes[1],emotes[2],emotes[3],emotes[4],emotes[5]],
    "sprays": [sprays[0],sprays[1],sprays[2],sprays[3]]
}

with open(f"{os.path.realpath(os.path.dirname(__file__))}/presets/saved_preset.json", "w") as file:
    file.write(json.dumps(preset))

print('Preset saved as saved_preset.json')
sleep(5)
