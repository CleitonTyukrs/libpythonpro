def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario=Usuario(nome='Cleiton')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rool_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios=[Usuario(nome='Cleiton'), Usuario(nome='Sousa')]
    for usuario in usuarios
        sessao.salvar(usuario)
        sessao.salvar(usuario)
    assert usuario == sessao.listar()
    sessao.rool_back()
    sessao.fechar()
    conexao.fechar()

