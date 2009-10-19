from Tkinter import *
import daqX as daq



class App():

    def __init__(self, master):
        
        device = daq.GetDeviceList()
        
        self.master = master
        deviceLabel = Label(master, text = "Availible Devices")
        deviceLabel.grid(row = 0, column = 0)
        self.v = StringVar()
        deviceRadio = Radiobutton(self.master, text = device, variable = self.v,
                                  value = device, command = self.radioDevice)
        deviceRadio.grid(row = 1, column = 0)

    def radioDevice(self):
        deviceName = self.v.get()
        self.device = daq.daqDevice(deviceName)

if __name__ == '__main__':
    
    root  = Tk()
    app = App(root)
    root.mainloop()
    
