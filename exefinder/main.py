import os, fnmatch
# to get path and matching the excat pattern

def find(pattern, path):
    res = []
    # store the result extracted from folder
    for root, dirs, files in os.walk(path):
        # import pdb; pdb.set_trace()
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                # checking the .exe pattern if it match or not
                res.append(os.path.join(root, name))
                # if match return the path and folder name?
        return res

print(find('*.exe', 'folder'))
