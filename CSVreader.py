while True:
    try:    
        import pandas as pd
        import time as tm
        import random as rn
    
        a: str = (input("Type your CSV name to read it, and exit by typing '0': "))

        if a=="0":
            print("Exiting CSVreader...")
            break
        elif a.lower()=="i":
            if __name__ == "__main__":

                print(f"\nCSVreader")
                print(f"MADE WITH PYTHON 3.11.4\nPandas version: {pd.__version__}\nBeing imported: No\nFile path: {__file__}\n")
            else:

                print(f"\nCSVreader")
                print(f"MADE WITH PYTHON 3.11.4\nPandas version: {pd.__version__}\nBeing imported: Yes\nFile path: {__file__}\n")
        else:
            d = str(input("Would you like the index numbers (y or n)?: "))
            b = pd.read_csv(a)
            if d.lower()=="y":
                print(f"{b}\n")
            elif d.lower()=="n":
                print(f"{b.to_string(index=False)}\n")
            else:
                print("Please try again. The reader will come back in 3 seconds.")
                tm.sleep(3)

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