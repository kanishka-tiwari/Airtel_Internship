import numpy as np
import pandas as pd

#data that should exist
required_data = {
    'Alphabets': ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    'IDs': ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
}
df_required = pd.DataFrame(required_data)

print("Alphabets expected in database:")
print(df_required.to_string(index=False))

user_raw = input("\nEnter the alphabets (separated by commas): ")                       #user input

user_items = [item.strip() for item in user_raw.split(',')]                             #put commas and remove extra spaces

required_array = df_required['Alphabets'].values                                        #convert alphabets column into numpy array

missing_ids = np.setdiff1d(required_array, user_items)                                  #find items not entered by user using setdiff1d

if len(missing_ids) == 0:
    print("No data missing")
else:
    print(f"Data not included: {len(missing_ids)}")
    
    df_missing = df_required[df_required['IDs'].isin(missing_ids)]                      #use panda to filter missing alphabets
    print("\n Missing data:")
    print(df_missing.to_string(index=False))