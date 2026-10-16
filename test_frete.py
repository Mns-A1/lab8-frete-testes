from frete import calcular_frete


def test_frete_padrao_para_carrinho_abaixo_de_250():
    # Arrange
    subtotal = 249.99

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == 15.00


def test_frete_gratis_para_carrinho_igual_a_250():
    # Arrange
    subtotal = 250.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == 0.00


def test_frete_gratis_para_carrinho_acima_de_250():
    # Arrange
    subtotal = 400.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == 0.00