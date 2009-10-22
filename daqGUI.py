from Tkinter import *
import daqX as daq


class App():

    def __init__(self, master):

        self.master = master
        master.title("PyDaqBoard")

        self.menuCreation()

    def menuCreation(self):

        menubar = Menu(self.master)
        
        filemenu = Menu(menubar)
        menubar.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='DAQ Device', command=self.chooseDevice)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.exitProgram)
        
        self.master.config(menu=menubar)
        
    def exitProgram(self):
        self.master.quit()
        self.master.destroy()

    def chooseDevice(self):
        window = ChooseDeviceWindow()
        window
        
        
class ChooseDeviceWindow():

        
    def __init__(self):
        
        self.exists = True
        self.master = Toplevel()
        self.master.title("Choose DAQ Device")
        
        devices = daq.GetDeviceList()
        
        deviceLabel = Label(self.master, text="Availible Devices")
        deviceLabel.grid(row=0, column=0)
        
        self.devicebox = Listbox(self.master)
        self.devicebox.grid(row=1, column=0)
        
        for item in devices:
            self.devicebox.insert(END, item)

        selectButton = Button(self.master, text="Select", command=self.setDevice)
        selectButton.grid(row=1,column=1)

    def __del__(self):
        return self.curdevice

    def setDevice(self):
        devindex = self.devicebox.curselection()
        self.curdevice = self.devicebox.get(devindex)
        self.exists = False
        self.master.destroy()
        
        

if __name__ == '__main__':
    
    root = Tk()
    app = App(root)
    root.mainloop()
    
