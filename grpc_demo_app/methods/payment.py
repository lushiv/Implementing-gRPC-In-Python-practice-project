import json

def convert_dic_to_bytes(args):
    data = json.dumps(args, indent=2).encode('utf-8')
    return data

def get_payments_info(payment_id,payment_type,payment_method):
    try:
        data ={
            'Payment Id' : payment_id,
            'Payment Type' : payment_type,
            'Methods' :payment_method
        }
        return_data = convert_dic_to_bytes(data)

        return (return_data)
    except Exception as e:
        raise e
