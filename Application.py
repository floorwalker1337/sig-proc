import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.CreateWidgets()
    
    def CreateWidgets(self):
        # Create frames
        self.signalFrame = tk.Frame(background="bisque")
        self.signalFrame.pack(side="left")
        self.buttonFrame = tk.Frame(background="black")
        self.buttonFrame.pack(side="right")
        # SIGNAL WINDOWS
        self.TimeDomain = self.CreateSignalWindow("top")
        self.FreqDomain = self.CreateSignalWindow("bottom")
        # BUTTONS

        # Quit Button
        self.quit = tk.Button(self.buttonFrame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right")
    
    def CreateSignalWindow(self,windowSide):
        tFig = Figure(figsize=(5,5), dpi=100)
        tPlot = tFig.add_subplot(111)
        signalWindow = FigureCanvasTkAgg(tFig, master = self.signalFrame)
        signalWindow.draw()
        signalWindow.get_tk_widget().pack(side=windowSide, fill=tk.BOTH, expand=1)
        return signalWindow