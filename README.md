# ZombsRoyale.io Locker Presets

Are you one of those people who change their skin after each game and ever wanted to be able to change your combo without having to pick a skin for each slot individually? Introducing: Locker Presets!

### How it works?

After downloading and unzipping the zip file containg the program with 7zip or WinRAR, open to the `config.json` with any text editor you want and change the _"presets_path"_ key's value to an absolute path\* to a folder you want to keep your presets in.
Once you're done with that you can safely run `Locker Presets.exe`. You will be greeted with a window filled with different options:

#### Sidebar Options:

- "New" - creates a blank preset in your presets folder.
- "Save" - saves your current in-game locker as a preset.
- "Random" - picks a random preset from your presets folder and loads it.
- "Discord" - opens up your browser and takes you to _[discord.com/invite/RmkzyA8GMN](https://discord.com/invite/RmkzyA8GMN)_.

#### "Locker Presets" Tab:

- "Entry Preset Name" - type in the name of the preset you wish to load (can be with .json suffix or without it).
- "Load" - loads the preset with the name that is currently in the entry box.
- "Presets Explorer" - a list of all presets in your presets folder. To scroll you must have your cursor on the scrollbar and use the scroll on your mouse. Clicking on any of the presets in the list will insert it's name in the entry box.

#### Settings:

- "Presets folder path" - if you want to change your presets folder, you can paste in a new path there and click save.
- "Color scheme" - paste in hex codes (with # prefix) to customize your buttons colors.
- "Order numbers: show zeros" - turn on/off zeros added at the start of the order numbers on the presets list.
- "Order numbers: length" - change the goal length of the numbers.

### Important notes

- This project is still in beta version. You might and probably will encounter some bugs and if you do, please file an issue or DM me on Discord - creaffy#1939.
- If you're filing an issue, please provide all the necressary information relevant to the issue.
- When changing the _"presets_path"_ key's value inside of `config.json` do not use `\` as a directory separator. `\\` and `/` are both fine.
- If you want a specific slot or slots in your locker not to change when loading a preset, open the preset json file that is in your presets folder and change the value of that slot from a number to `null`.
- Expect frequent updates because as I said, it's still in beta and there's a ton of bugs waiting to be discovered and fixed.
- Every time the game updates you're gonna have to download a new `items.json` file from this repository and replace the old one from the assets folder in your installation directory. - *ignore if you're using beta 1.0*
- THE ITEMS.JSON FILE IN RELEASES IS PROBABLY OUTDATED WHICH CAN CAUSE BUGS WHEN TRYING TO LOAD NEW SKINS. PLEASE CHANGE IT FOR THE ONE THAT IS IN THIS REPOSITORY AT /assets/items.json - *ignore if you're using beta 1.0*
- Clicking ENTER will automatically load the preset which's name is curently in the entry box.

### Questions

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

**Q: Why is your code so messy and chaotic and weird? wtf you're so bad**<br>
A: Yes, I know I'm horrible.
