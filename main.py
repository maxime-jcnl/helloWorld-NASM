import subprocess
import tkinter as tk

# Fonction pour récupérer le out du binaire 
def run_hello_executable():
    executable_path = './bin/hello'
    
    try:
        result = subprocess.run([executable_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Erreur: {str(e)}"

# Défilement de texte
def animate_text():
    global x_pos
    x_pos += 2
    canvas.coords(text_id, x_pos, 50)  
    if x_pos > 200:
        x_pos = -100
    canvas.after(50, animate_text)


hello_message = run_hello_executable()

# Interface graphique
root = tk.Tk()
root.title("Hello World")
root.geometry("400x200")
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
x_pos = -100
text_id = canvas.create_text(x_pos, 50, text=hello_message, font=('Helvetica', 24), fill='blue')
animate_text()
root.mainloop()
