from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:8000")

    # TESTE 1 - Verificar título
    titulo = driver.find_element(By.TAG_NAME, "h1")
    assert titulo.text == "♻️ CittaLixo"
    print("✅ Teste 1 aprovado - Título")

    # TESTE 2 - Verificar mapa
    mapa = driver.find_element(By.ID, "map")
    assert mapa.is_displayed()
    print("✅ Teste 2 aprovado - Mapa")

    # TESTE 3 - Verificar quantidade de cards
    cards = driver.find_elements(By.CLASS_NAME, "card")
    assert len(cards) == 2
    print("✅ Teste 3 aprovado - Cards")

    # TESTE 4 - Verificar Ecoponto Centro
    assert "Ecoponto Centro" in driver.page_source
    print("✅ Teste 4 aprovado - Ecoponto Centro")

    # TESTE 5 - Verificar endereço do Ecoponto Centro
    assert "Rua do Sol, 100" in driver.page_source
    print("✅ Teste 5 aprovado - Endereço Ecoponto Centro")

    # TESTE 6 - Verificar Ecoponto Bairro Novo
    assert "Ecoponto Bairro Novo" in driver.page_source
    print("✅ Teste 6 aprovado - Ecoponto Bairro Novo")

    print("\n🎉 Todos os testes passaram!")

finally:
    driver.quit()