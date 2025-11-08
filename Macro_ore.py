    
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 10:26:27 2025
@author: theop
Prospecting Ore (Roblox Game) macro 
"""

import pydirectinput
import time
import tkinter as tk
from tkinter import messagebox

class ProspectingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("450x300")
        self.root.title("Prospecting Menu")
        self.root.resizable(False, False)
        
        # Variable to store the number of hits (clicks)
        self.valeur_totem = tk.IntVar(value="")
        # Variable to store the shovel filling duration (mouse hold time)
        self.duree_remplissage = tk.DoubleVar(value="")
        self.is_running = False
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title label
        titre = tk.Label(self.root, text="Prospecting Configuration", 
                        font=("Arial", 16, "bold"), fg="#2c3e50")
        titre.pack(pady=15)
        
        # Frame for number of hits input
        frame_hits = tk.Frame(self.root)
        frame_hits.pack(pady=10)
        
        label_hits = tk.Label(frame_hits, text="Number of hits (to fill your pan):", 
                              font=("Arial", 11))
        label_hits.grid(row=0, column=0, padx=5)
        
        self.entry_hits = tk.Entry(frame_hits, textvariable=self.valeur_totem, 
                                   width=8, font=("Arial", 11))
        self.entry_hits.grid(row=0, column=1, padx=5)
        
        # Frame for shovel filling duration input
        frame_duree = tk.Frame(self.root)
        frame_duree.pack(pady=10)
        
        label_duree = tk.Label(frame_duree, text="Shovel filling duration (seconds):", 
                               font=("Arial", 11))
        label_duree.grid(row=0, column=0, padx=5)
        
        self.entry_duree = tk.Entry(frame_duree, textvariable=self.duree_remplissage, 
                                    width=8, font=("Arial", 11))
        self.entry_duree.grid(row=0, column=1, padx=5)
        
        # Frame for control buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=20)
        
        # Start button
        self.bouton_start = tk.Button(frame_buttons, text="Start", command=self.start,
                                      bg="#38a365", fg="white", width=10, height=2, 
                                      font=("Arial", 12, "bold"), cursor="hand2")
        self.bouton_start.grid(row=0, column=0, padx=15)
        
        # Quit button
        bouton_quitter = tk.Button(frame_buttons, text='Quit', command=self.quitter,
                                   bg="#e13825", fg="white", width=10, height=2, 
                                   font=("Arial", 12, "bold"), cursor="hand2")
        bouton_quitter.grid(row=0, column=1, padx=15)
        
        # Information label
        self.label_info = tk.Label(self.root, text="", font=("Arial", 9), fg="#7f8c8d")
        self.label_info.pack(pady=10)
    
    def start(self):
        try:
            # Validate number of hits
            hits = self.valeur_totem.get()
            if hits <= 0 or hits > 20:
                messagebox.showerror("Error", "Number of hits must be between 1 and 20")
                return
            
            # Validate shovel filling duration
            duree = self.duree_remplissage.get()
            if duree <= 0 or duree > 30:
                messagebox.showerror("Error", "Duration must be between 0 and 30 seconds")
                return
            
            # Disable input fields and start button
            self.bouton_start.config(state="disabled")
            self.entry_duree.config(state="disabled")
            self.entry_hits.config(state="disabled")
            
            # Update info label
            self.label_info.config(text="You have 5 seconds to switch to the game window!", 
                                  fg="#e67e22")
            self.root.update()
            
            # Give user time to switch to game window
            time.sleep(5)
            
            # Start the macro cycle
            self.is_running = True
            self.label_info.config(text="Program running! Press Ctrl+C in console to stop", 
                                  fg="#6dcd95")
            self.cycle()
            
        except tk.TclError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def cycle(self):
        # Get user-configured values
        e = self.valeur_totem.get()  # Number of hits
        y = self.duree_remplissage.get()  # Shovel filling duration
        
        try:
            while self.is_running:
                # Hold mouse to fill shovel 
                for i in range(e):
                    pydirectinput.mouseDown()
                    time.sleep(y)
                    pydirectinput.mouseUp()
                    time.sleep(1)
                
                # Wait before filling shovel
                time.sleep(1.5)
                
                # Move forward slightly
                pydirectinput.keyDown('w')
                time.sleep(0.5)
                pydirectinput.keyUp('w')
                time.sleep(0.5)
                
                # Single click to prepare shovel
                pydirectinput.click()
                time.sleep(0.7)
                
                # Hold mouse to empty the pan 
                pydirectinput.mouseDown()
                time.sleep(e*3)
                pydirectinput.mouseUp()
                time.sleep(1.5)
                
                # Move backward to reset position
                pydirectinput.keyDown('s')
                time.sleep(0.5)
                pydirectinput.keyUp('s')
                time.sleep(0.5)
                
                
                
        except KeyboardInterrupt:
            # Stop the program if interrupted
            self.arreter()
        except Exception as e:
            # Handle any errors that occur
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.arreter()
    
    def arreter(self):
        # Stop the running cycle
        self.is_running = False
        self.label_info.config(text="Program stopped", fg="#e74c3c")
    
    def quitter(self):
        # Confirm and quit the application
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.is_running = False
            self.root.quit()
            self.root.destroy()


# Launch the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProspectingApp(root)
    root.mainloop()