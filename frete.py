TAXA_PADRAO = 15.00
LIMITE_FRETE_GRATIS = 250.00


def calcular_frete(subtotal: float) -> float:
    if subtotal >= LIMITE_FRETE_GRATIS:
        return 0.00
    return TAXA_PADRAO

def confirmar_frete(pedido_id, regiao, subtotal, usuario, logistica, notificacao):
    taxa = logistica.consultar_taxa(regiao)
    frete = 0.00 if subtotal >= LIMITE_FRETE_GRATIS else taxa
    notificacao.enviar_notificacao_rastreio(pedido_id)
    return frete