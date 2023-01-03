# >>> PRESET LOADER FUNCTION

import winreg, json, os

preset_choice = input("Insert preset file name: ")

if preset_choice.endswith('.json'):
    preset_choice_formatted = preset_choice
else:
    preset_choice_formatted = f"{preset_choice}.json"

file = open(f"{os.path.realpath(os.path.dirname(__file__))}/presets/{preset_choice_formatted}", "r")
preset_loaded = json.load(file)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)

winreg.SetValueEx(key, "cosmeticSlotOutfitSkin_h3392416802", 0, winreg.REG_DWORD, preset_loaded['outfit'])
winreg.SetValueEx(key, "cosmeticSlotBackpackSkin_h2300351525", 0, winreg.REG_DWORD, preset_loaded['backpack'])
winreg.SetValueEx(key, "cosmeticSlotMeleeSkin_h3037021715", 0, winreg.REG_DWORD, preset_loaded['melee'])
winreg.SetValueEx(key, "cosmeticSlotParachuteSkin_h661321818", 0, winreg.REG_DWORD, preset_loaded['parachute'])

print(f"Changed your locker items to: {preset_loaded['outfit']}, {preset_loaded['backpack']}, {preset_loaded['melee']}, {preset_loaded['parachute']}")

file.close()