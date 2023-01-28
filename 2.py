import pandas as pd

def mapping_function(value1):
    df = pd.read_csv(r'D:\quiz\Embedded Software Engineer Quiz Resource - Sheet1.csv')
#print(df.iloc[:,0])

    column1 = df.iloc[:,0]
    column2 = df[df.columns[1]]

    condition = column1.isin([value1]).any().any()


    if condition :
        index = column1[column1==value1].index.values
        print(column2[index])

    else:
        print("No such value exists")

#print(column2)
value1 = input("Enter the value")
value1 = int(value1)

mapping_function(value1)


