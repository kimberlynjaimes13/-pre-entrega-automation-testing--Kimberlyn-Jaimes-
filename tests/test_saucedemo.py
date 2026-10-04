from selenium.webdriver.common.by import By

from utils.helpers import navegar_login


def test_01_navegar_login(driver):
    navegar_login(driver)

    assert "saucedemo.com" in driver.current_url, "ERROR: No se navegó a la página de login de SauceDemo"


def test_02_ingresar_credenciales(driver):
    usuario = driver.find_element(By.ID, "user-name")
    contraseña = driver.find_element(By.ID, "password")

    usuario.send_keys("standard_user")
    contraseña.send_keys("secret_sauce")

    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()


def test_03_validar_login_exitoso(driver):
    assert "/inventory.html" in driver.current_url, "ERROR: No se redirigió a /inventory.html"


def test_04_validar_titulos(driver):
    page_title = driver.title

    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs", f'ERROR: Título de ventana esperado "Swag Labs", obtenido {page_title}'

    assert section_title == "Products", f'ERROR: El título de la sección esperado "Products", obtenido {section_title}'


def test_05_verificar_productos_visibles(driver):
    inventory_item = driver.find_elements( By.CLASS_NAME, "inventory_item")

    assert len(inventory_item) > 0, "ERROR: No se encontraron productos visibles"

def test_06_verificar_elementos_interfaz(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn")

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(),"ERROR: El menú no está visible"

    assert filtro.is_displayed(), "ERROR: El filtro no está visible"


def test_07_verificar_nombre_precio_primer_producto(driver):
    inventory_item = driver.find_elements( By.CLASS_NAME, "inventory_item")

    first_item = inventory_item[0]

    nombre_producto = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text

    precio_producto = first_item.find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"Primer producto: {nombre_producto}")
    print(f"Precio: {precio_producto}")

    assert nombre_producto != "", "ERROR: El nombre del producto está vacío"

    assert precio_producto != "", "ERROR: El precio del producto está vacío"


def test_08_anadir_producto_carrito(driver):
    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    boton_agregar = first_item.find_element(By.TAG_NAME, "button")

    boton_agregar.click()

    assert boton_agregar.text.capitalize() == "Remove", "ERROR: El nombre del botón no cambió a Remove"


def test_09_verificar_contador_carrito(driver):
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert contador_carrito == "1", f"ERROR: Se esperaba 1, se obtuvo {contador_carrito}"


def test_10_navegar_carrito(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

    assert "/cart.html" in driver.current_url, "ERROR: No se redirigió a /cart.html"


def test_11_comprobar_producto_carrito(driver):
    producto_nombre_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert producto_nombre_en_carrito == "Sauce Labs Backpack", 'ERROR: No se encontró el producto "Sauce Labs Backpack"'
