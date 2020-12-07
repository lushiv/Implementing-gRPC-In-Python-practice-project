import json

def convert_dic_to_bytes(args):
    data = json.dumps(args, indent=2).encode('utf-8')
    return data