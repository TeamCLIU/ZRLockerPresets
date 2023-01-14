# i know my code is messy as shit but the important thing is that it works haha
# if you know any way i could manage it better or if you want to help me with tkinter (it sucks), feel free to dm me on discord: creaffy#1939
# version beta 1.0 || 14-1-22

# IMPORTS
import json
import os
import winreg
import webbrowser
import keyboard
import random
from time import *
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

# CONFIG.JSON LOADER
app_config = json.load(open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json", "r"))

# WINDOW CONFIG
app=ctk.CTk()
app.configure(bg="#383838")
app.title("Locker Presets")
app.geometry("1000x400")
app.minsize(1000,400)
app.maxsize(1000,400)
app.resizable(False, False)
app.wm_iconphoto(False, tk.PhotoImage(file='assets/icon.png'))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# FRAMES & CANVAS CONFIG
main_frame = ctk.CTkFrame(master=app, height=150, width=1000, fg_color="#242424")
presets_list_frame_outer = ctk.CTkFrame(master=app, height=250, width=400, fg_color="#242424")
sidebar_frame = ctk.CTkFrame(master=app, height=400, width=110, fg_color="#1f1f1f")
presets_list_canvas = ctk.CTkCanvas(master=presets_list_frame_outer, bg="#242424", highlightthickness=0)
presets_list_canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=1)
presets_list_frame_inner = ctk.CTkFrame(master=presets_list_canvas, fg_color="#1f1f1f", bg_color="#1f1f1f")

def reload_presets():
    presets = sorted(os.listdir(app_config['presets_path']))
    i = 0
    for preset in presets:
        i+=1
        preset_file = json.load(open(fr"{app_config['presets_path']}\{preset}"))
        items_file = json.load(open(f"{os.path.realpath(os.path.dirname(__file__))}/assets/items.json"))

        def getItemName(slot):
            if str(preset_file[slot]) in items_file:
                return items_file[str(preset_file[slot])]
            elif preset_file[slot] == None:
                return "Null"
            elif preset_file[slot] == 0:
                return "Default"

        if app_config['rjust']['status'] == "1":
            show_status_output = f"{str(i).rjust(int(app_config['rjust']['length']), '0')} :"
        else:
            show_status_output = " "

        ctk.CTkButton(master=presets_list_frame_inner, text=f"{show_status_output} {preset[:len(preset) - 5]}", text_color="#FFFFFF", font=("Calibri", 20, "bold"), fg_color="transparent", hover_color=app_config['color_scheme']['light'], anchor=ctk.W, corner_radius=50, command=lambda selected = f"{preset[:len(preset) - 5]}": presets_list_btn_clicked_func(selected), width=360).grid(row=i, column=1, pady=5, padx=10, sticky=ctk.W)
        if i == len(presets):
            ctk.CTkLabel(master=presets_list_frame_inner, text=" ").grid(row=i+1, column=0, pady=5, padx=0, sticky=ctk.W)
def new_btn_func():
    preset = {
        "outfit": 0,
        "backpack": 0,
        "melee": 0,
        "parachute": 0,
        "emotes": [0,0,0,0,0,0],
        "sprays": [0,0,0,0]
    }

    with open(f"{app_config['presets_path']}/new_preset.json", "w") as file:
        file.write(json.dumps(preset))

    load_success_label.configure(text="Blank preset has been created", text_color="#565B5E")
    reload_presets()
def save_btn_func():
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
        "emotes": [emotes[0],emotes[1],emotes[2],emotes[3],emotes[4],emotes[5]],
        "sprays": [sprays[0],sprays[1],sprays[2],sprays[3]]
    }

    with open(f"{app_config['presets_path']}/saved_preset.json", "w") as file:
        file.write(json.dumps(preset))

    load_success_label.configure(text="Current locker has been saved", text_color="#565B5E")
    reload_presets()
def load_btn_func():
    preset_choice = load_entry.get()
    load_entry.delete(0, len(load_entry.get()))

    if preset_choice.endswith('.json'):
        preset_choice_formatted = preset_choice
    else:
        preset_choice_formatted = f"{preset_choice}.json"

    try:
        file = open(f"{app_config['presets_path']}/{preset_choice_formatted}", "r")
        preset_loaded = json.load(file)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)

        def setV(slot, value):
            if value != None:
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

        load_success_label.configure(text="Preset has been loaded", text_color="#565B5E")
    except FileNotFoundError:
        load_success_label.configure(text="Preset does not exist", text_color="#565B5E")
