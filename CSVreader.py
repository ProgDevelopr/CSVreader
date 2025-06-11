while True:
    try:    
        import pandas as pd
        import time as tm
        import random as rn
    
        a = str(input("Type your CSV name to read it (example: file.csv) and exit by typing '0': "))

        if a=="0":
            print("Exiting CSVreader...")
            LeavingTime = [0.8,2.1,1.3,5.3,4.3]
            c = rn.choice(LeavingTime)
            tm.sleep(c)
            break
        else:
            d = str(input("Would you like the index numbers(y or n)?: "))
            b = pd.read_csv(a)
            print(b)
            if d=="n" or d=="N" or d=="no":
                print(b.to_string(index=False))

    except FileNotFoundError:
        print("Sorry, but your CSV file was not found. Please try again. The reader will come back in 5 seconds.")
        tm.sleep(5)
    except pd.errors.EmptyDataError:
        print("Sorry, but check your CSV again. It might be empty. The reader will come back in 5 seconds.")
        tm.sleep(5)
    except pd.errors.ParserError:
        print("Sorry, but your CSV file doesn't have the structure of a CSV (Rows and Columns). The reader will come back in 5 seconds.")
        tm.sleep(5)
    except TypeError:
        print("Sorry, we encountered a TypeError. Please check your CSV again. The reader will come back in 5 seconds.")
        tm.sleep(5)