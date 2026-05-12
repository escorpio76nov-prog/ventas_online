# Ventas Online

Sitio web de ventas online de productos de importación.

---

# Funcionalidades

## Usuarios

- Registro
- Login
- Logout
- Perfil de usuario
- Edición de perfil
- Avatar
- Mensajería entre usuarios

---

## Productos

- Listado de productos
- Detalle de producto
- Crear producto
- Editar producto
- Eliminar producto
- Búsqueda de productos
- Opiniones de clientes

---

## Carrito y pagos

- Carrito de compras
- Agregar productos
- Eliminar productos
- Integración con Mercado Pago

---
## Perfiles
 - Solo el superuser puede:
    agregar productos nuevos
    borrar/editar/modificar

# Tecnologías utilizadas

- Python
- asgiref            3.11.1
- certifi            2026.4.22
- charset-normalizer 3.4.7
- Django             6.0.4
- django-ckeditor    6.7.3
- django-js-asset    3.1.2
- idna               3.14
- mercadopago        2.4.0
- pillow             12.2.0
- pip                26.1.1
- requests           2.33.1
- sqlparse           0.5.5
- tzdata             2026.2
- urllib3            2.7.0

## Start de app
- django-admin startproject ventas .     
- python  manage.py startapp productos
- python  manage.py startapp cuentas
- python  manage.py startapp mensajes

## Levantar sitio local
- python manage.py runserver    

# Función MercadoPago
- Instalar ngrok
- Levantar el server en el port 8000 : comando ngrok http 8000
    realizará Forwarding de http://localhost:8000 a https://stinger-cymbal-unmade.ngrok-free.dev
    Si la dirección https no es la misma reemplazarla en view.py de app productos función pagar

## Rutas:

/
- Registro
/cuentas/signup/

- Login
/cuentas/login/

- Productos
/pages/

- Buscar productos
/buscar/

- Perfil
/accounts/profile/

- Mensajes
/mensajes/

- Carrito
/carrito/

- Superusuario
/admin/


