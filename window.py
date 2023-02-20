import customtkinter
from HerbCleaning import HerbWindow
from VialFilling import VialFilling

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("250x200")
        self.title("Runescape-Bot")
        self._set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.button_cleanHerbs = customtkinter.CTkButton(master=self, text="Clean herbs", command=self.open_CleanHerbs)
        self.button_cleanHerbs.pack(padx=10, pady=10)

        self.button_FillVials = customtkinter.CTkButton(self, text="Fill Vials", command=self.open_Vial)
        self.button_FillVials.pack(padx= 10, pady = 10)

        self.toplevel_window = None


    def open_CleanHerbs(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = HerbWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


    def open_Vial(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = VialFilling(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
            
    def open_Settings(self):
        pass

