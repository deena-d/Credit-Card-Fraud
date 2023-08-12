
import numpy as np
import pickle

#loading model
loaded_model = pickle.load(open('D:/web_app/trained.sav','rb'))

input_data= (0,-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,149.62)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)


prediction = loaded_model.predict(input_data_reshaped)

print(prediction)


if (prediction [0]== 0):
  print("Normal Transaction")
else:
  print("fraudulent transaction")
  