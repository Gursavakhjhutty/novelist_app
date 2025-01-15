import tkinter as tk

def create_main_window():
    root = tk.TK()
    root.title("Novel Writing App")

    chapter_list = tk.Listbox(root)
    chapter_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    text_area = tk.Text(root)
    text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    root.mainloop()