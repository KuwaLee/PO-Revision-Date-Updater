# PO-Revision-Date-Updater

This is a Python script to automatically update `PO-Revision-Date` of `messages.po` while translating for Bluesky app with `VS code`.

## How to use

1. Clone and copy `PO-Revision-Date-Updater.py` any where you like.

2. Edit `update_po_revision_date()` to match your condition.

3. In `VS code` you need [`Run on save`](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) extension.

4. Open `settings.json` to add rules like this.

```
"emeraldwalk.runonsave": {
        "shell":"path/to/python.exe",
        "commands": [
        
            {
                "match": "your-translation-language\\\\messages.po",
                "cmd": "exec(open('path/to/PO-Revision-Date-Updater.py').read())"
            }
        ]
    }
```

5. Enjoy!