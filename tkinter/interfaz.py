import tkinter as tk

ventana = tk.Tk()
ventana.geometry ("600x800")

bienvenida = tk.Label(ventana , text=" biblioidat", font= ("helvetica", 24 , "bold")  )

bienvenida.pack(side = "top" , anchor="w", padx=20, pady=20)
ventana.title("BIBLIOIDAT")

container = tk.Frame(ventana)
container.place(relx=0.5, rely=0.5, anchor="center")

usuario = tk.Label(container, text="USUARIO", font=("arial" , 15 ))
usuario.grid (row=0 ,column=0 , padx=10 , pady= 10, sticky="w" )


usuario_caja = tk.Entry(container, width=15 , font=("arial" , 12))
usuario_caja.grid(  row=0,column=1 , padx=10, pady=10)


contraseña= tk.Label(container , text="CONTRASEÑA", font=("arial" , 15 ))
contraseña.grid (row=1 ,column=0 , padx=10 , pady= 10, sticky="w" )

contraseña_caja = tk.Entry(container, width=15 , font=("arial" , 12))
contraseña_caja.grid(  row=1,column=1 , padx=10, pady=10)

boton_entrar = tk.Button(container, text="Entrar", font=("arial", 14, "bold"), width=15, bg="#1C1D59", fg="white")
boton_entrar.grid(row=2, column=0, columnspan=2, pady=20)

ventana.mainloop()