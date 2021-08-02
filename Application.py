import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

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
        self.Buttons = {
            "OpenButton": tk.Button(self.master,text="Open CSV", 
                                    command=self.OpenFile),
            "QuitButton": tk.Button(self.master, text="QUIT", fg="red",
                                    command=self.master.destroy)
        }
        # Button layout
        n=0
        for button in self.Buttons:
            self.Buttons[button].grid(row=n,column=1)
            n+=1

        # SIGNAL WINDOWS
        self.CreateSignalCanvas()

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
    
    def CreateSignalCanvas(self):
        self.signalFigure, [self.timeAx, self.freqAx] = plt.subplots(2,1)
        self.timeAx.cla()
        self.freqAx.cla()
        # Set labels
        self.timeAx.set_xlabel("Number of Samples")
        self.freqAx.set_xlabel("Frequency (Hz)")

        # Arrange and show
        self.signalFigure.tight_layout()
        self.signalCanvas = FigureCanvasTkAgg(self.signalFigure, self.master)
        self.signalCanvas.get_tk_widget().grid(row=0,column=0,rowspan=len(self.Buttons))

    def OpenFile(self):
        pass

    def PlotData(self, data):
        pass