class ServicoLogisticaAPI:
    def consultar_taxa(self, regiao: str) -> float:
        raise NotImplementedError("Chamada de rede real, não usar em testes")


class ServicoNotificacao:
    def enviar_notificacao_rastreio(self, pedido_id: str) -> None:
        raise NotImplementedError("Envio real, não usar em testes")