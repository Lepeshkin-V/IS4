import traceback
import re
import json

def exception(trace):
    file_name = "main.py"
    line = re.search("line \d+", trace.split("\n")[1]).group(0)[5:]
    exception = trace.split("\n")[-2].strip()
    print("Ошибка в строке", line,  tree[file_name + ' ' + line][exception][hash(trace)])
if __name__ == '__main__':
    with open("errors.json", 'r') as f:
            errors = json.load(f)
    print(errors)
    tree = {}
    for i in errors:
        tree[i[0]] = {i[1]:{hash(i[2]): i[3]}}

    try:
        raise TimeoutError()
    except:
        exception(traceback.format_exc())
    try:
        raise KeyError()
    except:
        exception(traceback.format_exc())
    try:
        raise TypeError()
    except:
        exception(traceback.format_exc())
    try:
        raise IndexError()
    except:
        exception(traceback.format_exc())
    try:
        raise ImportError()
    except:
        exception(traceback.format_exc())
        