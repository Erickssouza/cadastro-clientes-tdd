import pytest
from src.cliente_service import ClienteService

def test_criar_cliente():
    service = ClienteService()
    cliente = service.criar(1, "Ana Silva", "ana@email.com")
    assert cliente["nome"] == "Ana Silva"
    assert len(service.listar()) == 1

def test_nao_deve_criar_cliente_com_email_invalido():
    service = ClienteService()
    with pytest.raises(ValueError, match="E-mail inválido"):
        service.criar(1, "João", "email_sem_arroba")
 
def test_buscar_cliente_por_id():
    service = ClienteService()
    service.criar(1, "Carlos", "carlos@email.com")
    encontrado = service.buscar(1)
    assert encontrado["email"] == "carlos@email.com"

def test_atualizar_cliente():
    service = ClienteService()
    service.criar(1, "Mariana", "mari@email.com")
    atualizado = service.atualizar(1, nome="Mariana Costa")
    assert atualizado["nome"] == "Mariana Costa"

def test_remover_cliente():
    service = ClienteService()
    service.criar(1, "Pedro", "pedro@email.com")
    assert service.remover(1) is True
    assert service.buscar(1) is None        