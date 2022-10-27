import pickle

def model_prediction(features):
    pickled_model = pickle.load(open('model/TSLA_stock_prediction.pkl', 'rb'))
    stock_price = float(pickled_model.predict(features))
    
    return stock_price
  
test_features = [[17.114,17.344667,75346500]] #Passed in the order 'Open','Close','Volume'

print(f'The stock price the next day will be ${model_prediction(test_feature)}')
