import tkinter as tk
from tkinter import ttk
from Controller import ProteinSystem
from UseCases import RnaManager, DnaManager


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Protein Synthesis Master")
        self.geometry("650x225")
        self.resizable(False, False)
        self._frame = None
        self.frame_switch(MainPage)

    def frame_switch(self, frame):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def copy_to_clipboard(self, text):
        """Copies text to clipboard"""
        tk.Tk.clipboard_clear(self)
        tk.Tk.clipboard_append(self, text)
        tk.Tk.update(self)


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to the Protein Synthesis Master!") \
            .pack(side="top", fill="x", pady=20)
        tk.Button(self, text="Get the complementary DNA pair of a DNA sequence",
                  command=lambda: master.frame_switch(DNAtoDNA)).pack()
        tk.Button(self, text="Convert DNA sequence to its matching "
                             "complementary mRNA sequence",
                  command=lambda: master.frame_switch(DNAtoRNA)).pack()
        tk.Button(self, text="Convert RNA sequence to its "
                             "matching complementary DNA sequence",
                  command=lambda: master.frame_switch(RNAtoDNA)).pack()
        tk.Button(self, text="Find the polypeptide chain for a DNA sequence",
                  command=lambda: master.frame_switch(DNAtoProtein)).pack()


class DNAtoDNA(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input DNA sequence").pack(side="top",
                                                       pady=20)
        entry = tk.Entry(self, width=50)
        entry.pack()
        label = tk.Label(self, text="", state="normal")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            [label.config(text=ps.dna_pairing(entry.get()),
                                          wraplengt=500),
                             copied.config(text="")])
        convert.pack()
        copy = tk.Button(self, text="Copy",
                         command=lambda: [master.copy_to_clipboard(
                             label.cget("text")),
                             copied.config(text="Copied to Clipboard")])
        copy.pack()
        tk.Button(self, text="Return to main page",
                  command=lambda: master.frame_switch(MainPage)).pack()
        copied = tk.Label(self, text="")
        copied.pack(pady=10)


class DNAtoRNA(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input DNA sequence").pack(side="top",
                                                       pady=20)
        entry = tk.Entry(self, width=50)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            [label.config(text=ps.get_mrna(entry.get()),
                                          wraplengt=500),
                             copied.config(text="")])
        convert.pack()
        copy = tk.Button(self, text="Copy",
                         command=lambda: [master.copy_to_clipboard(
                             label.cget("text")),
                             copied.config(text="Copied to Clipboard")])
        copy.pack()
        tk.Button(self, text="Return to main page",
                  command=lambda: master.frame_switch(MainPage)).pack()
        copied = tk.Label(self, text="")
        copied.pack(pady=10)


class RNAtoDNA(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input RNA sequence").pack(side="top",
                                                       pady=20)
        entry = tk.Entry(self, width=50)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()
        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            [label.config(text=ps.get_dna(entry.get()),
                                          wraplengt=500),
                             copied.config(text="")])
        convert.pack()
        copy = tk.Button(self, text="Copy",
                         command=lambda: [master.copy_to_clipboard(
                             label.cget("text")),
                             copied.config(text="Copied to Clipboard")])
        copy.pack()
        tk.Button(self, text="Return to main page",
                  command=lambda: master.frame_switch(MainPage)).pack()
        copied = tk.Label(self, text="")
        copied.pack(pady=10)


class DNAtoProtein(tk.Frame):
    def __init__(self, master):
        dm = DnaManager()
        rm = RnaManager()
        ps = ProteinSystem(dm, rm)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Input DNA sequence").pack(side="top",
                                                       pady=20)
        entry = tk.Entry(self, width=50)
        entry.pack()
        label = ttk.Label(self, text="")
        label.pack()

        convert = tk.Button(self, text="Convert",
                            command=lambda:
                            [label.config(text=ps.get_protein(entry.get()),
                                          wraplengt=500),
                             copied.config(text="")])
        convert.pack()
        copy = tk.Button(self, text="Copy",
                         command=lambda: [master.copy_to_clipboard(
                             label.cget("text")),
                             copied.config(text="Copied to Clipboard")])
        copy.pack()
        tk.Button(self, text="Return to main page",
                  command=lambda: master.frame_switch(MainPage)).pack()
        copied = tk.Label(self, text="")
        copied.pack(pady=10)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
