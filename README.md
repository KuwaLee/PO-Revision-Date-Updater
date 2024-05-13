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
                "match": "regex",
                "cmd": "exec(open('path/to/PO-Revision-Date-Updater.py').read(), {'file_path': r'${file}', 'timezone': 'Your/Timezone'}))"
            }
        ]
    }
```

> [!NOTE]
>
> - `regex` rule can be like `bluesky-social-app.+zh-TW.+messages.po`, `zh-TW.+messages.po`, `zh-TW\\\\messages.po`, `messages.po`.
>
> - `${file}` or `r'${file}'` can be replace by absolute path.
>
> - `timezone`, For example can be like `Asia/Taipei`.
>
> - You can add multiple rules by adding objects to `commands`.

4. Enjoy!