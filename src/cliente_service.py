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