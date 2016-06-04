import Tkinter as tk
import string, tkMessageBox
from datetime import date

class ChristmasRotation(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        
        self.families = ['Family1', 'Family2']
        
        label1 = tk.Label(self,
            text = 'Select family and enter desired year below -- ' +
                'use only 4 digit years')
        label1.grid(column = 0, row = 0, columnspan = 2)
        
        self.listbox = tk.Listbox(self, height = len(self.families), width = 10)
        self.listbox.grid(column = 0, row = 1)
        for i in range(len(self.families)):
            self.listbox.insert(i + 1, self.families[i])
            
        self.entryVariable = tk.IntVar()        
        self.entry = tk.Entry(self, textvariable = self.entryVariable)
        self.entry.grid(column = 1, row = 1)
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(date.today().year)
    
        button = tk.Button(self, text = 'See Rotation', 
            command = self.OnButtonClick)
        button.grid(column = 0, row = 2, columnspan = 2)
        
        self.frame = tk.Frame(self)
        self.frame.grid(column = 0, row = 3, columnspan = 2, sticky = 'EW')
	    
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
        
    #def OnPressEnter(self, event):
    #   '''
    #   Initiates program
    #   '''
    #    self.Run()
        
    def OnButtonClick(self):
        '''
        Initiates program
        '''
        self.Run()
        
    def Run(self):
        '''
        Determines family and base year
        Initiates calcuation of rotation information
        '''
        for w in self.frame.winfo_children():
            w.destroy()
        if len(self.listbox.curselection()) == 0:
            tkMessageBox.showerror(title = 'Error!', message = 'Select a family')            
        famIndex = int(self.listbox.curselection()[0])
        if famIndex == 0:
            baseYear = 2010
        else:
            baseYear = 2008
        self.givers = self.loadNames(self.families[famIndex] + '.txt')
        
        self.namelist = list(self.givers)
        year = self.entryVariable.get()
        self.receivers = self.getRotation(self.namelist, year, baseYear)
        
        t = tk.Label(self.frame, text = 'Giver: ', anchor = 'w')
        t.grid(column = 0, row = 0, sticky = 'EW')
        for i in range(len(self.givers)):
            t = tk.Label(self.frame, text = self.givers[i], anchor = 'w')
            t.grid(column = 0, row = (1 + i), sticky = 'EW')
        
        t = tk.Label(self.frame, text = 'Receiver: ', anchor = 'w')
        t.grid(column = 1, row = 0, sticky = 'EW')
        for i in range(len(self.givers)):
            t = tk.Label(self.frame, text = self.receivers[i], anchor = 'w')
            t.grid(column = 1, row = (1 + i), sticky = 'EW')
    
    def loadNames(self, filename):
        """
        filename: a file listing names in the family. Names should be listed 
        in order of birth -- oldest to youngest.
        returns: list of names
        """
        # inFile: file
        inFile = open(filename, 'r', 0)
        # line: string
        line = inFile.readline()
        # namelist: list of strings
        namelist = string.split(line)
        return namelist
    
    def rotate(self, namelist):
        """
        namelist: the list of family names
        returns: the list of names, rotated once.
        """
        moveName = namelist.pop(0)
        namelist.insert(len(namelist), moveName)
        return namelist
        
    def getRotation(self, namelist, year, baseYear):
        """
        namelist: the list of family names
        year: the year of gift exchange
        baseYear: the year the gift exchange began
        returns: the list of receivers
        """
        numRotate = (year - baseYear)%(len(namelist) - 1) + 1
        for i in range(numRotate):
            self.rotate(namelist)
            if namelist == self.givers:
                self.rotate(namelist)
        return namelist
       
if __name__ == '__main__':
    app = ChristmasRotation(None)
    app.title('Christmas Rotation Calculator')
    app.mainloop()            
                                                
