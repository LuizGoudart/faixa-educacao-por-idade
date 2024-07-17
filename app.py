from datetime import datetime
import customtkinter as tk
from datetime import datetime
import os


class Main(tk.CTk):
    def __init__(self):
        super().__init__()
        self.window_config()
        self.body()
        self.interacoes()
        self.frames()
        self.color_theme()
        self.duvida_button()
        self.iconbitmap(r'codes\imagens\school-removebg-preview.ico')

    def window_config(self):
        self.geometry('800x500')
        self.title('Faixa Educação Por Idade')
        self.resizable(False, False)


    def color_theme(self):
        self.label_theme = tk.CTkLabel(self, text='Tema:', 
                                       text_color=['#000', '#fff'], 
                                       bg_color="transparent",
                                       font=('Bahnschrift', 15))
        self.label_theme.place(relx=0.35, rely=0.85)
        self.option = tk.CTkOptionMenu(self, values=['Claro', 'Escuro', 'Padrão Sistema'], command=self.click_theme)
        self.option.place(relx=0.35, rely=0.9)
        self.option.set('Padrão Sistema')


    def click_theme(self, new_theme):
        if new_theme == 'Claro':
            tk.set_appearance_mode('Light')
        elif new_theme == 'Escuro':
            tk.set_appearance_mode('Dark')
        else:
            tk.set_appearance_mode('System')


    def clear_result(self):
        
        # Limpar labels de resultados anteriores, se existirem
        if hasattr(self, 'resultado_label'):
            self.resultado_label.destroy()


    def verificar_data(self):
        # Limpar o resultado anterior antes de mostrar o novo
        self.clear_result()
        # Obtém o valor do CTkEntry
        data_str = self.entry.get()
        try:
            # Tenta converter a string de data para um objeto datetime com barras
            data = datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            try:
                # Se falhar, tenta converter sem barras
                data = datetime.strptime(data_str, "%d%m%Y")
            except ValueError:
                # Se ambas as conversões falharem, mostra mensagem de erro
                self.mostrar_mensagem_erro("Formato de data inválido! \nUse o formato DD/MM/YYYY ou DDMMYYYY.")
                return  # Encerra a função aqui para não prosseguir com cálculos inválidos

        # Calcula a idade da pessoa
        hoje = datetime.now()
        idade_atual = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))

        # Mostrar o resultado na tela
        self.mostrar_resultado(idade_atual)

    def mostrar_mensagem_erro(self, mensagem):
        self.resultado_label = tk.CTkLabel(self, text=mensagem,
                                            text_color='red',
                                            font=('Bahnschrift', 20))
        self.resultado_label.place(relx=0.44, rely=0.6)


    def mostrar_resultado(self, idade_atual):
        if idade_atual <= 1:
            resultado_texto = f"A criança tem: {idade_atual} ano.\n Creche (Berçário)"
        elif idade_atual == 2:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n Maternal 1"
        elif idade_atual == 3:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n Maternal 2"
        elif idade_atual == 4:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n Pré - Escolar I"
        elif idade_atual == 5:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n Pré - Escolar II"
        elif idade_atual == 6:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 1º ano do Fundamental"
        elif idade_atual == 7:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 2º ano do Fundamental"
        elif idade_atual == 8:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 3º ano do Fundamental"
        elif idade_atual == 9:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 4º ano do Fundamental"
        elif idade_atual == 10:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 5º ano do Fundamental"
        elif idade_atual == 11:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 6º ano do Fundamental"
        elif idade_atual == 12:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 7º ano do Fundamental"
        elif idade_atual == 13:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 8º ano do Fundamental"
        elif idade_atual == 14:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 9º ano do Fundamental"
        elif idade_atual == 15:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 1º ano do Ensino Médio"
        elif idade_atual == 16:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 2º ano do Ensino Médio"
        elif idade_atual == 17:
            resultado_texto = f"A criança tem: {idade_atual} anos.\n 3º ano do Ensino Médio"
        else:
            resultado_texto = f"Idade atual: {idade_atual} anos.\n Etapa escolar finalizada!"

        self.resultado_label = tk.CTkLabel(self, text=resultado_texto,
                                            text_color='green',
                                            font=('Bahnschrift', 23))
        self.resultado_label.place(relx=0.52, rely=0.6)


    def body(self):
        self.tit1 = tk.CTkLabel(self, text="Faixa Educação Por Idade", font=('Bahnschrift', 28), 
                                text_color=['#696969', '#fff'], bg_color="transparent")
        self.tit1.pack(pady=15, padx=15)
        self.tit1.place(relx=0.453, rely=0.05)

        self.label_data_nascimento = tk.CTkLabel(self, text="Insira a data de nascimento:", text_color=['#696969', '#fff'], 
                                                 bg_color="transparent", font=('Bahnschrift', 15))
        self.label_data_nascimento.place(relx=0.535, rely=0.18)


    def frames(self):    
        # Frame à esquerda
        self.frame_principal = tk.CTkFrame(self, width=255, height=500, bg_color=['#DCDCDC', '#1C1C1C'], 
                                           fg_color='transparent', corner_radius=10)
        self.frame_principal.grid(row=1, column=1, padx=2, pady=2)

        # Texto do frame
        self.txt_frame1 = tk.CTkLabel(self.frame_principal, text='Turmas com base na \nidade adquada', text_color=['#000', '#fff'], 
                                      font=('Bahnschrift', 18), 
                                      bg_color=['#DCDCDC', '#1C1C1C'])
        self.txt_frame1.place(relx=0.2, rely=0.05)

        # Maternal I
        self.txt_frame2 = tk.CTkLabel(self.frame_principal, text='Maternal I - 2 anos', 
                                      text_color=['#000', '#fff'], font=('Bahnschrift', 15), 
                                      bg_color=['#DCDCDC', '#1C1C1C'])
        self.txt_frame2.place(relx=0.25, rely=0.2)

        # Maternal II
        self.txt_frame3 = tk.CTkLabel(self.frame_principal, text='Maternal II - 3 anos', 
                                      text_color=['#000', '#fff'], font=('Bahnschrift', 15), 
                                      bg_color=['#DCDCDC', '#1C1C1C'])
        self.txt_frame3.place(relx=0.25, rely=0.3)

        # Pré - Escolar I
        self.txt_frame4 = tk.CTkLabel(self.frame_principal, text='Pré-Escolar I - 4 anos', 
                                      text_color=['#000', '#fff'], font=('Bahnschrift', 15), 
                                      bg_color=['#DCDCDC', '#1C1C1C'])
        self.txt_frame4.place(relx=0.22, rely=0.4)

        # Pré - Escolar II
        self.txt_frame5 = tk.CTkLabel(self.frame_principal, text='Pré-Escolar II - 5 anos', 
                                      text_color=['#000', '#fff'], font=('Bahnschrift', 15), 
                                      bg_color=['#DCDCDC', '#1C1C1C'])
        self.txt_frame5.place(relx=0.22, rely=0.5)

        # 1ª Ensino Fundamental
        self.txt_frame6 = tk.CTkLabel(self.frame_principal, text='1ª Ensino Fundamental - 6 anos', 
                                      text_color=['#000', '#fff'], font=('Bahnschrift', 15), 
                                      bg_color=['#DCDCDC', '#1C1C1C'])
        self.txt_frame6.place(relx=0.05, rely=0.6)

        
        self.button_como_funciona = tk.CTkButton(self.frame_principal, text='Como usar', 
                                          font=('Bahnschrift', 14),
                                          width=150, bg_color="transparent", fg_color='green', 
                                          hover_color='#006400',
                                          command=self.material_auxiliar).place(relx=0.22, rely=0.9)


    def material_auxiliar(self):
        os.startfile(r'codes\externo\FEPI-Material Auxiliar.pdf')


    def clear(self):
        # Limpar o campo de entrada e o resultado anterior
        self.entry.delete(0, 'end')
        self.clear_result()

    
    def duvida_button(self):
        pass


    def interacoes(self):
        # Campo a inserir a data
        self.entry = tk.CTkEntry(self, width=220, height=30, text_color=['#696969', 'white' ], 
                                 placeholder_text='Exemplo: 12/05/2020', 
                                 bg_color="transparent", placeholder_text_color='#696969')
        self.entry.pack(pady=20)
        self.entry.place(relx=0.52, rely=0.25)

        # Botão para verificar a data
        self.button = tk.CTkButton(self, width=200, height=30, text='Verificar' ,font=('Bahnschrift', 15),
                                   fg_color='green', command=self.verificar_data, hover_color='#006400')
        self.button.place(relx=0.533, rely=0.37)

        # Botão para limpar o campo e o resultado
        self.button_clear = tk.CTkButton(self, text="Limpar", font=('Bahnschrift', 14), fg_color='green',
                                         hover_color='#006400',
                                         command=self.clear).place(relx=0.8, rely=0.9)
        
        
