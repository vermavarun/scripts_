## Owner vermavarun. Python Script to convert Parquet File To CSV
import os
import pandas as pd
# assign directory
directory = '.\\TestFiles\\'
error = 0
success = 0


if not os.path.exists(directory+"CSV"):
    os.makedirs(directory+"CSV")

outputFile = open(directory+"CSV\\outputOfConversionCSV.txt", 'a')

# iterate over files in
# that directory
for filename in os.listdir(directory):
    try:
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            outputFile.write("\n"+f)
            df = pd.read_parquet(f)
            df.to_csv(directory+"CSV\\" + filename + ".csv")
            success = success + 1
    except Exception as e:
        print("ERROR in file: " + f)
        outputFile.write("\nERROR in file: " + f)
        error = error + 1
        print(e)
        outputFile.write("\n"+e)

print("Total Success: " + str(success))
outputFile.write("\nTotal Success: " + str(success))
print("Total Errors: " + str(error))
outputFile.write("\nTotal Errors: " + str(error))
outputFile.close()
