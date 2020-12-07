from pymongo import MongoClient

def mongo_conn(): 
    try: 
        conn = MongoClient(host='127.0.0.1', port=27017) 
        return conn.grpc_test_database
    except Exception as e: 
        print ("Mongo connection Error")
