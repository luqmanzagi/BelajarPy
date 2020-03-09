import re

# Open the file for reading
with open('/home/giza/Percobaan/file.txt') as fd:

    # Iterate over the lines
    for line in fd:

        # Capture one-or-more characters of non-whitespace after the initial match
        match = re.search(r'mov (\w+)', line)

        # Did we find a match?
        if match:
            # Yes, process it
            weather = match.group()
            print(weather) 