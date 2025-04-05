# # Creating a series
import pandas as pd
import matplotlib.pyplot as plt
# colour_series = pd.Series(['red','blue','yellow'])
# # print(series)
# car_series = pd.Series(['Mustang','Ford','Ferrari'])


#Creating a dataframe
# car_colour = pd.DataFrame({"cars":car_series,"colour":colour_series})
# print(car_colour)

#importing data into a dataframe
car_sales = pd.read_csv("car-sales.csv")
#exporting csv to a new csv
# car_sales.to_csv("new-cars.csv")

#Info data
# print(car_sales.info())

#Create a series of different numbers and find the mean of them
mean_series = pd.Series([222,333,555,666,777])
#Find the length of a dataframe
#print(len(car_sales))

#showing the rows of dataframe
# print(car_sales.head())
# print(car_sales.head(7))
# print(car_sales.tail())
#using the loc function
# print(car_sales.loc[3])
# #using the iloc function
# print(car_sales.iloc[3])

#selecting odometer column from the database
# print(car_sales[car_sales["Odometer (KM)"]>100000]["Odometer (KM)"])
# cross = pd.crosstab(car_sales["Make"],car_sales["Doors"])
# print(cross)
#Creating a histogram of odometer
# plot = car_sales["Odometer (KM)"].hist()
# plt.show()
#converting the price into integer
# car_sales['Price'] = car_sales['Price'].replace('[\$\,\.]', '', regex=True).astype(int)
# car_sales["Price"] = car_sales["Price"]//100
# print(car_sales)

#converting make column into lowercase
# car_sales["Make"]=car_sales["Make"].str.lower()
# print(car_sales["Make"])
# print(car_sales)

missing_cars = pd.read_csv("car-sales-missing-data.csv")
odometer_mean = missing_cars["Odometer"].mean()
missing_cars["Odometer"].fillna(odometer_mean,inplace=True)
missing_cars.dropna(inplace=True)

#Adding Columns
seats_column = pd.Series([5,5,5,5,5])
missing_cars["Seats"] = seats_column
missing_cars["Seats"].fillna(5,inplace=True)

engine_size = [1.3,1.4,2.1,2.5,3.1,3.9]
missing_cars["Engine Size"] = engine_size


missing_cars['Price'] = missing_cars['Price'].replace('[\$\,\.]', '', regex=True).astype(int)


missing_cars["Price per km"] = missing_cars["Price"]/missing_cars["Odometer"]
missing_cars.drop("Price per km",axis=1,inplace=True)

shuffle = missing_cars.sample(frac=1)
shuffle.reset_index(drop = True,inplace=True)

missing_cars["Odometer"]=missing_cars["Odometer"].apply(lambda x:x/0.6)

missing_cars.rename(columns={"Odometer":"Odometer (M)"},inplace = True)
print(missing_cars)
