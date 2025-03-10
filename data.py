
# Establish data path, Find name and path automagically
def autoPath(name):
    from os import path
    currentFile = path.realpath(__file__)
    currentFileName = path.basename(__file__)
    currentFilePath = currentFile.rstrip(currentFileName)
    path = f"{cFile}{name}.dat" # Data File Path

# Read Data Line
def readLine(path, lineNum):
    try:
        with open(path, 'r') as file:
            for i, line in enumerate(file):
                if i == lineNum - 1:
                    return line.rstrip('\n')
            return None
    except FileNotFoundError:
        return None
    
# Write Data Line
def writeLine(path, lineNum: int, new_content):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
         lines = []

    if 1 <= lineNum <= len(lines):
        lines[lineNum - 1] = str(new_content) + '\n'
    elif lineNum > len(lines):
        lines.extend(['\n'] * (lineNum - len(lines) - 1))
        lines.append(str(new_content) + '\n')
    else:
        return
    with open(path, 'w') as file:
        file.writelines(lines)
