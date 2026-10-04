# Pre-Entrega Automation Testing - SauceDemo

## Propósito del proyecto

La finalidad de esta pre-entrega es automatizar distintas pruebas de navegación web del sitio SauceDemo utilizando: Selenium WebDriver, Python y Pytest.

La automatización permite validar el inicio de sesión, la navegación del catálogo de productos y la interacción con el carrito de compras.

## 1 - Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- WebDriver Manager
- Git y GitHub

## 2 - Estructura del proyecto

Pre entrega/
│
├── reports/
│
├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   └── helpers.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
└── README.md

## 3 - Casos de prueba

### 3.1 - Navegación y Login

Se verifica el acceso al sitio y el inicio de sesión con un usuario válido.

Se valida:

- Navegación a la página de login.
- Ingreso de usuario `standard_user`.
- Ingreso de contraseña `secret_sauce`.
- Redirección a `/inventory.html`.

### 3.2 - Catálogo

Se verifica que la página de productos cargue correctamente.

Se valida:

- Título de la página `Swag Labs`.
- Título de la sección `Products`.
- Presencia de productos visibles.
- Presencia del menú.
- Presencia del filtro.
- Nombre del primer producto.
- Precio del primer producto.

### 3.3 - Carrito

Se verifica la interacción con el carrito de compras.

Se valida:

- Agregar el primer producto al carrito.
- Cambio del botón a `Remove`.
- Contador del carrito en `1`.
- Navegación al carrito.
- Presencia del producto agregado en el carrito.

## 4 - Instalación de dependencias

Desde la carpeta del proyecto ejecutar:

pip install selenium pytest pytest-html webdriver-manager

## 5 - Ejecución de las pruebas

Para ejecutar las pruebas:

python -m pytest tests/test_saucedemo.py -v

Para mostrar también los mensajes `print` durante la ejecución:

python -m pytest tests/test_saucedemo.py -v -s

## 6 - Generación del reporte HTML

Para generar el reporte HTML de las pruebas:
python -m pytest Tests/test_saucedemo.py -v --html=reports/Report.html

El reporte se guarda dentro de la carpeta `reports`.

## 7 - Resultado de las pruebas

El proyecto contiene 11 casos de prueba correspondientes a los puntos solicitados en la pre-entrega.

Las pruebas se ejecutan manteniendo la misma sesión del navegador para conservar el estado entre los diferentes casos.
