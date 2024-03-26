from customtkinter import * # Importando as funcionalidades do customtkinter para a criação da interface grafica
from .utils import verificarPalindromo # Importa a função verificarPalindromo do modulo utils para realizar a verificação da palavra

class GUI:
    def __init__(self) -> None:
        """
        Inicializa a classe GUI e configura a tela principal.
        
        Cria uma instância do CTk (CustomTkinter) e define a variável 
        de resultado como uma string vazia.
        """
        self.screen = CTk()  # Cria a janela principal da aplicação
        self.resultado = ""  # Armazena o resultado da verificação de palíndromo

    def configure(self):
        """
        Configura a janela principal da aplicação.
        
        Define o título da janela, o tamanho, a capacidade de redimensionamento e o modo de aparência.
        """
        self.screen.title("Palindrometro")  # Define o título da janela
        self.screen.geometry("350x300")  # Define o tamanho da janela (largura x altura)
        self.screen.resizable(False, False)  # Impede o redimensionamento da janela
        self.screen._set_appearance_mode("dark")  # Define o modo de aparência para "escuro"

    def verificar_palindromo(self):
        """
        Obtém o texto da entrada do usuário e verifica se é um palíndromo.
        
        Atualiza o rótulo de resposta com o resultado da verificação.
        """
        palavra = self.input.get()  # Obtém o texto da entrada de texto
        self.resultado = verificarPalindromo(palavra)  # Verifica se a palavra é um palíndromo
        self.response.configure(text=self.resultado)  # Atualiza o rótulo com o resultado

    def main(self):
        """
        Configura e exibe os elementos principais da interface gráfica.
        
        Adiciona os widgets (rótulo, entrada, botão e rótulo de resposta) à tela principal.
        """
        self.bg = self.screen["bg"]  # Obtém a cor de fundo da tela

        # Cria e adiciona o rótulo de título
        self.title = CTkLabel(self.screen, width=350, height=40, text="Palindrometro")
        self.title.pack()

        # Cria e adiciona o campo de entrada de texto
        self.input = CTkEntry(self.screen, width=150, height=40, bg_color=self.bg)
        self.input.pack(pady=30)  # Adiciona espaço vertical ao redor do campo de entrada

        # Cria e adiciona o botão para verificar se a palavra é um palíndromo
        self.button = CTkButton(self.screen, command=self.verificar_palindromo, width=100, height=40, text="Verificar", bg_color=self.bg, text_color="white")
        self.button.pack()

        # Cria e adiciona o rótulo que exibirá o resultado
        self.response = CTkLabel(self.screen, width=350, height=40, text=self.resultado)
        print(self.resultado)  # Imprime o resultado no console (para depuração)
        self.response.pack(pady=20)  # Adiciona espaço vertical ao redor do rótulo de resposta

    def executar(self):
        """
        Executa a configuração e o loop principal da aplicação.
        
        Configura a interface gráfica e inicia o loop principal do Tkinter.
        """
        self.configure()  # Configura a janela principal
        self.main()  # Adiciona e organiza os widgets na janela
        self.screen.mainloop()  # Inicia o loop principal da aplicação
