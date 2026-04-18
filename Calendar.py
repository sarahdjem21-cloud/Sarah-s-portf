import tkinter as tk
import calendar
from datetime import datetime

# Date actuelle
now = datetime.now()
month = now.month
year = now.year

def show_calendar():
    cal = calendar.month(year, month)
    text.delete("1.0", tk.END)
    text.insert(tk.END, cal)

# Fenêtre
root = tk.Tk()
root.title("Calendrier")

# Zone texte
text = tk.Text(root, width=20, height=8, font=("Courier", 14))
text.pack()

# Bouton
btn = tk.Button(root, text="Afficher Calendrier", command=show_calendar)
btn.pack()

root.mainloop()