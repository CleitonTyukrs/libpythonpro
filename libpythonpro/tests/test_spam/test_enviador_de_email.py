from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None
def test_remetente():
    enviador = Enviador()
    enviador.enviar(
        'renzo@python.pro.br',
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma guido con Rossum aberta.'
    )
    assert 'renzo@python.pro.br' in resultado