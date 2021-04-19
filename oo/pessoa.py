class Pessoa:
    def __init__(self, nome=None, idade=25):
        self.idade = idade
        self.nome = nome  # sel.nome->atributo do objeto | nome->parâmetro

    def cumprimentar(self):  # atributo da classe
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Ben')
    print(Pessoa.cumprimentar(p))  # passando o parâmetro p
    print(id(p))
    print(p.cumprimentar())  # deste modo também estou passando o parâmetro p
    print(p.nome)  # acessando atributo através do próprio objeto
    p.nome = 'Luan'  # alterando o valor do atributo
    print(p.nome)
    print(p.idade)
