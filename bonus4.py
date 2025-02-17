filenames = ["1.raw data.txt" , "2.reports.txt" , "3.presentation.txt"]

for filename in filenames:
    filename = filename.replace('.' , '_' , 1)
    print(filename)