def discord_btn_func():
    webbrowser.open("https://discord.gg/RmkzyA8GMN")
def random_btn_func():

    presets = os.listdir(fr"{app_config['presets_path']}/presets")
    random_preset = presets[random.randint(0, len(presets)-1)]
    with open(fr"{app_config['presets_path']}/presets/{random_preset}") as file:
        preset_loaded = json.load(file)

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Yang Liu\\Zombs Royale", 0, winreg.KEY_ALL_ACCESS)

    def setV(slot, value):
        if value != None:
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

    load_success_label.configure(text=f"{random_preset} has been loaded", text_color="#565B5E")
def presets_path_options_save_btn_func():
    input = presets_path_options_entry.get()
    presets_path_options_entry.delete(0, len(presets_path_options_entry.get()))
    new_path = input.replace("\\", "/")
    new_config_structure = {
        "presets_path": new_path,
        "color_scheme": {
            "light": app_config['color_scheme']['light'],
            "dark": app_config['color_scheme']['dark']
        },
        "rjust": {
            "length": app_config['rjust']['length'],
            "status": app_config['rjust']['status']
        }
    }
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json", "w") as new_app_config:
        new_app_config.write(json.dumps(new_config_structure))
def presets_list_btn_clicked_func(preset):
    load_entry.delete(0, len(load_entry.get()))
    load_entry.insert(0, preset)
def color_scheme_options_save_btn_func(light, dark):
    if light != '' and dark != '':
        new_config_structure = {
            "presets_path": app_config['presets_path'],
            "color_scheme": {
                "light": light,
                "dark": dark
            },
            "rjust": {
                "length": app_config['rjust']['length'],
                "status": app_config['rjust']['status']
            }
        }   
        with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json", "w") as new_app_config:
            new_app_config.write(json.dumps(new_config_structure))

        color_scheme_restartrequired_options_label.configure(text="restart required")
def rjust_show_options_toggle():
    def edit_status(status):
        new_config_structure = {
            "presets_path": app_config['presets_path'],
            "color_scheme": {
                "light": app_config['color_scheme']['light'],
                "dark": app_config['color_scheme']['dark'],
            },
            "rjust": {
                "length": app_config['rjust']['length'],
                "status": status
            }
        }   
        with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json", "w") as new_app_config:
            new_app_config.write(json.dumps(new_config_structure))

    edit_status(rjust_show_options_switch.get())

    if rjust_show_options_switch.get() == "1":
        rjust_length_options_entry.configure(state="normal")
        rjust_length_options_save_button.configure(state="normal")
        rjust_length_options_entry.configure(fg_color="#38343c")
        rjust_length_options_save_button.configure(fg_color=app_config['color_scheme']['light'])
    elif rjust_show_options_switch.get() == "0":
        rjust_length_options_entry.configure(state="disabled")
        rjust_length_options_save_button.configure(state="disabled")
        rjust_length_options_entry.configure(fg_color="#1f1f1f")
        rjust_length_options_save_button.configure(fg_color=app_config['color_scheme']['dark'])

    rjust_show_restartrequired_options_label.configure(text="restart required")
def rjust_length_options_save_btn_func(num):

    try:
        if isinstance(int(num), int):
            new_config_structure = {
                "presets_path": app_config['presets_path'],
                "color_scheme": {
                    "light": app_config['color_scheme']['light'],
                    "dark": app_config['color_scheme']['dark'],
                },
                "rjust": {
                    "length": num,
                    "status": rjust_show_options_switch.get()
                }
            }   
            with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json", "w") as new_app_config:
                new_app_config.write(json.dumps(new_config_structure))
            rjust_show_restartrequired_options_label.configure(text="restart required")
    except ValueError:
        print("NaN")

# DISPLAY PRESETS LIST
reload_presets()

