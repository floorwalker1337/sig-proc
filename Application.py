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
        self.signalFrame = tk.Frame(width=385, height=800, background="bisque")
        self.signalFrame.pack(side="left")
        self.signalFrame.pack_propagate(0)
        self.buttonFrame = tk.Frame(background="black")
        self.buttonFrame.pack(side="right")
        # SIGNAL WINDOWS
        self.TimeDomain = self.CreateSignalCanvas(self.signalFrame,"top")
        self.FreqDomain = self.CreateSignalCanvas(self.signalFrame,"bottom")
        # BUTTONS

        # Quit Button
        self.quit = tk.Button(self.buttonFrame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right")
    
    def CreateSignalCanvas(self,frame,windowSide):
        tFig = Figure(figsize=(2,1), dpi=100)
        tPlot = tFig.add_subplot(111)
        signalCanvas = FigureCanvasTkAgg(tFig, master = frame)
        signalCanvas.draw()
        signalCanvas.get_tk_widget().pack(side=windowSide, fill=tk.BOTH, expand=1)
        return signalCanvas