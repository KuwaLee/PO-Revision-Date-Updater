# PO-Revision-Date-Updater

This is a Python script to automatically update `PO-Revision-Date` of `messages.po` while translating for Bluesky app with `VS code`.

## How to use

1. Clone project.

2. In `VS code` you need [`Run on save`](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) extension.

4. Open `settings.json` to add rules like this.

```
"emeraldwalk.runonsave": {
        "shell":"path/to/python.exe",
        "commands": [
            {
                "match": "your-translation-language\\\\messages.po",
                "cmd": "exec(open('path/to/PO-Revision-Date-Updater.py').read(), {'file_path': 'path/to/messages.po', 'timezone': 'Your/Timezone'}))"
            }
        ]
    }
```

> [!NOTE]
> `timezone`, For example will be like `Asia/Taipei`
> You can add multiple rules by adding objects to commands

4. Enjoy!