# GITHUB REPO WATERMARK
github_label = ctk.CTkLabel(master=app, text="github.com/TeamCLIU/ZRLockerPresets | Beta Release v1.0", text_color="#565B5E", font=("Calibri", 10))
github_label.place(x=990, y=390, anchor=tk.E)

# SIDEBAR FRAME LAYOUT CONFIG
new_button = ctk.CTkButton(master=sidebar_frame, text="New", command=new_btn_func, width=40, height=30, fg_color="transparent", hover_color="#1f1f1f", text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
new_button.place(x=5, y=25, anchor=tk.W)

save_button = ctk.CTkButton(master=sidebar_frame, text="Save", command=save_btn_func, width=40, height=30, fg_color="transparent", hover_color="#1f1f1f", text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
save_button.place(x=5, y=60, anchor=tk.W)

random_button = ctk.CTkButton(master=sidebar_frame, text="Random", command=random_btn_func, width=40, height=30, fg_color="transparent", hover_color="#1f1f1f", text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
random_button.place(x=5, y=95, anchor=tk.W)

discord_button = ctk.CTkButton(master=sidebar_frame, text="Discord", command=discord_btn_func, width=40, height=30, fg_color="transparent", hover_color="#1f1f1f", text_color=app_config['color_scheme']['light'], font=("Calibri", 20, "bold"), corner_radius=50)
discord_button.place(x=5, y=380, anchor=tk.W)

# LOAD FUNCTION LAYOUT
load_button = ctk.CTkButton(master=main_frame, text="Load", command=load_btn_func, width=40, height=30, fg_color=app_config['color_scheme']['light'], hover_color=app_config['color_scheme']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50)
load_button.place(x=480, y=100, anchor=tk.CENTER)

load_entry = ctk.CTkEntry(master=main_frame, width=300, height=30, corner_radius=50, placeholder_text="Enter preset name here", font=("Calibri", 20))
load_entry.place(x=270, y=100, anchor=tk.CENTER)

load_success_label = ctk.CTkLabel(master=main_frame, text="Preset to be loaded", text_color="#858D91", font=("Calibri", 20))
load_success_label.place(x=120, y=68, anchor=tk.W)

# TOPBAR FRAME LAYOUT CONFIG
lockerpresets_title_label = ctk.CTkLabel(master=main_frame, text="Locker Presets", font=("Calibri", 25, "bold")).place(x=120, y=25, anchor=ctk.W)
settings_title_label = ctk.CTkLabel(master=main_frame, text="Settings", font=("Calibri", 25, "bold")).place(x=570, y=25, anchor=ctk.W)

# SETTINGS: PRESETS FOLDER PATH
presets_path_options_label = ctk.CTkLabel(master=main_frame, text="Presets folder path", text_color="#858D91", font=("Calibri", 20)).place(x=570, y=68, anchor=ctk.W)
presets_path_options_entry = ctk.CTkEntry(master=main_frame, placeholder_text="Paste here", font=("Calibri", 20), width=300, height=30, corner_radius=50)
presets_path_options_entry.place(x=570, y=100, anchor=ctk.W)
presets_path_options_save_button = ctk.CTkButton(master=main_frame, text="Save", command=presets_path_options_save_btn_func, width=40, fg_color=app_config['color_scheme']['light'], hover_color=app_config['color_scheme']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50).place(x=890, y=100, anchor=ctk.W)

# SETTINGS: COLOR SCHEME
color_scheme_options_label = ctk.CTkLabel(master=main_frame, text="Color scheme", text_color="#858D91", font=("Calibri", 20)).place(x=570, y=148, anchor=ctk.W)
color_scheme_restartrequired_options_label = ctk.CTkLabel(master=main_frame, text="", text_color=app_config['color_scheme']['light'], font=("Calibri", 20))
color_scheme_restartrequired_options_label.place(x=725, y=148, anchor=ctk.W)
color_scheme_light_options_label = ctk.CTkLabel(master=main_frame, text="Light color:", text_color="#565B5E", font=("Calibri", 20)).place(x=610, y=180, anchor=ctk.W)
color_scheme_dark_options_label = ctk.CTkLabel(master=main_frame, text="Dark color:", text_color="#565B5E", font=("Calibri", 20)).place(x=610, y=220, anchor=ctk.W)
color_scheme_light_options_entry = ctk.CTkEntry(master=main_frame, placeholder_text=app_config['color_scheme']['light'], font=("Calibri", 20), width=150, height=30, corner_radius=50)
color_scheme_light_options_entry.place(x=720, y=180, anchor=ctk.W)
color_scheme_dark_options_entry = ctk.CTkEntry(master=main_frame, placeholder_text=app_config['color_scheme']['dark'], font=("Calibri", 20), width=150, height=30, corner_radius=50)
color_scheme_dark_options_entry.place(x=720, y=220, anchor=ctk.W)
color_scheme_options_save_button = ctk.CTkButton(master=main_frame, text="Save", command= lambda: color_scheme_options_save_btn_func(color_scheme_light_options_entry.get(), color_scheme_dark_options_entry.get()), width=40, fg_color=app_config['color_scheme']['light'], hover_color=app_config['color_scheme']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50).place(x=890, y=200, anchor=ctk.W)

# SETTINGS: RJUST
rjust_options_label = ctk.CTkLabel(master=main_frame, text="Order numbers", text_color="#858D91", font=("Calibri", 20)).place(x=570, y=268, anchor=ctk.W)
rjust_show_options_label = ctk.CTkLabel(master=main_frame, text="Show zeros:", text_color="#565B5E", font=("Calibri", 20)).place(x=610, y=300, anchor=ctk.W)
rjust_show_options_switch = ctk.CTkSwitch(master=main_frame, text="", switch_width=150, corner_radius=50, fg_color="#1f1f1f", progress_color=app_config['color_scheme']['light'], offvalue="0", onvalue="1", command=rjust_show_options_toggle)
rjust_show_options_switch.place(x=720, y=301, anchor=ctk.W)
rjust_length_options_label = ctk.CTkLabel(master=main_frame, text="Length:", text_color="#565B5E", font=("Calibri", 20)).place(x=610, y=340, anchor=ctk.W)
rjust_length_options_entry = ctk.CTkEntry(master=main_frame, placeholder_text=app_config['rjust']['length'], font=("Calibri", 20), width=150, height=30, corner_radius=50)
rjust_length_options_entry.place(x=720, y=340, anchor=ctk.W)
rjust_length_options_save_button = ctk.CTkButton(master=main_frame, text="Save", command= lambda: rjust_length_options_save_btn_func(rjust_length_options_entry.get()), width=40, fg_color=app_config['color_scheme']['light'], hover_color=app_config['color_scheme']['dark'], text_color="#FFFFFF", font=("Calibri", 20, "bold"), corner_radius=50, text_color_disabled="#FFFFFF")
rjust_length_options_save_button.place(x=890, y=340, anchor=ctk.W)

if app_config['rjust']['status'] == "1": 
    rjust_show_options_switch.select()
if app_config['rjust']['status'] == "0": 
    rjust_length_options_entry.configure(state="disabled") 
    rjust_length_options_save_button.configure(state="disabled")
    rjust_length_options_entry.configure(fg_color="#1f1f1f")
    rjust_length_options_save_button.configure(fg_color=app_config['color_scheme']['dark'])

rjust_show_restartrequired_options_label = ctk.CTkLabel(master=main_frame, text="", text_color=app_config['color_scheme']['light'], font=("Calibri", 20))
rjust_show_restartrequired_options_label.place(x=725, y=268, anchor=ctk.W)

# PRESETS LIST SCROLLBAR
presets_list_scrollbar = ctk.CTkScrollbar(master=presets_list_frame_outer, orientation=ctk.VERTICAL, command=presets_list_canvas.yview)
presets_list_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
presets_list_canvas.configure(yscrollcommand=presets_list_scrollbar)
presets_list_canvas.bind('<Configure>', lambda e: presets_list_canvas.configure(scrollregion=presets_list_canvas.bbox("all")))
presets_list_canvas.create_window((0,0), window=presets_list_frame_inner, anchor=ctk.NW)

# LOAD FRAMES
main_frame.pack(fill=ctk.BOTH, expand=1)
presets_list_frame_outer.place(x=120, y=150)
sidebar_frame.place(x=0, y=0)

# ENTER = LOAD
keyboard.add_hotkey('Enter', lambda: load_btn_func())

app.mainloop()