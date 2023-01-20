# ZombsRoyale.io Locker Presets

Are you one of those people who change their skin after each game and ever wanted to be able to change your combo without having to pick a skin for each slot individually? Introducing: Locker Presets!

### How it works?

After downloading and unzipping the zip file containg the program with 7zip or WinRAR, open to the `config.json` with any text editor you want and change the _"presets_path"_ key's value to an absolute path\* to a folder you want to keep your presets in.
Once you're done with that you can safely run `Locker Presets.exe`. You will be greeted with a window filled with different options:

### Options:

- "Settings" *(gear icon)* - takes you to the settings menu.
- "Random" *(two arrows icon)* - picks a random preset from your presets folder and loads it.
- "Save" *(files icon)* - saves your current in-game locker as a preset.
- "New" *(plus icon)* - creates a blank preset in your presets folder.
- "Delete" *(trashcan icon)* - removes selected preset.
- "Reload" *(rounded arrow icon)* - reloads the presets list.

### Loading Presets:

- Select a preset from the list,
- Click "Load",
- That's it. The preset is loaded.

### Settings:

- "Presets folder path" - paste in a new path there and click "Save".
- "Color scheme" - paste in hex codes to customize your buttons colors and click "Save".

### Important notes:

- This project is still in beta version. You might and probably will encounter some bugs and if you do, please file an issue or DM me on Discord - creaffy#1939.
- If you're filing an issue, please provide all the necressary information relevant to the issue.
- When changing the _"presets_path"_ key's value inside of `config.json` do not use `\` as a directory separator. `\\` and `/` are both fine.
- If you want a specific slot or slots in your locker not to change when loading a preset, open the preset json file that is in your presets folder and change the value of that slot from a number to `null`.
- Expect frequent updates because as I said, it's still in beta and there's a ton of bugs waiting to be discovered and fixed.
- To scroll the presets list you must have your cursor on the scrollbar and use the scroll on your mouse. Clicking on any of the presets in the list will insert it's name in the entry box.
- Using `"random"` (with quotes) or `4294967294` as a skin ID will result in the game picking a random skin (does not work on sprays and emotes).

### Questions:

**Q: Can I get banned for using this?**<br>
A: I am almost sure you cannot but use at your own risk.

**Q: Will this work on browser?**<br>
A: No, it won't.

**Q: Is there a version for mobile devices?**<br>
A: No, there isn't.

**Q: Can I load skins that I do not own?**<br>
A: No, you can't. You must have the skin unlocked in order for it to load in game. It will be visible in cosmetics tab but not when you hop into a game.

**Q: How do I download this?**<br>
A: From releases tab.

**Q: What are "rarity colors" in the config file?**<br>
A: Hex codes for preset previews. You can change them if you want.
