import json
import toml
import re

TEMPLATE_PATH   = "./settings_template.json"
SETTINGS_PATH   = "./settings.toml"
OUT_PATH        = "../settings.json"

def replace_placeholders(key, value, data):
    return data.replace("${%s}" % key, str(value).lower())

def main():
    with open(TEMPLATE_PATH) as data:
        template = data.read()

        # Remove comments
        template = re.sub(r'.*\/\/.*', '', template)

        # Remove empty lines
        template = '\n'.join([line for line in template.split('\n') if line.strip()])

    with open(SETTINGS_PATH) as data:
        settings = toml.load(data)

    for key, value in settings.items():
        template = replace_placeholders(key, value, template)

    with open(OUT_PATH, 'w+') as file:
        file.write(template)

if __name__ == '__main__':
    main()