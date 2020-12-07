import json

def convert_dic_to_bytes(args):
    data = json.dumps(args, indent=2).encode('utf-8')
    return data

def get_vendors_info(vendor_id,vendor_name,phone,email,address):
    try:
        data ={
            'Vendors Id' : vendor_id,
            'Vendors name' : vendor_name,
            'vendor Phone' :phone,
            'email' : email,
            'address' : address
        }
        return_data = convert_dic_to_bytes(data)

        return (return_data)
    except Exception as e:
        raise e
