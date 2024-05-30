# Consigna

Implementar el borrado de usuarios.

Para esto debe respetar el modelo MVC, o sea:
- Si pasa datos entre vista, controlador y modelo, debe ser utilizando DTOs.
- Las responsabilidades de visualizar van a la capa de vistas.
- Las responsabilidades de atender pedidos van a la capa de controladores.
- Las responsabilidades de almacenado y recuperacion de datos van a la capa de modelos.

Para implementar el borrado debe agregar una nueva opcion en el menu antes de loguearse, que sea "Baja de usuario". Un usuario solamente puede borrarse a si mismo, por lo que es necesario que ingresar sus credenciales. La base de datos de texto debe reflejar el borrado de usuarios, asi cuando se reinicia el programa, todo usuario borrado permanece borrado, similar a lo que ocurre con los contactos.

# Entrega

Se debe entregar en un unico archivo .zip el codigo modificado, funcionando.

# Evaluacion

El trabajo estara bien siempre que desde el punto de vista del usuario se observe el comportamiento pedido, se respeten la responsabilidades de cada una de las capas y se pasen los datos con DTOs. Cualquier manera en que se quiera implementar, dentro de este marco, y respetando las buenas practicas de programacion, sera aceptada.
