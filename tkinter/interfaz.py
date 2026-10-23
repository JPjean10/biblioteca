import tkinter as tk

ventana = tk.Tk()
ventana.geometry ("600x800")

bienvenida = tk.Label(ventana , text=" biblioidat", font= ("helvetica", 24 , "bold")  )

bienvenida.pack(side = "top" , anchor="w", padx=20, pady=20)
ventana.title("BIBLIOIDAT")

usuario = tk.Label(ventana , text="usuario", font=("arial" , 15 ))

usuario.pack (side = "top" ,anchor="w" , padx=20 , pady= 5 )

usuario_caja = tk.Entry(ventana, width=15 , font=("arial" , 12))
usuario_caja.place(  relx=0.5 , anchor="w")

contraseña= tk.Label(ventana , text="contraseña", font=("arial" , 15 ))

contraseña.pack (side = "top" ,anchor="w" , padx=20 ,pady=10 )

ventana.mainloop()