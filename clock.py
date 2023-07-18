import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    current_info = f"{time_zone} Time\n{city}"
    clock_label.config(text=current_time)
    info_label.config(text=current_info)
    clock_label.after(1000, update_clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.configure(bg="black")

# Set the time zone and city
time_zone = "GMT"
city = "Nairobi"

# Set the clock style
font_style = ("Digital-7", 80)
font_color = "red"
bg_color = "black"

# Create a label to display the clock
clock_label = tk.Label(window, font=font_style, fg=font_color, bg=bg_color)
clock_label.pack(pady=20)

# Create a label to display time zone and city info
info_label = tk.Label(window, font=("Arial", 14), fg="white", bg=bg_color)
info_label.pack()

# Update the clock every second
update_clock()

# Start the main event loop
window.mainloop()
