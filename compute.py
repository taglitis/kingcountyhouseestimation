from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
import pickle
import pandas as pd


def compute(bedrooms, sqft_living,  waterfront,
            view,  grade,  yob , zipcode):

    features_dict = {}
    features_dict['price'] = 0
    features_dict['bedrooms'] = bedrooms
    #features_dict['bathroms'] = bathrooms
    features_dict['sqft_living'] = sqft_living
    #features_dict['sqft_lot'] = sqft_lot
    #features_dict['floors'] = floors
    features_dict['waterfront'] = waterfront
    features_dict['view'] = view
    #features_dict['condition'] = condition
    features_dict['grade'] = grade
    #features_dict['sqft_basement'] = sqft_basement
    features_dict['n_years_built_ago'] = 2015 - yob
    columns_zipcode = ['98001', '98002', '98003', '98004', '98005',
       '98006', '98007', '98008', '98010', '98011', '98014', '98019', '98022',
       '98023', '98024', '98027', '98028', '98029', '98030', '98031', '98032',
       '98033', '98034', '98038', '98039', '98040', '98042', '98045', '98052',
       '98053', '98055', '98056', '98058', '98059', '98065', '98070', '98072',
       '98074', '98075', '98077', '98092', '98102', '98103', '98105', '98106',
       '98107', '98108', '98109', '98112', '98115', '98116', '98117', '98118',
       '98119', '98122', '98125', '98126', '98133', '98136', '98144', '98146',
       '98148', '98155', '98166', '98168', '98177', '98178', '98188', '98198',
       '98199']


    for i in columns_zipcode:
        features_dict[i] = 0
    features_dict[zipcode] = 1


    filename_scaler = '/home/taglitis/mysite/model_scaler.sav'
    filename_model = '/home/taglitis/mysite/finalized_model.sav'
    loaded_model = pickle.load(open(filename_model, 'rb'))
    loaded_scaler = pickle.load(open(filename_scaler, 'rb'))

    df_estimate = pd.DataFrame(features_dict, index=[0])
    print('\n\n df_estimate size ', df_estimate, '\n\n')
    df_estimate_norm = loaded_scaler.transform(df_estimate)
    df_estimate_norm = pd.DataFrame(df_estimate_norm, index=[0], columns= df_estimate.columns)
    y_pred_norm = loaded_model.predict(df_estimate_norm.loc[:,'bedrooms':])
    df_estimate_norm.loc[0,'price'] = y_pred_norm.tolist()[0]
    results = pd.DataFrame(data = loaded_scaler.inverse_transform(df_estimate_norm), columns = df_estimate_norm.columns)
    estimated_price = results.loc[0,'price']

    df = pd.read_csv('/home/taglitis/mysite/kc_house_data.csv', dtype = {'id':str, 'price':float, 'bedrooms':str, 'bathrooms':str, 'sqft_living':str,
                                                  'sqft_lot':str, 'floors':str, 'waterfront':str, 'view':str, 'condition':str,
                                                  'grade':str, 'sqft_above':str,  'sqft_basement':str,  'yr_built':str ,
                                                  'yr_renovated':str, 'zipcode':str, 'lat':str, 'long':str,
                                                  'sqft_living15':float, 'sqft_lot15':float})

    estimated_price_precent =  estimated_price*0.2

    df = df[df.zipcode == zipcode]
    df = df[(df.price >= estimated_price-estimated_price_precent)&(df.price <= estimated_price+estimated_price_precent)]

    #df.date = pd.to_datetime(df.date).strptime('%d-%m-%Y')
    df.date = pd.to_datetime(df.date).dt.strftime('%d-%m-%Y')

    df = df.drop(columns=['lat', 'long', 'sqft_lot15', 'sqft_living15', 'yr_renovated',
                          'sqft_lot', 'floors', 'sqft_above', 'condition', 'sqft_basement',
                          'bathrooms'])
    df.price = df.price.astype(int)
    df = df.loc[:,['id', 'date', 'bedrooms', 'sqft_living','waterfront', 'view', 'grade','yr_built', 'zipcode', 'price']]
    df.waterfront = df.waterfront.map({"0":"No", '1':'Yes'})
    df.rename(columns = {'id':'ID', 'date':'Date', 'bedrooms':'Number of Bedrooms', 'sqft_living': 'Living Area, sqft', 'grade':'Grade',
                         'yr_built':"Year of Build", "zipcode":"Zipcode", 'price':'Price', "waterfront":"Waterfront view", 'view':"View from Property"}, inplace = True)

    return estimated_price, df

if __name__ == '__main__':
    bedrooms = 3
    #bathrooms = 3
    sqft_living = 1500
    #sqft_lot = 1500
    #floors = 2
    waterfront = 1
    view = 3
    #condition = 3
    grade = 5
    #sqft_basement = 0
    yob = 2000
    zipcode = str(98119)
    print(compute(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront,
                view, condition, grade, sqft_basement, yob, zipcode))
