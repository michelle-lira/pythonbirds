class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))  # passando o parâmetro p
    print(id(p))
    print(p.cumprimentar())  # deste modo também estou passando o parâmetro p
