# >>> IMPORTS
import json
import os
import winreg
import webbrowser
import random
from time import *
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

# >>> USER CONFIG
app_config = json.load(open("./config.json", "r"))

# >>> CTK SETTINGS
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# >>> ACTUAL CODE
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        '''MAIN WINDOW'''

        # WINDOW SETINGS
        self.title("Locker Presets")
        self.geometry("650x400")
        self.resizable(False, False)
        self.wm_iconphoto(False, tk.PhotoImage(file='./assets/icon.png'))
        # SIDEBAR CONFIG
        self.sidebar_frame = ctk.CTkFrame(master=self, height=400, width=210, fg_color='#1f1f1f')
        self.sidebar_frame.place(x=0, y=0)
        # LOADER TAB CONFIG
        self.loader_frame = ctk.CTkFrame(master=self, height=400, width=445)
        self.loader_frame.place(x=210, y=0)

        '''LOADER'''

        # STATUS LABEL
        self.selected_label = ctk.CTkLabel(master=self.loader_frame, text="Selected Preset", text_color="#858D91", font=("Calibri", 20))
        self.selected_label.place(x=22, y=68, anchor=tk.W)
        # LOAD ENTRY
        self.load_entry = ctk.CTkEntry(master=self.loader_frame, width=300, height=30, corner_radius=50, placeholder_text="Select below", font=("Calibri", 20))
        self.load_entry.place(x=22, y=100, anchor=tk.W)
        # LOAD BUTTON
        self.load_button = ctk.CTkButton(master=self.loader_frame, text="Load", command=self.load_clickEvent, width=40, height=30, fg_color=app_config['color_scheme']['theme_colors']['light'], hover_color=app_config['color_scheme']['theme_colors']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
        self.load_button.place(x=340, y=100, anchor=tk.W)
        # RELOAD BUTTON
        self.reload_button = ctk.CTkButton(master=self.loader_frame, text="", image=ctk.CTkImage(dark_image=Image.open("./assets/reload.png"), size=(20, 20)), command=self.reload_list, width=30, height=30, fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], corner_radius=50)
        self.reload_button.place(x=345, y=30, anchor=tk.W)
        # DELETE BUTTON
        self.delete_button = ctk.CTkButton(master=self.loader_frame, text="", image=ctk.CTkImage(dark_image=Image.open("./assets/delete.png"), size=(20, 20)), command=self.delete_clickEvent, width=30, height=30, fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], corner_radius=50)
        self.delete_button.place(x=281.7, y=30, anchor=tk.W)
        # NEW BUTTON
        self.new_button = ctk.CTkButton(master=self.loader_frame, image=ctk.CTkImage(dark_image=Image.open("./assets/new.png"), size=(20, 20)), text="", command=self.new_clickEvent, width=30, height=30, fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], corner_radius=50)
        self.new_button.place(x=218.4, y=30, anchor=tk.W)
        # SAVE BUTTON
        self.save_button = ctk.CTkButton(master=self.loader_frame, image=ctk.CTkImage(dark_image=Image.open("./assets/save.png"), size=(20, 20)), text="", command=self.save_clickEvent, width=30, height=30, fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], corner_radius=50)
        self.save_button.place(x=155.1, y=30, anchor=tk.W)
        # RANDOM BTTON
        self.random_button = ctk.CTkButton(master=self.loader_frame, image=ctk.CTkImage(dark_image=Image.open("./assets/random.png"), size=(20, 20)), text="", command=self.random_clickEvent, width=30, height=30, fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], corner_radius=50)
        self.random_button.place(x=91.8, y=30, anchor=tk.W)
        # SETTINGS BUTTON
        self.settings_button = ctk.CTkButton(master=self.loader_frame, image=ctk.CTkImage(dark_image=Image.open("./assets/settings.png"), size=(20, 20)), text="", command=self.settings_clickEvent, width=30, height=30, fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], corner_radius=50)
        self.settings_button.place(x=28.5, y=30, anchor=tk.W)

        '''PRESETS LIST'''

        # SCROLLBAR SETUP
        self.list_frame_outer = ctk.CTkFrame(master=self.loader_frame, fg_color="transparent")
        self.list_canvas = ctk.CTkCanvas(master=self.list_frame_outer, highlightthickness=0, bg="#2B2B2B")
        self.list_canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=ctk.TRUE)
        self.list_frame_inner = ctk.CTkFrame(master=self.list_canvas, fg_color="#1f1f1f", width=370, height=265, corner_radius=20)
        self.list_scrollbar = ctk.CTkScrollbar(master=self.list_frame_outer, orientation=ctk.VERTICAL, command=self.list_canvas.yview)
        self.list_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
        self.list_canvas.configure(yscrollcommand=self.list_scrollbar)
        self.list_canvas.bind('<Configure>', lambda e: self.list_canvas.configure(scrollregion=self.list_canvas.bbox("all")))
        self.list_canvas.create_window((0, 0), window=self.list_frame_inner, anchor=ctk.NW)
        self.list_frame_outer.place(x=23, y=125)
        # LOAD LIST
        self.reload_list()

        '''SIDEBAR'''

        # SOCIAL LINKS
        self.discord_button = ctk.CTkButton(master=self.sidebar_frame, image=ctk.CTkImage(dark_image=Image.open("./assets/discord.png"), size=(30, 30)), text="", command=lambda social="discord": self.social_clickEvent(social), width=30, height=30, fg_color="transparent", hover_color="#1f1f1f", corner_radius=50)
        self.discord_button.place(x=100, y=380, anchor=tk.E)
        self.github_button = ctk.CTkButton(master=self.sidebar_frame, image=ctk.CTkImage(dark_image=Image.open("./assets/github.png"), size=(30, 30)), text="", command=lambda social="github": self.social_clickEvent(social), width=30, height=30, fg_color="transparent", hover_color="#1f1f1f", corner_radius=50)
        self.github_button.place(x=110, y=380, anchor=tk.W)
        # PRESET PREVIEW
        self.preview_preset_name = ctk.CTkLabel(master=self.sidebar_frame, text="PRESET", font=("Calibri", 20, "bold"), text_color='#FFFFFF')
        self.preview_preset_name.place(anchor=ctk.W, x=10, y=40)
        self.preview_outfit_name = ctk.CTkLabel(master=self.sidebar_frame, text="Outfit", font=("Calibri", 15, "bold"), text_color='#e3e5e6')
        self.preview_outfit_info = ctk.CTkLabel(master=self.sidebar_frame, text="[####] Rarity", font=("Calibri", 12.5, "bold"), text_color=app_config['color_scheme']['rarity_colors']["Common"], anchor=ctk.W)
        self.preview_outfit_name.place(anchor=ctk.W, x=10, y=80)
        self.preview_outfit_info.place(anchor=ctk.W, x=10, y=105)
        self.preview_melee_name = ctk.CTkLabel(master=self.sidebar_frame, text="Melee", font=("Calibri", 15, "bold"), text_color='#e3e5e6')
        self.preview_melee_info = ctk.CTkLabel(master=self.sidebar_frame, text="[####] Rarity", font=("Calibri", 12.5, "bold"), text_color=app_config['color_scheme']['rarity_colors']["Common"], anchor=ctk.W)
        self.preview_melee_name.place(anchor=ctk.W, x=10, y=150)
        self.preview_melee_info.place(anchor=ctk.W, x=10, y=175)
        self.preview_backpack_name = ctk.CTkLabel(master=self.sidebar_frame, text="Backpack", font=("Calibri", 15, "bold"), text_color='#e3e5e6')
        self.preview_backpack_info = ctk.CTkLabel(master=self.sidebar_frame, text="[####] Rarity", font=("Calibri", 12.5, "bold"), text_color=app_config['color_scheme']['rarity_colors']["Common"], anchor=ctk.W)
        self.preview_backpack_name.place(anchor=ctk.W, x=10, y=220)
        self.preview_backpack_info.place(anchor=ctk.W, x=10, y=245)
        self.preview_parachute_name = ctk.CTkLabel(master=self.sidebar_frame, text="Parachute", font=("Calibri", 15, "bold"), text_color='#e3e5e6')
        self.preview_parachute_info = ctk.CTkLabel(master=self.sidebar_frame, text="[####] Rarity", font=("Calibri", 12.5, "bold"), text_color=app_config['color_scheme']['rarity_colors']["Common"], anchor=ctk.W)
        self.preview_parachute_name.place(anchor=ctk.W, x=10, y=290)
        self.preview_parachute_info.place(anchor=ctk.W, x=10, y=315)

        '''FUNCTIONS'''

    def reload_list(self):
        for PRESETS_LIST_ITEM in self.list_frame_inner.winfo_children():
            PRESETS_LIST_ITEM.destroy()

        PRESETS = sorted(os.listdir(app_config['presets_path']))
        i = 0
        for PRESET in PRESETS:
            i += 1
            ctk.CTkButton(master=self.list_frame_inner, text=f"{PRESET[:len(PRESET) - 5]}", text_color="#FFFFFF", font=("Calibri", 20, "bold"), fg_color="transparent", hover_color=app_config['color_scheme']['theme_colors']['dark'], anchor=ctk.W, corner_radius=50, width=350, command=lambda selected=f"{PRESET[:len(PRESET) - 5]}": self.list_item_clickEvent(selected)).grid(row=i, column=1, pady=5, padx=10, sticky=ctk.W)
            if i == len(PRESETS): ctk.CTkLabel(master=self.list_frame_inner, text=" ").grid(row=i+1, column=0, pady=5, padx=0, sticky=ctk.W)
            if len(PRESETS) < 7: 
                for j in range(7-len(PRESETS)): ctk.CTkLabel(master=self.list_frame_inner, text=" ").grid(row=i+1+j, column=0, pady=5, padx=0, sticky=ctk.W)

    def error_window(self, error:str):
        self.reload_list()
        error_window = ctk.CTkToplevel()
        error_window.title("Error")
        error_window.geometry("300x100")
        error_window.resizable(True, False)
        error_window.wm_iconphoto(False, tk.PhotoImage(file='./assets/icon.png'))

        error_label = ctk.CTkLabel(master=error_window, text=error, font=("Calibri", 20))
        error_label.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

    def delete_clickEvent(self):
        self.reload_list()
        SELECTED_PRESET = self.load_entry.get()
        if os.path.exists(f"{app_config['presets_path']}/{SELECTED_PRESET}.json"):

            def deletion_confirmed():
                os.remove(f"{app_config['presets_path']}/{SELECTED_PRESET}.json")
                self.load_entry.delete(0, len(self.load_entry.get()))
                self.reload_list()
                confirm_window.destroy()
        
            confirm_window = ctk.CTkToplevel()
            confirm_window.title("Deletion")
            confirm_window.geometry("300x200")
            confirm_window.resizable(False, False)
            confirm_window.wm_iconphoto(False, tk.PhotoImage(file='./assets/icon.png'))
            confirm_label = ctk.CTkLabel(master=confirm_window, text=f"Confirm deletion of\n{SELECTED_PRESET}", font=("Calibri", 20))
            confirm_label.place(x=150, y=80, anchor=ctk.CENTER)
            confirm_button = ctk.CTkButton(master=confirm_window, text="CONFIRM", font=("Calibri", 20, "bold"), text_color="#FFFFFF", fg_color="#E53535", hover_color="#A61F1F", command=deletion_confirmed)
            confirm_button.place(x=150, y=125, anchor=ctk.CENTER)

        else: self.error_window("You can't delete something\nthat does not exist!")
            
    def load_clickEvent(self):
            self.reload_list()
            SELECTED_PRESET = self.load_entry.get()
            self.load_entry.delete(0, len(self.load_entry.get()))

            try:
                with open(f"{app_config['presets_path']}/{SELECTED_PRESET}.json", "r") as PRESET_FILE:
                    LOADED_PRESET = json.load(PRESET_FILE)

                self.list_item_clickEvent(SELECTED_PRESET)

                # SKINS
                self.setKeyValue("cosmeticSlotOutfitSkin_h3392416802", LOADED_PRESET['outfit'])
                self.setKeyValue("cosmeticSlotBackpackSkin_h2300351525", LOADED_PRESET['backpack'])
                self.setKeyValue("cosmeticSlotMeleeSkin_h3037021715", LOADED_PRESET['melee'])
                self.setKeyValue("cosmeticSlotParachuteSkin_h661321818", LOADED_PRESET['parachute'])
                # EMOTES
                self.setKeyValue("cosmeticSlotEmote1_h580670127", LOADED_PRESET['emotes'][0])
                self.setKeyValue("cosmeticSlotEmote2_h580670124", LOADED_PRESET['emotes'][1])
                self.setKeyValue("cosmeticSlotEmote3_h580670125", LOADED_PRESET['emotes'][2])
                self.setKeyValue("cosmeticSlotEmote4_h580670122", LOADED_PRESET['emotes'][3])
                self.setKeyValue("cosmeticSlotEmote5_h580670123", LOADED_PRESET['emotes'][4])
                self.setKeyValue("cosmeticSlotEmote6_h580670120", LOADED_PRESET['emotes'][5])
                # SPRAYS
                self.setKeyValue("cosmeticSlotSpray1_h1274385104", LOADED_PRESET['sprays'][0])
                self.setKeyValue("cosmeticSlotSpray2_h1274385107", LOADED_PRESET['sprays'][1])
                self.setKeyValue("cosmeticSlotSpray3_h1274385106", LOADED_PRESET['sprays'][2])
                self.setKeyValue("cosmeticSlotSpray4_h1274385109", LOADED_PRESET['sprays'][3])

            except Exception as err:
                self.error_window(err.args[1])

    def list_item_clickEvent(self, selected:str):
        self.reload_list()
        self.load_entry.delete(0, len(self.load_entry.get()))
        self.load_entry.insert(0, selected)

        with open(f"{app_config['presets_path']}/{selected}.json", "r") as PRESET_FILE:
            PRESET_DATA = json.load(PRESET_FILE)

        SKINS_DATA = {
            "outfit": self.getItemObject(PRESET_DATA['outfit']),
            "melee": self.getItemObject(PRESET_DATA['melee']),
            "backpack": self.getItemObject(PRESET_DATA['backpack']),
            "parachute": self.getItemObject(PRESET_DATA['parachute'])
        }

        self.preview_preset_name.configure(text=selected.upper())

        self.preview_outfit_name.configure(text=SKINS_DATA['outfit']['name'])
        self.preview_melee_name.configure(text=SKINS_DATA['melee']['name'])
        self.preview_backpack_name.configure(text=SKINS_DATA['backpack']['name'])
        self.preview_parachute_name.configure(text=SKINS_DATA['parachute']['name'])

        self.preview_outfit_info.configure(text=f"[{str(SKINS_DATA['outfit']['id']).rjust(4, '0')}] {SKINS_DATA['outfit']['rarity']} Outfit", text_color=app_config['color_scheme']['rarity_colors'][SKINS_DATA['outfit']['rarity']])
        self.preview_melee_info.configure(text=f"[{str(SKINS_DATA['melee']['id']).rjust(4, '0')}] {SKINS_DATA['melee']['rarity']} Melee", text_color=app_config['color_scheme']['rarity_colors'][SKINS_DATA['melee']['rarity']])
        self.preview_backpack_info.configure(text=f"[{str(SKINS_DATA['backpack']['id']).rjust(4, '0')}] {SKINS_DATA['backpack']['rarity']} Backpack", text_color=app_config['color_scheme']['rarity_colors'][SKINS_DATA['backpack']['rarity']])
        self.preview_parachute_info.configure(text=f"[{str(SKINS_DATA['parachute']['id']).rjust(4, '0')}] {SKINS_DATA['parachute']['rarity']} Parachute", text_color=app_config['color_scheme']['rarity_colors'][SKINS_DATA['parachute']['rarity']])

    def new_clickEvent(self):
        PRESET = {
            "outfit": None,
            "backpack": None,
            "melee": None,
            "parachute": None,
            "emotes": [None, None, None, None, None, None],
            "sprays": [None, None, None, None]
        }

        with open(f"{app_config['presets_path']}/new_preset.json", "w") as NEW_FILE:
            NEW_FILE.write(json.dumps(PRESET))
            self.reload_list()
    
    def save_clickEvent(self):

        PRESET = {
            "outfit": self.getKeyValue("cosmeticSlotOutfitSkin_h3392416802"),
            "backpack": self.getKeyValue("cosmeticSlotBackpackSkin_h2300351525"),
            "melee": self.getKeyValue("cosmeticSlotMeleeSkin_h3037021715"),
            "parachute": self.getKeyValue("cosmeticSlotParachuteSkin_h661321818"),
            "emotes": [self.getKeyValue("cosmeticSlotEmote1_h580670127"), self.getKeyValue("cosmeticSlotEmote2_h580670124"), self.getKeyValue("cosmeticSlotEmote3_h580670125"), self.getKeyValue("cosmeticSlotEmote4_h580670122"), self.getKeyValue("cosmeticSlotEmote5_h580670123"), self.getKeyValue("cosmeticSlotEmote6_h580670120")],
            "sprays": [self.getKeyValue("cosmeticSlotSpray1_h1274385104"), self.getKeyValue("cosmeticSlotSpray2_h1274385107"), self.getKeyValue("cosmeticSlotSpray3_h1274385106"), self.getKeyValue("cosmeticSlotSpray4_h1274385109")]
        }

        with open(f"{app_config['presets_path']}/saved_preset.json", "w") as NEW_FILE:
            NEW_FILE.write(json.dumps(PRESET))
            self.reload_list()
    
    def settings_clickEvent(self):
        self.reload_list()
        # WINDOW SETTINGS
        settings_window = ctk.CTkToplevel()
        settings_window.title("Settings")
        settings_window.geometry("500x400")
        settings_window.resizable(False, False)
        settings_window.wm_iconphoto(False, tk.PhotoImage(file='./assets/icon.png'))

        def presets_path_save_clickEvent():
            ORIGINAL_INPUT = presets_path_options_entry.get()
            presets_path_options_entry.delete(0, len(presets_path_options_entry.get()))
            NEW_PATH = ORIGINAL_INPUT.replace("\\", "/")
            self.editConfigFile(presets_path = NEW_PATH)

        def color_scheme_save_clickEvent():
            LIGHT_ORIGINAL_INPUT = color_scheme_light_options_entry.get()
            DARK_ORIGINAL_INPUT = color_scheme_dark_options_entry.get()
            color_scheme_light_options_entry.delete(0, len(color_scheme_light_options_entry.get()))
            color_scheme_dark_options_entry.delete(0, len(color_scheme_dark_options_entry.get()))
            if LIGHT_ORIGINAL_INPUT.startswith("#"):
                NEW_LIGHT_COLOR = LIGHT_ORIGINAL_INPUT
            else:
                NEW_LIGHT_COLOR = f"#{LIGHT_ORIGINAL_INPUT}"
            if DARK_ORIGINAL_INPUT.startswith("#"):
                NEW_DARK_COLOR = DARK_ORIGINAL_INPUT
            else:
                NEW_DARK_COLOR = f"#{DARK_ORIGINAL_INPUT}"
            self.editConfigFile(theme_colors_light=NEW_LIGHT_COLOR, theme_colors_dark=NEW_DARK_COLOR)

        # PRESETS PATH
        presets_path_options_label = ctk.CTkLabel(master=settings_window, text="Presets folder path", text_color="#FFFFFF", font=("Calibri", 20))
        presets_path_options_label.place(x=10, y=30, anchor=ctk.W)

        presets_path_options_entry = ctk.CTkEntry(master=settings_window, placeholder_text="Paste here", font=("Calibri", 20), width=390, height=30, corner_radius=50)
        presets_path_options_entry.place(x=10, y=70, anchor=ctk.W)

        presets_path_options_save_button = ctk.CTkButton(master=settings_window, text="Save", command=presets_path_save_clickEvent, width=40, fg_color=app_config['color_scheme']['theme_colors']['light'], hover_color=app_config['color_scheme']['theme_colors']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
        presets_path_options_save_button.place(x=415, y=70, anchor=ctk.W)

        # COLOR SCHEME
        color_scheme_options_label = ctk.CTkLabel(master=settings_window, text="Color scheme", text_color="#FFFFFF", font=("Calibri", 20))
        color_scheme_options_label.place(x=10, y=148, anchor=ctk.W)

        color_scheme_restartrequired_options_label = ctk.CTkLabel(master=settings_window, text="", text_color=app_config['color_scheme']['theme_colors']['light'], font=("Calibri", 20))
        color_scheme_restartrequired_options_label.place(x=10, y=148, anchor=ctk.W)

        color_scheme_light_options_label = ctk.CTkLabel(master=settings_window, text="Light color:", text_color="#858D91", font=("Calibri", 20))
        color_scheme_light_options_label.place(x=40, y=180, anchor=ctk.W)

        color_scheme_dark_options_label = ctk.CTkLabel(master=settings_window, text="Dark color:", text_color="#858D91", font=("Calibri", 20))
        color_scheme_dark_options_label.place(x=225, y=180, anchor=ctk.W)

        color_scheme_light_options_entry = ctk.CTkEntry(master=settings_window, placeholder_text=app_config['color_scheme']['theme_colors']['light'], font=("Calibri", 20), width=160, height=30, corner_radius=50)
        color_scheme_light_options_entry.place(x=40, y=220, anchor=ctk.W)

        color_scheme_dark_options_entry = ctk.CTkEntry(master=settings_window, placeholder_text=app_config['color_scheme']['theme_colors']['dark'], font=("Calibri", 20), width=160, height=30, corner_radius=50)
        color_scheme_dark_options_entry.place(x=225, y=220, anchor=ctk.W)

        color_scheme_options_save_button = ctk.CTkButton(master=settings_window, text="Save", command=color_scheme_save_clickEvent, width=40, fg_color=app_config['color_scheme']['theme_colors']['light'], hover_color=app_config['color_scheme']['theme_colors']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
        color_scheme_options_save_button.place(x=415, y=220, anchor=ctk.W)

    def random_clickEvent(self):
        self.reload_list()
        PRESETS = os.listdir(fr"{app_config['presets_path']}")
        DRAWN_PRESET = PRESETS[random.randint(0, len(PRESETS)-1)]

        self.load_entry.delete(0, len(self.load_entry.get()))
        self.load_entry.insert(0, DRAWN_PRESET[:len(DRAWN_PRESET)-5])

        self.list_item_clickEvent(DRAWN_PRESET[:len(DRAWN_PRESET)-5])

    def social_clickEvent(self, social:str):
        match social:
            case "discord": webbrowser.open("https://discord.gg/RmkzyA8GMN")
            case "github": webbrowser.open("https://github.com/TeamCLIU/ZRLockerPresets")

    def getItemObject(self, id):
        with open("./assets/shop.json") as SHOP_API_FILE:
            SHOP_API_DATA = json.load(SHOP_API_FILE)

        match id:
            case 0: 
                ITEM_OBJECT = { "id": 0, "sku": "-", "name": "Default", "type": "None", "category": "None", "rarity": "Common", "cost_coins": 0, "cost_gems": 0, "is_stock": False, "can_purchase": False }
            case 4294967294:
                ITEM_OBJECT = { "id": 4294967294, "sku": "-", "name": "Random", "type": "None", "category": "None", "rarity": "None", "cost_coins": 0, "cost_gems": 0, "is_stock": False, "can_purchase": False }
            case "random":
                ITEM_OBJECT = { "id": 4294967294, "sku": "-", "name": "Random", "type": "None", "category": "None", "rarity": "None", "cost_coins": 0, "cost_gems": 0, "is_stock": False, "can_purchase": False }
            case None:
                ITEM_OBJECT = { "id": "None", "sku": "-", "name": "None", "type": "None", "category": "None", "rarity": "None", "cost_coins": 0, "cost_gems": 0, "is_stock": False, "can_purchase": False }
            case _:
                for SHOP_API_ITEM in SHOP_API_DATA['items']:
                    if id == SHOP_API_ITEM['id']:
                        ITEM_OBJECT = SHOP_API_ITEM
        return ITEM_OBJECT

    def setKeyValue(self, slot:str, value):
        KEY = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)
        if value == "random":
            winreg.SetValueEx(KEY, slot, 0, winreg.REG_DWORD, 4294967294)
        if isinstance(value, int):
            winreg.SetValueEx(KEY, slot, 0, winreg.REG_DWORD, value)
    
    def getKeyValue(self, slot:str):
        KEY = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)
        return winreg.QueryValueEx(KEY, slot)[0]

    def editConfigFile(self, presets_path = app_config['presets_path'], theme_colors_light = app_config['color_scheme']['theme_colors']['light'], theme_colors_dark = app_config['color_scheme']['theme_colors']['dark'], rarity_colors_common = app_config['color_scheme']['rarity_colors']['Common'], rarity_colors_uncommon = app_config['color_scheme']['rarity_colors']['Uncommon'], rarity_colors_rare = app_config['color_scheme']['rarity_colors']['Rare'], rarity_colors_epic = app_config['color_scheme']['rarity_colors']['Epic'], rarity_colors_legendary = app_config['color_scheme']['rarity_colors']['Legendary'], rarity_colors_mythic = app_config['color_scheme']['rarity_colors']['Mythic'], rarity_colors_none = app_config['color_scheme']['rarity_colors']['None']):
        TEMPLATE = {
            "presets_path": presets_path,
            "color_scheme": {
                "theme_colors": {
                    "light": theme_colors_light,
                    "dark": theme_colors_dark
                },
                "rarity_colors": {
                    "Common": rarity_colors_common,
                    "Uncommon": rarity_colors_uncommon,
                    "Rare": rarity_colors_rare,
                    "Epic": rarity_colors_epic,
                    "Legendary": rarity_colors_legendary,
                    "Mythic": rarity_colors_mythic,
                    "None": rarity_colors_none
                }
            }
        }
        
        with open("./config.json", "w") as CONFIG_FILE:
            CONFIG_FILE.write(json.dumps(TEMPLATE))

# >>> START FUNCTION
if __name__ == "__main__":
    app = App()
    app.mainloop()
