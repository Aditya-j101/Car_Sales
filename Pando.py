import pandas as pd
import matplotlib.pyplot as plt
cars = pd.Series(['BMW','Hyundai','Mcclaren','Lamborghini','Toyota','Ford']) # 1 dimensional is called series
colours = pd.Series(['Blue','White','Red','Black','Yellow','Green'])
car_data = pd.DataFrame({"Car_makes":cars , "Colours":colours}) # 2 dimensional is called dataframe
car_sales = pd.read_csv('car-sales.csv')#.read_csv is use to read the csv files
#exporting a dataframe
# export = car_sales.to_csv("Export_sales.csv", index = False)
# exported = pd.read_csv('Export_sales.csv')
# print(exported)

#Describing data in Pandas
#Describing datatypes
# print(car_sales.dtypes)
#print(car_sales.columns)#returning the columns
#checking the index
# print(car_sales.index)

#describe
# print(car_sales.describe())

#returning info
# print(car_sales.info())

#returning mean
# print(car_sales.mean(numeric_only=True))

#Viewing and selecting data
# print(car_sales.head()) #print the top 5 columns of the dataframe unless no value added
# print(car_sales.tail()) #print the bottom 5 columns of the dataframe unless no value added

# print(car_sales.loc[5])
# print(car_sales.iloc[7])

# print(car_sales["Make"])
# print(car_sales["Colour"])
Toyota = car_sales[car_sales["Make"]=="Toyota"]

Odo = car_sales[car_sales["Odometer (KM)"]>100000]
#Aggregating to columns together
cross = pd.crosstab(car_sales["Make"] , car_sales["Doors"])
#groupby
group = car_sales.groupby(["Make"])[["Odometer (KM)","Doors"]].mean()
#plotting
# plot = car_sales["Odometer (KM)"].hist()
# plt.show() #make the graph 
#converting pandas string data into an integer
# car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '', regex=True).astype(int)
# plot2 = car_sales["Price"].plot()
# plt.show()

#Manipulating Data
car_sales["Make"]=car_sales["Make"].str.lower()
car_sales_missing = pd.read_csv("car-sales-missing-data.csv")
car_sales_missing.loc["Odometer"] = car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean())
car_sales_missing.dropna(inplace=True)
car_sales_missing = pd.read_csv("car-sales-missing-data.csv")

car_sales_missing_dropped = car_sales_missing.dropna()

seats_column = pd.Series([5,5,5,5,5])
car_sales["Seats"] = seats_column
car_sales["Seats"] = car_sales["Seats"].fillna(5)

fuel_economy = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
car_sales["Fuel per 100km"]=fuel_economy

car_sales["Total fuel used"] = car_sales["Odometer (KM)"]/100 * car_sales["Fuel per 100km"] #Column from another column
car_sales["Number of wheels"] = 4
car_sales["Road safety"] = True
car_sales = car_sales.drop("Total fuel used", axis=1)
car_sales["Onroad Price"] = car_sales["Price"]*2
car_sales = car_sales.drop("Onroad Price", axis = 1)

car_sales_shuffeled = car_sales.sample(frac=1.0)
car_sales_shuffeled = car_sales_shuffeled.reset_index(drop=True)

car_sales["Odometer (KM)"] = car_sales["Odometer (KM)"].apply(lambda x: x/1000)
# print(car_sales)
