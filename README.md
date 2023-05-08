# Proyecto Base de Datos PIL
Repositorio creado para realizar el trabajo solicitado en el marco de la capacitación del programa de inserción laboral (PIL) en nuevas tecnologías. Consigna del trabajosd:

Una entidad educativa se encuentra en un proceso de migración de sistemas, cuyo objetivo busca lograr la limpieza y estandarización de sus datos.
Para ello provee fuentes de datos contenidos en diferentes archivos en formato csv. Dicha entidad contrata nuestros servicios para crear una aplicación que permita la importación de los datos a una base de datos, con las siguientes consideraciones:

* Los datos insertados en las diferentes tablas deben ser únicos, por lo que se deberá revisar la consistencia y eliminar aquellos que estén repetidos. El campo de personal_id (DNI) es de tipo texto y hay que transformarlo en tipo número. 
* Cada tabla creada debe contar un un campo que haga referencia a la fecha y hora de la inserción del registro, como así también otro con la fecha y hora de modificación. 
* Se debe analizar toda la información de cada fuente de datos y diseñar un modelo de entidad / relación que permita disgregar en tablas principales y de catálogo manteniendo la respectiva relación.(ejemplo género, localidades, etc.).
* Las tablas catálogo deben ser universales, de manera que puedan ser relacionadas por mas de una tabla actual o futura.
* La solución debe ser modularizada, con el fin de poder reutilizar parte del código en futuros desarrollos sin que esto afecte su normal funcionamiento. 
* Cada función o procedimiento debe estar debidamente documentada para que cualquier equipo de desarrollo actual o futuro conozca el funcionamiento si necesidad de leer/interpretar el código. (A)
* Luego de la migración de los datos, se debe entregar reportes para respaldar la integridad de la información. 
