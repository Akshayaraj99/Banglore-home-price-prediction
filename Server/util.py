import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
         loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1

    x_pred = np.zeros(len(__data_columns))
    x_pred[0] = sqft
    x_pred[1] = bath
    x_pred[2] = bhk
    if loc_index >= 0:
        x_pred[loc_index] = 1
    return round(__model.predict([x_pred]) [0],2)

def load_saved_artifacts():
    global __data_columns, __locations, __model  # ✅ Declare what you're modifying

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")

def get_location_names():
    return __locations

    with open("./artifacts/banglore_home_prices_model.pickle",'r')as f:
        __model=pickle.load(f)
        print("loading saved artifacts...done")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
    print(get_estimated_price('kalhalli',1000,2,2))
    print(get_estimated_price('Ejipura',1000,2,2))
