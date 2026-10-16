from unittest.mock import Mock

from frete import confirmar_frete
from servicos import ServicoLogisticaAPI, ServicoNotificacao


def test_confirmar_frete_com_test_doubles():
    # Arrange
    usuario_dummy = object()  # Dummy: só preenche a assinatura

    logistica_stub = Mock(spec=ServicoLogisticaAPI)  # Stub: resposta fixa
    logistica_stub.consultar_taxa.return_value = 22.50

    notificacao_mock = Mock(spec=ServicoNotificacao)  # Mock/Spy: verifica chamada

    pedido_id = "PED-123"

    # Act
    frete = confirmar_frete(
        pedido_id, "Sudeste", 100.00,
        usuario_dummy, logistica_stub, notificacao_mock,
    )

    # Assert
    assert frete == 22.50
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with("PED-123")