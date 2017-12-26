import argparse
import os
import tempfile
import json

filename = 'storage.txt'

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")

args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), filename)
json_res = dict()
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        f.write('')


with open(storage_path, 'r+') as f:

    if args.val is None:
        if os.stat(storage_path).st_size != 0:
            json_res = json.load(f)

        print(", ".join(json_res.get(args.key, list())))
    else:
        if os.stat(storage_path).st_size != 0:
            json_res = json.load(f)

        col = json_res.get(args.key, list())
        col.append(args.val)
        json_res[args.key] = col
        f.seek(0)
        json.dump(json_res, f)
        f.flush()

