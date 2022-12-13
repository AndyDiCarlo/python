import tkinter as tk
from datetime import datetime

# Create Tkinter window
window = tk.Tk()

# Set window title and make window sticky
window.title("Digital Clock")
window.geometry("300x100")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create label to display the time, set grid and make centered
clock_label = tk.Label(window, font=("times", 20, "bold"))
clock_label.grid(row=0, column=0, sticky="NESW")
clock_label.grid_rowconfigure(0, weight=1)
clock_label.grid_columnconfigure(0, weight=1)

# Function to update the time display
def update_time():
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    # Update the time on the label
    clock_label.configure(text=current_time)
    # Call the function again after one second
    clock_label.after(1000, update_time)

# Call the update_time function to start the clock
update_time()

# Run the Tkinter main loop
window.mainloop()
