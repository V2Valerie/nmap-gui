import os
from tkinter import *

# Create the GUI window
root = Tk()
root.title("Nmap Scanner")
root.geometry("600x600")

# Define a function to run Nmap with selected options and display the output
def run_nmap():
    # Get the IP address or domain name from the text entry box
    target = target_entry.get()

    # Get the selected options
    options = ""
    if tcp_var.get() == 1:
        options += " -sS"
    if udp_var.get() == 1:
        options += " -sU"
    if pon_var.get() == 1:
        options += " -Pn"
    if os_detection_var.get() == 1:
        options += " -O"
    #if port_range_entry.get():
    #    options += f" -p {port_range_entry.get()}"

    # Run Nmap using the subprocess module
    cmd = f"nmap{options} {target}"
    result = os.popen(cmd).read()

    # Display the output in the text box
    output.delete(1.0, END)
    output.insert(END, result)

# Add a label and text entry box for the target
target_label = Label(root, text="Enter IP Address or Domain Name:")
target_label.pack()
target_entry = Entry(root)
target_entry.pack()

# Add checkbuttons for options
options_frame = Frame(root)
options_frame.pack()

os_detection_var = IntVar()
os_detection_checkbutton = Checkbutton(options_frame, text="OS Detection (-O)", variable=os_detection_var, onvalue=1, offvalue=0)
os_detection_checkbutton.pack(side=LEFT)

tcp_var = IntVar()
tcp_checkbutton = Checkbutton(options_frame, text="TCP Scan (-sS)", variable=tcp_var, onvalue=1, offvalue=0)
tcp_checkbutton.pack(side=LEFT)

udp_var = IntVar()
udp_checkbutton = Checkbutton(options_frame, text="UDP Scan (-sU)", variable=udp_var, onvalue=1, offvalue=0)
udp_checkbutton.pack(side=LEFT)

pon_var = IntVar()
pon_checkbutton = Checkbutton(options_frame, text="Ping or Not (-Pn)", variable=pon_var, onvalue=1, offvalue=0)
pon_checkbutton.pack(side=LEFT)

# Add an entry box to specify port range
#port_range_label = Label(root, text="Port Range (e.g. 1-100):")
#port_range_label.pack()
#port_range_entry = Entry(root)
#port_range_entry.pack()

# Add a button to run Nmap and display the output
run_button = Button(root, text="Run Nmap", command=run_nmap)
run_button.pack()

# Add a text box to display the output
output = Text(root)
output.configure(height=33, width=98)
output.pack()

# Start the GUI loop
root.mainloop()
