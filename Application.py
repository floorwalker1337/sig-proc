import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.signalCanvas=None
        self.CreateToolBar()
        self.CreateWidgets()
    
    def CreateToolBar(self):
        # Toolbar
        self.toolbar=tk.Menu()
        self.config(menu=self.toolbar)

        self.fileMenu=tk.Menu(self.toolbar)
        self.runMenu=tk.Menu(self.toolbar)
        self.toolbar.add_cascade(label="File",menu=self.fileMenu)

        # File menu options
        self.fileMenu.add_command(label="Open...",command=self.OpenFile)
        self.fileMenu.add_command(label="Exit",command=self.OnQuit)

    def CreateWidgets(self):
        # Create frames
        self.signalFrame=tk.Frame(width=385, height=800, background="bisque")
        self.signalFrame.grid(column=0,columnspan=3,row=0,rowspan=5)
        self.buttonFrame=tk.Frame(background="black")
        self.buttonFrame.grid(column=4,row=0,rowspan=5)
        # BUTTONS
        self.Buttons = {
            "OpenButton": tk.Button(self.buttonFrame,text="Open CSV", 
                                    command=self.OpenFile),
            "QuitButton": tk.Button(self.buttonFrame, text="QUIT", fg="red",
                                    command=self.OnQuit)
        }
        # Button layout
        n=0
        for button in self.Buttons:
            self.Buttons[button].grid(row=n,column=1)
            n+=1
        # SIGNAL WINDOWS
        self.TimeDomain = self.CreateSignalCanvas(self.signalFrame)
        self.FreqDomain = self.CreateSignalCanvas(self.signalFrame)
    
    def CreateSignalCanvas(self,frame):
        # Figure that will contain the plot along with axes
        self.signalFigure, [timeAx,freqAx]=plt.subplots(2,1)
        timeAx.cla()
        freqAx.cla()
        # Set labels
        timeAx.set_xlabel("Number of Samples")
        freqAx.set_xlabel("Frequency (Hz)")
        # Arrange
        self.signalFigure.tight_layout()
        # Creating Tkinter canvas containing the figure
        self.signalCanvas=FigureCanvasTkAgg(self.signalFigure, master=frame)
        self.signalCanvas.draw()
        self.signalCanvas.get_tk_widget().grid(row=0,column=0,rowspan=len(self.Buttons))

    def OnQuit(self):
        self.destroy()
        exit()
    
    def OpenFile(self):
        pass

    def PlotData(self, data):
        pass

    def Filter(self):
        pass