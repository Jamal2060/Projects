import tkinter as tk

import customtkinter
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)

        # Creat window title and dimension
        self.geometry("800x700")
        self.title("Unit Converter")

        # Create a topbar frame
        self.topbar_frame = ctk.CTkFrame(self, width=800, height=60, corner_radius=0, border_width=2,)
        self.topbar_frame.grid(row=0, column=10, rowspan=4, sticky="n")
        self.topbar_frame.grid_rowconfigure(4, weight=1)

        # Create a custom label on the sidebar
        self.logo_label = ctk.CTkLabel(self.topbar_frame, text="Unit Converter", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=329, pady=10)

        # Creating tabview
        self.tabview = customtkinter.CTkTabview(self, width=800,
                                                segmented_button_selected_color="orange",
                                                text_color="black")
        self.tabview.grid_columnconfigure(0, weight=1,minsize=100)
        self.tabview.grid(row=4, column=10, padx=2, pady=20, sticky="n")
        self.tabview.add("Length Converter")
        self.tabview.add("Area Converter")
        self.tabview.add("Volume Converter")
        self.tabview.add("Mass/Weight Converter")
        self.tabview.add("Time Converter")
        self.tabview.add("Temperature Converter")
        self.tabview.tab("Length Converter").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Area Converter").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Volume Converter").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Mass/Weight Converter").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Time Converter").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Temperature Converter").grid_columnconfigure(0, weight=1)

        self.from_label = ctk.CTkLabel(self.tabview.tab("Length Converter"), text="From:",
                                       font=ctk.CTkFont(size=14, weight="bold"),)
        self.from_label.grid(row=0, column=0, padx=2, pady=20, sticky="n")


# Executing the main window
if __name__ == "__main__":
    app = App()
    app.mainloop()
