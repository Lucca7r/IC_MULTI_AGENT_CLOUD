import tkinter as tk
import subprocess

def create_agent():
    agent_name = entry_agent_name.get()
    if agent_name:
        subprocess.run(f"docker run -d --name {agent_name} ic_mult_agent_cloud-agent3", shell=True)
        
def star_agent():
    agent_name = entry_agent_name.get()
    if agent_name:
        subprocess.run(f"docker start {agent_name}", shell=True)

def stop_agent():
    agent_name = entry_agent_name.get()
    if agent_name:
        subprocess.run(f"docker stop {agent_name}", shell=True)

def remove_agent():
    agent_name = entry_agent_name.get()
    if agent_name:
        subprocess.run(f"docker rm {agent_name}", shell=True)


root = tk.Tk()
root.title("Gerenciador de Agentes Docker")

label_instruction = tk.Label(root, text="Nome do Agente:")
label_instruction.pack()

entry_agent_name = tk.Entry(root)
entry_agent_name.pack()

button_create = tk.Button(root, text="Criar Agente", command=create_agent)
button_create.pack()

button_create = tk.Button(root, text="Iniciar Agente", command=star_agent)
button_create.pack()

button_stop = tk.Button(root, text="Parar Agente", command=stop_agent)
button_stop.pack()

button_remove = tk.Button(root, text="Remover Agente", command=remove_agent)
button_remove.pack()

root.mainloop()
