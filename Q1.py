import pandas as pd
# enter the location where you have saved cars93.csv instead of this "Cars93.csv" if it does not work
car = pd.read_csv(r"Cars93.csv") #reading the csv file

# 1.(i)
# Model -----> nominal
# Type  -----> ordinal
# Max.Price -> interval scale
# AirBag ----> ordinal



# 1.(ii)
null = car.isnull() # finding in which column theree is null,na
printing_null = car.loc[:,car.isnull().any()].columns # printing the null columns
print(printing_null)

car_drop_NA = car.dropna(axis=1)
car_df = car.drop(["Rear.seat.room","Luggage.room"],axis=1)
print(car_df.info)
car_fillna = car_df.fillna(0)#replacing null with 0
print(car_fillna) #printing the updated file

print(car_fillna.loc[:,car_fillna.isnull().any()].columns)# checking wheteher any null is left



# 1.(iii)
#noise reduction using average method
def noise_reduction(x):
    list=[]
    for i in range(len(x)):
        list.append(x[i:i + 3] / 3)# averaging the value for reducing noise
        return list
    print(list)

df = pd.read_csv(r"Cars93.csv", usecols=['Price'])
print(df)
noise_reduction(df)



#1.(iv)
from sklearn.preprocessing import LabelEncoder
def encoding(x):
    label_encoder = LabelEncoder()
    s = label_encoder.fit_transform(car[x]) # label encoding each of the car columns
    t = {index: label for index, label in enumerate(label_encoder.classes_)}
    return t

# Taking all the catageries in cars93
car_columns = car.select_dtypes(include='object').columns # encoding labels to different catageries in car93
x = [j for j in car_columns]
for i in x:
    print('Encoded data :\n',encoding(i))



# 1.(v)
#normalising the function



# 1.(vi)
# random split of data into train
from sklearn.model_selection import train_test_split
X = car.iloc[:, 3]
Y = car.iloc[:, 2]

