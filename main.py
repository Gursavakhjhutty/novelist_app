import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from models.project import Project
from utils.file_manager import save_project, load_project

# Initialize a global variable for the current project
current_project = None

def new_project():
    global current_project
    title = simple_input("Enter the title of your novel:")
    genre = simple_input("Enter the genre of your novel:")
    if title and genre:
        current_project = Project(title, genre)
        update_chapter_list()
        messagebox.showinfo("New Project", f"Project '{title}' created!")

def add_chapter():
    global current_project
    if current_project is None:
        messagebox.showerror("Error", "Create or load a project first!")
        return

    title = simple_input("Enter chapter title:")
    if title:
        current_project.add_chapter({"title": title, "content": ""})
        update_chapter_list()

def save_project_to_file():
    global current_project
    if current_project is None:
        messagebox.showerror("Error", "Create or load a project first!")
        return

    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        save_project(current_project, filename)
        messagebox.showinfo("Save Project", "Project saved successfully!")

def load_project_from_file():
    global current_project
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filename:
        try:
            global current_project
            current_project = load_project(filename)
            update_chapter_list()
            messagebox.showinfo("Load Project", f"Project '{current_project.title}' loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load project: {e}")

def update_chapter_list():
    chapter_list.delete(0, tk.END)
    if current_project:
        for chapter in current_project.chapters:
            chapter_list.insert(tk.END, chapter['title'])

def on_chapter_select(event):
    if current_project:
        selected_index = chapter_list.curselection()
        if selected_index:
            chapter = current_project.chapters[selected_index[0]]
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, chapter['content'])

def save_chapter_content():
    global current_project
    if current_project:
        selected_index = chapter_list.curselection()
        if selected_index:
            chapter = current_project.chapters[selected_index[0]]
            chapter['content'] = text_area.get(1.0, tk.END)
            messagebox.showinfo("Save Chapter", "Chapter content saved!")

def simple_input(prompt):
    input_window = tk.Toplevel(root)
    input_window.title("Input")
    input_label = tk.Label(input_window, text=prompt)
    input_label.pack()
    input_entry = tk.Entry(input_window)
    input_entry.pack()
    input_entry.focus()
    def submit():
        input_window.user_input = input_entry.get()
        input_window.destroy()
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.pack()
    input_window.user_input = None
    root.wait_window(input_window)
    return input_window.user_input

# Create the main window
root = tk.Tk()
root.title("Novel Writing App")
root.geometry("800x600")

# Create UI components
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

chapter_list = tk.Listbox(left_frame)
chapter_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
chapter_list.bind("<<ListboxSelect>>", on_chapter_select)

add_chapter_button = tk.Button(left_frame, text="Add Chapter", command=add_chapter)
add_chapter_button.pack()

text_area = tk.Text(right_frame)
text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

save_chapter_button = tk.Button(right_frame, text="Save Chapter Content", command=save_chapter_content)
save_chapter_button.pack()

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project", command=new_project)
file_menu.add_command(label="Load Project", command=load_project_from_file)
file_menu.add_command(label="Save Project", command=save_project_to_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()