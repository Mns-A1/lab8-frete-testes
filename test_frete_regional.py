from frete import calcular_frete_regional


def test_norte_abaixo_de_300_cobra_taxa_adicional():
    # Arrange
    subtotal = 100.00

    # Act
    frete = calcular_frete_regional(subtotal, "Norte")

    # Assert
    assert frete == 25.00


def test_nordeste_abaixo_de_300_cobra_taxa_adicional():
    # Arrange
    subtotal = 280.00

    # Act
    frete = calcular_frete_regional(subtotal, "Nordeste")

    # Assert
    assert frete == 25.00


def test_norte_exatamente_300_ainda_cobra_frete():
    # Arrange
    subtotal = 300.00

    # Act
    frete = calcular_frete_regional(subtotal, "Norte")

    # Assert
    assert frete == 25.00


def test_nordeste_acima_de_300_frete_gratis():
    # Arrange
    subtotal = 300.01

    # Act
    frete = calcular_frete_regional(subtotal, "Nordeste")

    # Assert
    assert frete == 0.00


def test_outras_regioes_mantem_regra_padrao():
    # Arrange
    subtotal = 100.00

    # Act
    frete = calcular_frete_regional(subtotal, "Sudeste")

    # Assert
    assert frete == 15.00