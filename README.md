# POT-Creation-Date-Updater

This is a Python script to automatically update `POT-Creation-Date` of `messages.po` while translating for Bluesky app with `VS code`.

## How to use

1. Clone and copy `POT-Creation-Date-Updater.py` any where you like.

2. Edit `update_pot_creation_date()` to match your condition.

3. In `VS code` you need [`Run on save`](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) extension.

4. Open `settings.json` to add rules like this.

```
"emeraldwalk.runonsave": {
        "shell":"path/to/python.exe",
        "commands": [
        
            {
                "match": "your-translation-language\\\\messages.po",
                "cmd": "exec(open('path/to/POT-Creation-Date-Updater.py').read())"
            }
        ]
    }
```

5. Enjoy!