import customtkinter as ctk

ctk.set_appearance_mode('light')

app = ctk.CTk()
app.title("Consignado")
app.geometry("1200x600")

#label
label_codigo = ctk.CTkLabel(app, text='Código: ')
label_codigo.grid(row=0, column=0)
#entry
campo_codigo = ctk.CTkEntry(app,height=8, width=100)
campo_codigo.grid(row=1, column=0)
#label
label_peca_nome = ctk.CTkLabel(app, text='Nome da peça: ')
label_peca_nome.grid(row=0, column=2)
#entry
campo_peca_nome = ctk.CTkEntry(app,height=8, width=100)
campo_peca_nome.grid(row=1, column=2)
#label
label_chamado = ctk.CTkLabel(app, text='Chamado: ')
label_chamado.grid(row=2, column=0)
#entry
campo_chamado = ctk.CTkEntry(app,height=8, width=100)
campo_chamado.grid(row=3, column=0)
#label
label_caseID_consig = ctk.CTkLabel(app, text='ID da case (Consig): ')
label_caseID_consig.grid(row=2, column=2)
#entry
campo_caseID_consig = ctk.CTkEntry(app,height=8, width=100)
campo_caseID_consig.grid(row=3, column=2)
#label
label_caseID_troca = ctk.CTkLabel(app, text='ID da case (Troca): ')
label_caseID_troca.grid(row=0, column=3)
#entry
campo_caseID_troca = ctk.CTkEntry(app,height=8, width=100)
campo_caseID_troca.grid(row=1, column=3)
#label
label_tecnico = ctk.CTkLabel(app, text='Técnico: ')
label_tecnico.grid(row=2, column=3)
#entry
campo_tecnico = ctk.CTkEntry(app,height=8, width=100)
campo_tecnico.grid(row=3, column=3)
#label
label_data = ctk.CTkLabel(app, text='Data: ')
label_data.grid(row=0, column=4)
#entry
campo_data = ctk.CTkEntry(app,height=8, width=100)
campo_data.grid(row=1, column=4)
#label
label_obs = ctk.CTkLabel(app, text='Observações: ')
label_obs.grid(row=2, column=4)
#entry
campo_obs = ctk.CTkEntry(app,height=8, width=100)
campo_obs.grid(row=3, column=4)


#button
botao_enviar = ctk.CTkButton(app, )



app.mainloop()