
'''importacao do tkinter/banco de dados/messagebox'''
import customtkinter as ctk
from tkinter import *
import database
from tkinter import messagebox


'''a janela vai receber ctk'''
janela = ctk.CTk()
'''classe'''
class Aplication():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    #customizacao da tela de login--> cores e funcao tema
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    '''customizacao da janela/responsividade e funcao tela'''
    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de login")
        janela.iconbitmap("icon.ico")
        janela.resizable(False, False)

    '''imagem e funcao'''
    def tela_login(selef):
        img = PhotoImage(file="login2.png")
        label_img = ctk.CTkLabel(master= janela, image=img, text=None).place(x=1, y=70)

        title_label = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha\na plataforma",font=("Roboto", 25),text_color="#00B0F0").place(x= 10, y=10)

        '''login_frame divide a tela ao meio'''
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        '''login_frame widgets dentro do frame e tela de login'''
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("Roboto", 25)).place(x=25, y=5)


        '''campo login usuario p1 cores tamanho'''
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome do usuário", width=300, font=("Roboto", 15)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo nome do usuário é obrigatório", text_color="green", font=("Roboto", 11)).place(x=25, y=135)

        '''campo login usuario p2'''
        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do usuário", width=300, font=("Roboto", 15), show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo senha do usuário é obrigatório", text_color="green", font=("Roboto", 11)).place(x=25, y=205)

        '''botão 1 e 2'''
        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar sempre").place(x=25, y=235)

        '''Funcao login essa funcao esta dentro de uma funcao entao nao precisa do self da classe'''
        def login():

            msg = messagebox.showinfo(title="Estado do login", message="Parabéns! Login feito com sucesso.")
            pass
        login_Button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=login).place(x=25, y= 285)

        register_span = ctk.CTkLabel(master=login_frame, text="Se não tem uma conta").place(x=25, y=325)

        '''o atributo command vai receber o nome da funcao que vai dar funcionalidade a este botao quando ou seja ele vai receber o nome que chama a funcao que vai chamar as funcionalidades por tras do botao'''

        '''funcao tela cadastro'''
        def tela_register():
            #Remover o frame de login
            login_frame.pack_forget()

            '''criando a tela de cadastro de usuarios'''
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            rg_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=rg_frame, text="Faça o seu cadastro", font=("Roboto", 25)).place(x=25, y=5)

            span = ctk.CTkLabel(master=rg_frame, text="Por favor preencha todos os campos corretamente.", font=("Roboto", 12),text_color="gray").place(x=25, y=65)

            username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome do usuário", width=300, font=("Roboto", 15)).place(x=25, y=105)

            email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail do usuário", width=300, font=("Roboto", 15)).place(x=25, y=145)

            password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha do usuário", width=300, font=("Roboto", 15), show="*").place(x=25, y=185)

            cPassword_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirmação de senha", width=300, font=("Roboto", 15), show="*").place(x=25, y=225)

            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito todos os Termos de Política").place(x=25, y=265)

            '''Funcao do botao voltar'''
            def back():
                '''removendo o frame de cadastro'''
                rg_frame.pack_forget()

                '''devolvendo o frame de login'''
                login_frame.pack(side=RIGHT)

                

            back_Button = ctk.CTkButton(master=rg_frame, text="VOLTAR", width=145, fg_color="gray", hover_color="#204550", command=back).place(x=25, y= 315)

            '''funcao salvar usuario(save_user) --> essa funcao cadastra o usuario salvando seus dados para logo apos fazer o login'''
            def save_user():
                msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabéns! Usuário cadastrado com sucesso.")
                pass
            save_Button = ctk.CTkButton(master=rg_frame, text="CADASTRAR", width=145, fg_color="green", hover_color="#014B05", command=save_user).place(x=180, y= 315)


              
        register_Button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2d9334", command=tela_register).place(x=175, y=325) 




    '''janela main'''
Aplication()
