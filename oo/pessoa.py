class Pessoa:
    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome  # sel.nome->atributo do objeto | nome->parâmetro
        self.filhos = list(filhos)

    def cumprimentar(self):  # atributo da classe
        return f'Olá {id(self)}'


if __name__ == '__main__':
    # p = Pessoa('Ben')
    benjamin = Pessoa(nome='Benjamin')
    luciano = Pessoa(benjamin, nome='Luciano')
    # print(Pessoa.cumprimentar(p))  # passando o parâmetro p
    print(Pessoa.cumprimentar(luciano))
    # print(id(p))
    print(id(luciano))
    # print(p.cumprimentar())  # deste modo também estou passando o parâmetro p
    print(luciano.cumprimentar())
    # print(p.nome)  # acessando atributo através do próprio objeto
    print(luciano.nome)
    # p.nome = 'Luan'  # alterando o valor do atributo
    # print(p.nome)
    print(luciano.nome)
    # print(p.idade)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'  # criando atributo dinâmico
    print(luciano.sobrenome)
    benjamin.sobrenome = 'Lira'
    print(benjamin.sobrenome)
    print(luciano.__dict__)  # verificar todos os atributos de instância
    print(benjamin.__dict__)  # verificar todos os atributos de instância
    del luciano.filhos
    print(luciano.__dict__)  # verificar todos os atributos de instância (os do __init__ e os criados dinamicamente)
