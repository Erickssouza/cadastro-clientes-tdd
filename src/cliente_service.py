class ClienteService:
    """Serviço responsável pelas operações de CRUD de clientes em memória."""

    def __init__(self):
        """Inicializa o repositório em memória de clientes."""
        self.clientes = {}

    def criar(self, id_cliente: int, nome: str, email: str) -> dict:
        """
        Cadastra um novo cliente após validar o e-mail.

        Args:
            id_cliente (int): Identificador único do cliente.
            nome (str): Nome completo do cliente.
            email (str): Endereço de e-mail válido.

        Returns:
            dict: Dicionário contendo os dados do cliente criado.

        Raises:
            ValueError: Se o e-mail não contiver '@'.
        """
        if "@" not in email:
            raise ValueError("E-mail inválido")
        cliente = {"id": id_cliente, "nome": nome, "email": email}
        self.clientes[id_cliente] = cliente
        return cliente

    def listar(self) -> list:
        """Retorna a lista de todos os clientes cadastrados."""
        return list(self.clientes.values())
    
    def buscar(self, id_cliente: int) -> dict | None:
        """Busca um cliente pelo seu ID. Retorna None se não existir."""
        return self.clientes.get(id_cliente)

    def atualizar(self, id_cliente: int, nome: str = None, email: str = None) -> dict | None:
        """Atualiza o nome e/ou e-mail de um cliente existente."""
        cliente = self.buscar(id_cliente)
        if not cliente:
            return None
        if nome:
            cliente["nome"] = nome
        if email:
            if "@" not in email:
                raise ValueError("E-mail inválido")
            cliente["email"] = email
        return cliente

    def remover(self, id_cliente: int) -> bool:
        """Remove um cliente pelo ID. Retorna True se removido com sucesso."""
        if id_cliente in self.clientes:
            del self.clientes[id_cliente]
            return True
        return False