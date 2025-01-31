class Pessoa:
    olhos = 2  # atributo default ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome  # sel.nome->atributo do objeto | nome->parâmetro
        self.filhos = list(filhos)

    def cumprimentar(self):  # atributo da classe
        # return f'Olá {id(self)}'
        return f'Olá, meu nome é {self.nome}'

    @staticmethod  # funciona como uma função atrelada à classe
    def metodo_estatico():  # Independe do objeto, por isso ñ tem parâmetro
        return 43

    @classmethod
    def nome_e_atributos_de_classe(cls):  # usado quando queremos acessar dados da própria classe
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    # p = Pessoa('Ben')
    # benjamin = Homem(nome='Benjamin')  # ou Pessoa, classe mãe
    benjamin = Mutante(nome='Benjamin')
    # luciano = Pessoa(benjamin, nome='Luciano')
    luciano = Homem(benjamin, nome='Luciano')
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
    luciano.olhos = 1  # agora vai aparecer no __dict__, porque foi alterado na instância
    del luciano.olhos
    print(luciano.__dict__)  # verificar todos os atributos de instância (os do __init__ e os criados dinamicamente)
    # print(Pessoa.olhos)  # não faria sentido tentar saber isso, pois não é um atributo de classe
    # Pessoa.olhos = 3  # altera qtd de olhos para toda a classe
    print(luciano.olhos)
    print(benjamin.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(benjamin.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(benjamin, Pessoa))
    print(isinstance(benjamin, Homem))
    print(benjamin.olhos)
    print(luciano.cumprimentar())
    print(benjamin.cumprimentar())
