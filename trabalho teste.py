class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError("Nota deve estar entre 0 e 10")

    def calcular_media(self):
        if not self.notas:
            raise ValueError(f"Aluno {self.nome} ainda não tem notas registradas.")
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        raise NotImplementedError("Método aprovado não implementado")


class AlunoEnsinoMedio(Aluno):
    def aprovado(self):
        media = self.calcular_media()
        return media >= 6


class AlunoGraduacao(Aluno):
    def aprovado(self):
        media = self.calcular_media()
        return media >= 7


class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self.titulacao = titulacao

    def obter_informacoes(self):
        return f"Professor {self.nome}, Titulação: {self.titulacao}"


def verificar_aprovacao(aluno):
    try:
        media = aluno.calcular_media()
        aprovado = "Aprovado" if aluno.aprovado() else "Reprovado"
        return f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Média: {media}, Status: {aprovado}"
    except ValueError as e:
        return f"Erro: {e}"


aluno_ensino_medio = AlunoEnsinoMedio("João Silva", "12345")
aluno_ensino_medio.adicionar_nota(7)
aluno_ensino_medio.adicionar_nota(8)

aluno_graduacao = AlunoGraduacao("Maria Oliveira", "54321")
aluno_graduacao.adicionar_nota(6)
aluno_graduacao.adicionar_nota(5)

professor = Professor("Dr. Paulo Santos", "Doutorado")

print(verificar_aprovacao(aluno_ensino_medio))
print(verificar_aprovacao(aluno_graduacao))
print(professor.obter_informacoes())
