import json

def convert_dic_to_bytes(args):
    data = json.dumps(args, indent=2).encode('utf-8')
    return data


def get_product_info(product_id,product_name,product_cat,product_des,price):
    try:
        data ={
            'Product Id' : product_id,
            'Product Name' : product_name,
            'Categories' :product_cat,
            'Description' : product_des,
            'Price' : price

        }
        return_data = convert_dic_to_bytes(data)

        return (return_data)
    except Exception as e:
        raise e
