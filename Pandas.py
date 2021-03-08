import pandas as pd
import numpy as np

#Loading data

dataFrameCSV = pd.read_csv('pokemon_data.csv') #read_csv loads data from a csv file
dataFrameXLSX = pd.read_excel('pokemon_data.xlsx') #read_csv loads data from a xlsx(excel) file
dataFrameTXT = pd.read_csv('pokemon_data.txt', delimiter='\t') #read_csv loads data from a txt file but it needs a delimiter to identify where to separate each block of data
# print(dataFrameCSV.head(5)) #See the top 5 rows
# print(dataFrameTXT.tail(5)) #See bottom 5 rows

#Reading data

# print(dataFrameCSV.columns) #Read Headers
# print(dataFrameCSV['Name']) #Read each Column
# print(dataFrameCSV[['Name', 'Type 1', 'Legendary']]) #Read specific Columns
# print(dataFrameCSV.iloc[0]) #Read a row as a table
# print(dataFrameCSV.iloc[2,1]) #Read a specific location
# print(dataFrameCSV.loc[dataFrameCSV['Type 1'] == "Water"]) #Read elements based on criteria
# print(dataFrameCSV.describe()) # Read all rows and returns information
# print(dataFrameCSV.sort_values('Name')) #Read sorted values

for index, row in dataFrameCSV.iterrows(): #This will iterate through every single row
    break

#Altering data

dataFrameCSV['Total Stats'] = dataFrameCSV['HP'] + dataFrameCSV['Attack'] + dataFrameCSV['Defense'] + dataFrameCSV['Sp. Atk'] + dataFrameCSV['Sp. Def'] + dataFrameCSV['Speed'] #This will add to the table another column called Total Stats
dataFrameCSV = dataFrameCSV.drop(columns=['Total Stats']) #Drops a column
dataFrameCSV['Total Stats'] = dataFrameCSV.iloc[:, 4:10].sum(axis = 1) #This also adds a column

cols = list(dataFrameCSV.columns.values) #Creates a list with the values of the columns
dataFrameCSV = dataFrameCSV[cols[0:4] + [cols[-1]] + cols[4:12]] #Moves a column around the table

#Saving data

# dataFrameCSV.to_csv('modified_table.csv') #Export values from table to a csv file
# dataFrameCSV.to_csv('modified_table.csv', index = False) #Export values from table to a csv file without index
# dataFrameCSV.to_excel('modified_table.xlsx', index = False) #Export values from table to a xlxs file without index
# dataFrameCSV.to_csv('modified_table.txt', index = False, sep='\t') #Export values from table to a txt file without index and separated by tabs

#Filtering data

# print(dataFrameCSV.loc[dataFrameCSV['Type 1'] == 'Fire']) #This will filter all rows without type 1 = Fire
# print(dataFrameCSV.loc[(dataFrameCSV['Type 1'] == 'Fire') | (dataFrameCSV['Type 2'] == 'Fire')]) #This will filter all rows don't that have the primary or secondary type as Fire
# print(dataFrameCSV.loc[dataFrameCSV['Name'].str.contains('Mega')]) #This will filter all the rows that don't contain Mega in the name
# print(dataFrameCSV.loc[~dataFrameCSV['Name'].str.contains('Mega')]) #The ~ symbol functions as the NOT statement
# dataFrameCSV = dataFrameCSV.reset_index() #This will reset the indexing of your dataframe

#Conditional Changes

# dataFrameCSV.loc[(dataFrameCSV['Type 1'] == 'Grass') | (dataFrameCSV['Type 2'] == 'Grass'), 'Type 1'] = 'Plant' #This will change the type to Plant where it's Grass

#Aggregate Statistics(Groupby)

# dataFrameCSV = pd.read_csv('modified_table.csv')
# print(dataFrameCSV.groupby(['Type 1']).mean()) #This will look for the averages of each row, sorted by Type 1)
# print(dataFrameCSV.groupby(['Type 1']).mean().sort_values('Sp. Atk', ascending=False)) #This will look for the averages of each row, sorted by the Type 1 with the higher value )
# print(dataFrameCSV.groupby(['Type 1']).count()) #This will count the number of rows which have same Type 1
# dataFrameCSV['count'] = 1
# print(dataFrameCSV.groupby(['Type 1', 'Type 2']).count()['count']) #This will count the number of rows with the same Type 1, and same Type 2


#Working with large amounts of data
# for dataFrame in pd.read_csv('modified_table.csv', chunksize = 5): #Chunksize refers to the number of rows loaded at the time
    # print('DATAFRAME CHUNK')
    # print(dataFrame) 
    #This will print many smaller dataframes(5 rows long), of the whole modified_table.csv dataframe

# newDataFrame = pd.DataFrame(columns=dataFrameCSV.columns) #Creates a new dataframe with the same columns
# for dataFrame in pd.read_csv('modified_table.csv', chunksize = 5): #Chunksize refers to the number of rows loaded at the time
    # typeCount = dataFrame.groupby(['Type 1']).count() #This will store the number of rows which have the same Type 1 in results
    # newDataFrame = pd.concat([newDataFrame, typeCount])
    #Now newDataFrame will have only the fraction of information we need from dataFrameCSV
# print(newDataFrame)


 #Getting Water pokemons on a single DataFrame
waterType1 = dataFrameCSV[dataFrameCSV['Type 1'] == 'Water']
waterType2 = dataFrameCSV[dataFrameCSV['Type 2'] == 'Water']
waterTypes = pd.concat((waterType1, waterType2))


#Seeing if speedy pokemons are getting more speedy by generation
allPokesSpeed = dataFrameCSV[dataFrameCSV['Speed'] >= 0]
#print(allPokesSpeed.groupby(['Generation']).mean()[['Speed']]) #This will give the speed average, but there are also very slow pokemons being released with each generation, and I want to know if the speed on fast pokemon is being increased. And fast pokemon will be any pokemon with speed above average
#print(allPokesSpeed.groupby(['Generation']).mean()['Speed'].sum()/allPokesSpeed['Generation'].max()) #This will create the total speed average between generations
#speedyPokes = dataFrameCSV[dataFrameCSV['Speed'] >= 67.86288555805882]
#print(speedyPokes.groupby(['Generation']).mean()[['Speed']])

#Pivoting a DataFrame 
groupedPokemon = dataFrameCSV.groupby(['Generation', 'Type 1']).mean()['Attack']
#print(groupedPokemon.unstack())

groupedPokemon = dataFrameCSV.groupby(['Generation', 'Type 1']).mean()['Attack'].reset_index()
#print(groupedPokemon.pivot(index='Generation', columns='Type 1', values='Attack'))

groupedPokemon = dataFrameCSV.pivot_table(index='Generation', columns='Type 1', values='Attack', aggfunc=np.mean)
#print(groupedPokemon)

#Crosstab
#How many pokemon type combinations are there?
#print(pd.crosstab(dataFrameCSV['Type 1'], dataFrameCSV['Type 2']))

#Cleaning Data

# Since some generations don't have pokemons of all types, some values are null.
pokeAtkAvg = groupedPokemon[pd.notnull(groupedPokemon)]
pokeAtkAvg = pokeAtkAvg.fillna('No pokes') #fillna will replace null values with 'No pokes'.
print(pokeAtkAvg.sum())