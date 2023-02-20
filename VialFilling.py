import customtkinter, math, time
from pynput import mouse as pynputMouse
import pyautogui as mouse
from random import randrange
from pynput.keyboard import Key, Controller

class VialFilling(customtkinter.CTkToplevel):
    
    Banker_pos_x = 0
    Banker_pos_y = 0

    fountain_pos_x = 0
    fountain_pos_y = 0

    # how many items to clean
    Count = 0
    #how many items each times
    times = 0
    # how long the crafting takes
    FinishedDurations = 0
    Duration = 0
    # how many times the bot should run
    Rotations = 0
    # Enable or disable notifiactions 
    Notifiactions = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x500")
        self.title("Vial Filling")

        keyborad = Controller()
        self.keyboard = keyborad

        self.entry_count = customtkinter.CTkEntry(self, placeholder_text="x Items to clean")
        self.entry_count.pack(padx=10, pady=10)

        self.entry_times = customtkinter.CTkEntry(self, placeholder_text="How many items each time")
        self.entry_times.pack(padx=10, pady=10)

        self.entry_duration = customtkinter.CTkEntry(self, placeholder_text="length to craft (seconds)")
        self.entry_duration.pack(padx=10, pady=10)

        self.bank_pos_button = customtkinter.CTkButton(self, text="Bank position", command=self.change_bank_pos_label)
        self.bank_pos_button.pack(padx=10, pady=10)

        self.fill_vial_pos = customtkinter.CTkButton(self, text="Fill Vial position", command=self.change_fill_vial_pos_label)
        self.fill_vial_pos.pack(padx=10, pady=10)

        self.start_button = customtkinter.CTkButton(self, text="Start", command=self.start)
        self.start_button.pack(padx=10, pady=10)

        self.checkbox_notify = customtkinter.CTkCheckBox(self, text="notifications", command=self.notifyBox_event)
        self.checkbox_notify.pack(padx=10, pady=10)
        
        self.label_bank_pos = customtkinter.CTkLabel(self, text="X: 0 | Y: 0")
        self.label_bank_pos.pack(padx=10, pady=10)

        self.label_fill_vial_pos = customtkinter.CTkLabel(self, text="X: 0 | Y: 0")
        self.label_fill_vial_pos.pack(padx=10, pady=10)

        self.label_progress = customtkinter.CTkLabel(self, text="")
        self.label_progress.pack(padx=10, pady=10)

    #saving the pos
    def save_bank_pos(self, x, y, button, pressed):
        if button == pynputMouse.Button.left:  
            if pressed:
                self.Banker_pos_x = x
                self.Banker_pos_y = y
                return False
            
    #saving the pos
    def save_fountain_pos(self, x, y, button, pressed):
        if button == pynputMouse.Button.left:  
            if pressed:
                self.fountain_pos_x = x
                self.fountain_pos_y = y
                return False
            

     # banker pos callback
    def startMousePos_Bank(self):
        listener = pynputMouse.Listener(on_click=self.save_bank_pos)
        listener.start()
        listener.join()

     # fountain pos callback
    def startMousePos_fountain(self):
        listener = pynputMouse.Listener(on_click=self.save_fountain_pos)
        listener.start()
        listener.join()

    def change_bank_pos_label(self):
        self.startMousePos_Bank()
        self.label_bank_pos.configure(text="X: " +str(self.Banker_pos_x) + " | Y:" + str(self.Banker_pos_y))


    def change_fill_vial_pos_label(self):
        self.startMousePos_fountain()
        self.label_fill_vial_pos.configure(text="X: " +str(self.fountain_pos_x) + " | Y:" + str(self.fountain_pos_y))


        # toggles notifications value
    def notifyBox_event(self):
        self.Notifiactions ^= 1

    def UpdateProgress(self):
        self.label_progress.configure(text= str(self.FinishedDurations) + " / " + str(self.Rotations))

    # rotation calculation
    def CalculateRotation(self):
        RotationCount = self.Count / self.times
        self.Rotations = math.ceil(RotationCount)

    def saveValues(self):
        self.Count = int(self.entry_count.get())
        self.times = int(self.entry_times.get())
        self.Duration = int(self.entry_duration.get())

        self.CalculateRotation()
        self.UpdateProgress()


    def OnAction(self):
        for x in range(self.Rotations):
            self.FinishedDurations = x + 1
            self.UpdateProgress()
            self.update()
            time.sleep(5)
            mouse.moveTo(self.Banker_pos_x, self.Banker_pos_y)
            mouse.click()
            time.sleep(5)
            self.keyboard.press(Key.f3)
            self.keyboard.release(Key.f3)
            time.sleep(5)

            # move to 
            mouse.moveTo(self.fountain_pos_x, self.fountain_pos_y)
            mouse.click()
            time.sleep(8)
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
            time.sleep(self.Duration) 

            if x >= self.Rotations:
                print("finished")


    def start(self):
        self.saveValues()
        self.OnAction()
