import numpy as np

class SignalData():
    def __init__(self,timeData):
        if type(timeData)==np.ndarray:
            self.timeData=timeData
        else:
            print("Incoming data is not an ndarray.")
            return
    
    def SetTimeData(self,newTimeData):
        self.timeData=newTimeData
    
    def TakeFFT(self,timeData):
        self.freqData=np.fft.fft(timeData)
    
    def TakeIFFT(self,freqData):
        pass