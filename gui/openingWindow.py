import tkinter
from tkinter import filedialog
#import tkfiledialog

def main():

    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    print (in_path)

if __name__ == "__main__":
    main()