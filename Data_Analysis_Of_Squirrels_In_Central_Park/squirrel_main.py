import pandas

census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrelsColor = census_data["Primary Fur Color"]

redSquirrels = len(census_data[census_data["Primary Fur Color"] == 'Cinnamon'])

graySquirrels = len(census_data[census_data["Primary Fur Color"] == 'Gray'])

blackSquirrels = len(census_data[census_data["Primary Fur Color"] == 'Black'])

data_dict = {
    "Squirrels Fur Color": ["Gray", "Red", "Black"],
    "Squirrels Count": [graySquirrels, redSquirrels, blackSquirrels]
}

newData = pandas.DataFrame(data_dict)
newData.to_csv("squirrels_count_by_color.csv")
