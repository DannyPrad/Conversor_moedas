import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x600")

dic_conversoes_disponiveis = conversoes_disponiveis()

# criar os botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))

texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

# Novo campo para inserir o valor a ser convertido
texto_valor = customtkinter.CTkLabel(janela, text="Digite o valor a converter:")
campo_valor = customtkinter.CTkEntry(janela, placeholder_text="Ex: 100.00")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                                 command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    valor_a_converter = campo_valor.get()  # Pegando o valor a ser convertido
    
    if moeda_origem and moeda_destino and valor_a_converter:
        try:
            valor_a_converter = float(valor_a_converter)  # Convertendo a entrada para float
            cotacao = float(pegar_cotacao_moeda(moeda_origem, moeda_destino))  # Pegando a cotação como float
            valor_convertido = valor_a_converter * cotacao  # Multiplicando pelo valor da cotação
            texto_cotacao_moeda.configure(text=f"{valor_a_converter} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")
        except ValueError:
            texto_cotacao_moeda.configure(text="Erro: valor inválido.")
    else:
        texto_cotacao_moeda.configure(text="Por favor, preencha todos os campos.")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

# colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
texto_valor.pack(padx=10, pady=10)
campo_valor.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# rodar a janela
janela.mainloop()
