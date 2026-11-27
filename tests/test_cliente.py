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