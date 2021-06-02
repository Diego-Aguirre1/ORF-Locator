import tkinter as tk
from tkinter import *
from tkinter import filedialog
import getpass

global opened_file
global frames_number

root = Tk()
user = getpass.getuser()
# set window size
root.geometry("650x400")

# set window title
root.title("Open Reading Frame Locator")

# preview text box to show the contents of the file
preview = tk.Text(root, height=12)
preview.grid(column=0, row=0, sticky='nsew')

# results text box
results = tk.Text(root, height=5)
results.grid(column=0, row=13, sticky='nsew')

# DNA frames
FRAMES = [1, 2, 3]
var = StringVar(root)
# sets option to the first index (frame 1)
var.set(FRAMES[0])

def redirector(output):
    results.insert(INSERT, output)
    
def open_file():
    global opened_file
    global frames_number
    frames_number = var.get()
    frame = int(frames_number)
    
    type = (
    ("FASTA", "*.FASTA"),
    ("All files", "*.*")
    )
    # open file dialog
    sequence = filedialog.askopenfile(
        initialdir='C:/Users/%s/Documents' %user, 
        title="Select a file",
        filetypes=type
        )
    
    opened_file = sequence
    
    # read contents of the file to preview text window
    preview.insert('1.0', opened_file.readlines())
    



def findORF(file, frame):

    comment = file.readline()
    DNA_sequence = file.read().upper().replace('\n','')
    seq_length = len(DNA_sequence)
    
    longestORF = 0
    count = 0
    openframe = False
    
    for nucleotide in range(frame, seq_length, 3):
        triplet = DNA_sequence[nucleotide: nucleotide + 3]
        if triplet == "ATG" and not openframe:
            openframe = True
            start = nucleotide + 1
            count = 1
        elif triplet in ["TAG", "TGA", "TAA"]:
            count += 1
            if openframe == True:
                stop = nucleotide + 3
                codon = (stop-start+1)//3
                if codon >= 30:
                    redirector((
                        start, "..",
                        stop, "..",
                        codon, "codons ..",
                        "length in nucleotides =",
                        stop-start+1)
                        )
                    if count > longestORF:
                        longestORF = count
                        startORF = start
                        stopORF = stop
                openframe = False
            count = 0
        else:
            if openframe == True:
                count += 1

def submit():
    global opened_file
    global frames_number
    frames_number = int(var.get())
    findORF(opened_file, frames_number)
    results.insert(INSERT, opened_file.readlines())

# Open File Button
open_button = Button(root, text="Open a File", command=open_file)
open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)
# Submit Button
submit_file = Button(root, text="Submit", command=submit)
submit_file.grid(column=0, row=1, sticky='w', padx=100, pady=10)
# DNA Frames Options
frame_options = OptionMenu(root, var, *FRAMES)
frame_options.grid(column=0, row=1, sticky='w', padx=190, pady=10)

root.mainloop()

