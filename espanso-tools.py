
import tkinter as tk
import getpass
import tkinter as tk
import os

base_dir = os.path.dirname(__file__)
try:
    file_path = os.path.join(base_dir, './512@2x.png')
except:
    pass

username = getpass.getuser()
path = f"/Users/{username}/Library/Application Support/espanso/match/base.yml"



root = tk.Tk()
root.title("Espansa Tools")

# center window
# get tkinter window width and height
window_width = root.winfo_width()+30
window_height = root.winfo_height()+50
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# set icon to icons/512@2x.png
try:
    root.iconphoto(False, tk.PhotoImage(file="./512@2x.png"))
except:
    pass

# create input fields
input1_label = tk.Label(root, text="Trigger (without :)")
input1_label.pack()
input1_entry = tk.Entry(root)
input1_entry.pack()

input2_label = tk.Label(root, text="Replace with")
input2_label.pack()
input2_entry = tk.Entry(root)
input2_entry.pack()

# create trigger
def create_trigger():
    # if input fields are empty or contain a : show error
    if input1_entry.get() == "" or input2_entry.get() == "" or ":" in input1_entry.get() or ":" in input2_entry.get():
        error_label = tk.Label(root, text="Input fields are empty or contain a :")
        error_label.pack()
        root.after(2000, error_label.destroy)
        return
    with open(path, "a") as file:
        file.write(f"\n  - trigger: \":{input1_entry.get()}\"\n    replace: \"{input2_entry.get()}\"\n\n")
        file.close()

    # create text to show that trigger was created
    created_label = tk.Label(root, text="Trigger created!")
    created_label.pack()
    root.after(2000, created_label.destroy)

    # change created_label text to restart espanso
    created_label.config(text="Restart Espanso")
    created_label.pack()

    # restart espanso
    os.system("espanso restart")

    root.after(2000, created_label.destroy)

    # clear input fields
    input1_entry.delete(0, tk.END)
    input2_entry.delete(0, tk.END)


button_create_trigger = tk.Button(root, text="Create trigger", command=create_trigger, width=16)
button_create_trigger.pack()


def toggle_path():
    if path_label.cget("text") == "":
        path_label.config(text=path)
        button.config(text="Hide path")
        # set window width +100
        window_width = root.winfo_width()+300
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    else:
        path_label.config(text="")
        button.config(text="View path")
        # set window width -100
        window_width = root.winfo_width()-300
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

button = tk.Button(root, text="View path", command=toggle_path, width=16)
button.pack()

# create label to show path
path_label = tk.Label(root, text="")
path_label.pack()


# create test input field
test_input_label = tk.Label(root, text="Test input")
test_input_label.pack()
test_input_entry = tk.Entry(root)
test_input_entry.pack()


root.mainloop()
