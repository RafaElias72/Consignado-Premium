import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


editando_codigo = None

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS consignado (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    peca_nome TEXT NOT NULL,
    chamado TEXT NOT NULL,
    IDcase_troca TEXT NULL,
    IDcase_consig TEXT NOT NULL,
    tecnico TEXT,
    data TEXT, 
    obs TEXT
    )''')
conexao.commit()

caminho_banco = r"C:\Users\Rafael\Desktop\painel_consignado\data\banco.db"

def enviar_dados():
    global editando_codigo  
    
    codigo = campo_codigo.get()
    peca_nome = campo_peca_nome.get()
    chamado = campo_chamado.get()
    case_consig = campo_caseID_consig.get()
    case_troca = campo_caseID_troca.get()
    tecnico = campo_tecnico.get()
    data = campo_data.get()
    obs = campo_obs.get()

    if codigo == '':
        messagebox.showerror("Erro!", "Códgido não foi inserido.")
        return
    
    if editando_codigo:        
        cursor.execute('''
            UPDATE consignado 
            SET codigo = ?, peca_nome = ?, chamado = ?, IDcase_consig = ?, 
                IDcase_troca = ?, tecnico = ?, data = ?, obs = ?
            WHERE codigo = ?
        ''', (codigo, peca_nome, chamado, case_consig, case_troca, 
              tecnico, data, obs, editando_codigo))
        
        messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
        editando_codigo = None
        
    else:  
        cursor.execute("SELECT codigo FROM consignado WHERE codigo = ?", (codigo,))
        if cursor.fetchone():
            messagebox.showerror("Erro", "O código inserido já existe.")
            return
        
        cursor.execute('''
            INSERT INTO consignado(codigo, peca_nome, chamado, IDcase_consig, IDcase_troca, tecnico, data, obs)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        ''', (codigo, peca_nome, chamado, case_consig, case_troca, tecnico, data, obs))
        
    
    conexao.commit()

    limpar_campos()
    
    atualizar_tabela()
    

def atualizar_tabela():
    for item in tabela_consignado.get_children():
        tabela_consignado.delete(item)
    
    cursor.execute("SELECT codigo, peca_nome, chamado, IDcase_consig, IDcase_troca, tecnico, data, obs FROM consignado")
    
    for linha in cursor.fetchall():
        tabela_consignado.insert("", "end", values=linha)

def editar_dados():
    global editando_codigo  
    
    item_selecionado = tabela_consignado.selection()
    
    if item_selecionado:  
        valores = tabela_consignado.item(item_selecionado)['values']
        
        editando_codigo = valores[0]
        
        limpar_campos()
    
        campo_codigo.insert(0, valores[0])    
        campo_peca_nome.insert(0, valores[1])  
        campo_chamado.insert(0, valores[2])   
        campo_caseID_consig.insert(0, valores[3])  
        campo_caseID_troca.insert(0, valores[4])   
        campo_tecnico.insert(0, valores[5])     
        campo_data.insert(0, valores[6])        
        campo_obs.insert(0, valores[7])     

def excluir_dados():
    item_selecionado = tabela_consignado.selection()
    
    if item_selecionado:  
        valores = tabela_consignado.item(item_selecionado)['values']
        codigo = valores[0]  
        
        cursor.execute("DELETE FROM consignado WHERE codigo = ?", (codigo,))
        conexao.commit()
        atualizar_tabela()
        messagebox.showinfo("Excluído", "Dados excluidos com sucesso!")
        

 
def pesquisar():
    termo = campo_pesquisa.get()
    
    if termo:
        cursor.execute("SELECT codigo FROM consignado WHERE codigo = ?", (termo,))
        resultado = cursor.fetchone()
        
        if resultado:
            for item in tabela_consignado.selection():
                tabela_consignado.selection_remove(item)
            
            for item in tabela_consignado.get_children():
                valores = tabela_consignado.item(item)['values']
                if valores and str(valores[0]) == str(termo):  
                    tabela_consignado.selection_add(item)
                    tabela_consignado.see(item)
                    break
            
            campo_pesquisa.delete(0, 'end')
        else:
            messagebox.showerror("Erro", f"O código '{termo}' não existe.")
    else:
        messagebox.showwarning("Aviso", "Digite um código para pesquisar.")

def limpar_campos():
    campo_codigo.delete(0, 'end')
    campo_peca_nome.delete(0, 'end')
    campo_chamado.delete(0, 'end')
    campo_caseID_consig.delete(0, 'end')
    campo_caseID_troca.delete(0, 'end')
    campo_tecnico.delete(0, 'end')
    campo_data.delete(0, 'end')
    campo_obs.delete(0, 'end')


# criação da tela
app = ctk.CTk()
ctk.set_appearance_mode('light')
app.title("Consignado")
app.geometry("1200x600")

#label
label_codigo = ctk.CTkLabel(app, text='Código: ')
label_codigo.place(relx=0.05, rely=0.05)
#entry
campo_codigo = ctk.CTkEntry(app,height=8, width=100)
campo_codigo.place(relx=0.03, rely=0.10)

#label
label_peca_nome = ctk.CTkLabel(app, text='Nome da peça: ')
label_peca_nome.place(relx=0.135, rely=0.05)
#entry
campo_peca_nome = ctk.CTkEntry(app,height=8, width=100)
campo_peca_nome.place(relx=0.13, rely=0.10)

#label
label_chamado = ctk.CTkLabel(app, text='Chamado: ')
label_chamado.place(relx=0.049, rely=0.14)
#entry
campo_chamado = ctk.CTkEntry(app,height=8, width=100)
campo_chamado.place(relx=0.03, rely=0.19)

#label
label_caseID_consig = ctk.CTkLabel(app, text='ID da case (Consig): ')
label_caseID_consig.place(relx=0.13, rely=0.14)
#entry
campo_caseID_consig = ctk.CTkEntry(app,height=8, width=100)
campo_caseID_consig.place(relx=0.13, rely=0.19)

#label
label_caseID_troca = ctk.CTkLabel(app, text='ID da case (Troca): ')
label_caseID_troca.place(relx=0.23, rely=0.05)
#entry
campo_caseID_troca = ctk.CTkEntry(app,height=8, width=100)
campo_caseID_troca.place(relx=0.23, rely=0.10)

#label
label_tecnico = ctk.CTkLabel(app, text='Técnico: ')
label_tecnico.place(relx=0.25, rely=0.14)
#entry
campo_tecnico = ctk.CTkEntry(app,height=8, width=100)
campo_tecnico.place(relx=0.23, rely=0.19)

#label
label_data = ctk.CTkLabel(app, text='Data: ')
label_data.place(relx=0.359, rely=0.05)
#entry
campo_data = ctk.CTkEntry(app,height=8, width=100)
campo_data.place(relx=0.33, rely=0.10)

#label
label_obs = ctk.CTkLabel(app, text='Observações: ')
label_obs.place(relx=0.34, rely=0.14)
#entry
campo_obs = ctk.CTkEntry(app,height=8, width=100)
campo_obs.place(relx=0.33, rely=0.19)

#button
botao_enviar = ctk.CTkButton(app, text='Enviar Dados', command=enviar_dados, height=8, width=80)
botao_enviar.place(relx=0.03, rely=0.25)

#button
botao_editar = ctk.CTkButton(app, text='Editar Dados', command=editar_dados, height=8, width=80)
botao_editar.place(relx=0.11, rely=0.25)

#button
botao_excluir = ctk.CTkButton(app, text='Excluir Dados', command=excluir_dados, height=8, width=80)
botao_excluir.place(relx=0.19, rely=0.25)

#button
botao_limpar = ctk.CTkButton(app, text='Limpar Campos', command=limpar_campos, height=8, width=80)
botao_limpar.place(relx=0.273, rely=0.25)

#pesquisa
campo_pesquisa = ctk.CTkEntry(app, height=8, width=200, placeholder_text="Digite para pesquisar o código...")
campo_pesquisa.place(relx=0.50, rely=0.10)

botao_pesquisar = ctk.CTkButton(app, text='Buscar', command=pesquisar, height=8, width=80)
botao_pesquisar.place(relx=0.665, rely=0.10)

#container (tables)
container_tabela = ctk.CTkFrame(app)  
container_tabela.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.95, relheight=0.5)
container_tabela._set_appearance_mode("light")

#creating tables
tabela_consignado = ttk.Treeview(container_tabela, selectmode="browse", 
                                columns=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8"), 
                                show='headings', height=340)


#Tables
tabela_consignado.column("column1", width=100, minwidth=50)
tabela_consignado.heading("column1", text="Código")

tabela_consignado.column("column2", width=150, minwidth=50)
tabela_consignado.heading("column2", text="Nome da Peça")

tabela_consignado.column("column3", width=100, minwidth=50)
tabela_consignado.heading("column3", text="Chamado")

tabela_consignado.column("column4", width=120, minwidth=50)
tabela_consignado.heading("column4", text="ID Case Consig", )

tabela_consignado.column("column5", width=120, minwidth=50)
tabela_consignado.heading("column5", text="ID Case Troca")

tabela_consignado.column("column6", width=120, minwidth=50)
tabela_consignado.heading("column6", text="Técnico")

tabela_consignado.column("column7", width=100, minwidth=50)
tabela_consignado.heading("column7", text="Data")

tabela_consignado.column("column8", width=200, minwidth=50)
tabela_consignado.heading("column8", text="Observações")


tabela_consignado.pack(expand=True, fill='both', padx=7, pady=7) #expand permite que a tabela cresca a medida que dados são inseridos 

def ao_clicar_tabela(event):
    item_clicado = tabela_consignado.identify_row(event.y)
    itens_selecionados = tabela_consignado.selection()
    
    if item_clicado in itens_selecionados:
        tabela_consignado.selection_remove(item_clicado)

tabela_consignado.bind('<Button-1>', ao_clicar_tabela)


atualizar_tabela()

app.mainloop()