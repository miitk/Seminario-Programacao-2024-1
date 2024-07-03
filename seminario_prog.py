class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.atividades = []

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def recomendarExercicios(self):
        imc = self.calcularIMC()

        if imc < 18.5:
            return ['Exercícios de fortalecimento muscular', 'Exercícios aeróbicos']
        elif 18.5 <= imc < 25:
            return ['Exercícios aeróbicos', 'Exercícios de flexibilidade']
        elif 25 <= imc < 30:
            return ['Exercícios aeróbicos', 'Exercícios de fortalecimento muscular', 'Academia']
        elif 30 <= imc < 35:
            return ['Exercícios de equilíbrio', 'Exercícios aeróbicos', 'Exercícios de fortalecimento muscular', 'Academia', 'Natação']
        elif 35 <= imc < 40:
            return ['Exercícios aeróbicos', 'Exercícios de fortalecimento muscular', 'Exercícios de flexibilidade', 'Academia', 'Natação', 'Caminhada']
        else:
            return ['Acompanhamento médico e profissional', 'Academia', 'Caminhada', 'Natação', 'Esportes físicos']

    def cargaHorariaMinima(self):
        imc = self.calcularIMC()

        if imc < 18.5:
            return 3
        elif 18.5 <= imc < 25:
            return 2.5
        elif 25 <= imc < 30:
            return 4
        elif 30 <= imc < 35:
            return 5
        elif 35 <= imc < 40:
            return 6
        else:
            return 7

    def registrarAtividade(self, horas):
        self.atividades.append(horas)

    def totalHorasAtividades(self):
        return sum(self.atividades)

    def porcentagemMeta(self):
        horas_minimas = self.cargaHorariaMinima()
        total_horas = self.totalHorasAtividades()
        return (total_horas / horas_minimas) * 100

    def mensagemMotivacional(self):
        porcentagem = self.porcentagemMeta()

        if porcentagem >= 100:
            return "Parabéns! Você atingiu sua meta semanal de exercícios!"
        elif 75 <= porcentagem < 100:
            return "Ótimo trabalho! Você está quase lá. Continue assim!"
        elif 50 <= porcentagem < 75:
            return "Bom início! Continue se esforçando para atingir sua meta!"
        else:
            return "Você pode melhorar! Não desista e continue se exercitando!"

def cadastrarPessoa():
    print('Cadastro de Pessoa')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    altura = float(input('Informe a altura (em metros): '))
    peso = float(input('Informe o peso (em kg): '))

    pessoa = Pessoa(nome, idade, altura, peso)

    imc = pessoa.calcularIMC()
    print(f'O IMC de {pessoa.nome} é: {imc:.2f}')

    classificacaoIMC = ''
    match imc:
        case imc if imc < 18.5:
            classificacaoIMC = 'Abaixo do peso'
        case imc if 18.5 <= imc < 25:
            classificacaoIMC = 'Peso normal'
        case imc if 25 <= imc < 30:
            classificacaoIMC = 'Sobrepeso'
        case imc if 30 <= imc < 35:
            classificacaoIMC = 'Obesidade grau I'
        case imc if 35 <= imc < 40:
            classificacaoIMC = 'Obesidade grau II'
        case _:
            classificacaoIMC = 'Obesidade de grau III'

    print(f'Classificação do IMC: {classificacaoIMC}')

    print('Exercícios Recomendados:')
    for exercicio in pessoa.recomendarExercicios():
        print('- ', exercicio)

    print(f'Carga horária mínima semanal de exercícios: {pessoa.cargaHorariaMinima()} horas')

    return pessoa

def exibirPessoas(pessoas):
    print('Informações das Pessoas Cadastradas:')
    for nome, info in pessoas.items():
        print(f'Nome: {nome}')
        print(f'Idade: {info["idade"]}')
        print(f'Altura: {info["altura"]} m')
        print(f'Peso: {info["peso"]} kg')
        print(f'IMC: {info["imc"]:.2f}')
        print('Exercícios Recomendados:')
        for exercicio in info['exerciciosRecomendados']:
            print('- ', exercicio)
        print(f'Carga horária mínima semanal de exercícios: {info["cargaHorariaMinima"]} horas')
        print(f'Horas de exercícios realizadas na semana: {info["totalHorasAtividades"]} horas')
        print(f'Porcentagem da meta atingida: {info["porcentagemMeta"]:.2f}%')
        print(f'Mensagem Motivacional: {info["mensagemMotivacional"]}')
        print()

def cadastrarAtividade(pessoas):
    nome = input('Digite o nome da pessoa para registrar a atividade: ')

    if nome in pessoas:
        horas = float(input('Digite a quantidade de horas de exercícios realizados: '))
        pessoas[nome]['pessoa'].registrarAtividade(horas)
        pessoas[nome]['totalHorasAtividades'] = pessoas[nome]['pessoa'].totalHorasAtividades()
        pessoas[nome]['porcentagemMeta'] = pessoas[nome]['pessoa'].porcentagemMeta()
        pessoas[nome]['mensagemMotivacional'] = pessoas[nome]['pessoa'].mensagemMotivacional()
        print('Atividade registrada com sucesso!')
    else:
        print('Pessoa não encontrada.')

def main():
    pessoas = {}

    while True:
        print('\nMenu:')
        print('1. Cadastrar Pessoa')
        print('2. Exibir Pessoas Cadastradas')
        print('3. Cadastrar Atividade')
        print('4. Sair')

        opcao = int(input('Digite a opção desejada (1-4): '))
        match opcao:
            case 1:
                pessoa = cadastrarPessoa()
                pessoas[pessoa.nome] = {
                    'pessoa': pessoa,
                    'idade': pessoa.idade,
                    'altura': pessoa.altura,
                    'peso': pessoa.peso,
                    'imc': pessoa.calcularIMC(),
                    'exerciciosRecomendados': pessoa.recomendarExercicios(),
                    'cargaHorariaMinima': pessoa.cargaHorariaMinima(),
                    'totalHorasAtividades': pessoa.totalHorasAtividades(),
                    'porcentagemMeta': pessoa.porcentagemMeta(),
                    'mensagemMotivacional': pessoa.mensagemMotivacional()
                }
            case 2:
                exibirPessoas(pessoas)
            case 3:
                cadastrarAtividade(pessoas)
            case 4:
                print('Encerrando o programa...')
                break
            case _:
                print('Opção Inválida. Tente novamente')

if __name__ == '__main__':
    main()
