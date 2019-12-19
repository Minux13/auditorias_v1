 
### Instalación (linux)

```
git clone https://github.com/Minux13/auditorias_v1.git
```
```
cd auditorias_v1
```
```
python3 -m venv env
```
```
source env/bin/activate 
```
```
pip install --upgrade pip  
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=run.py
```
```
flask db init
```
```
flask db upgrade
```
```
flask run
```

Para crear los catalogos de municipios, tipo de auditoria y organo fiscalizador ingresar a: /create_cataloges





### Añadir un elemento a un catálogo

Ingresar a la url: 

http://15.164.48.84:8080/addc/ **nombreTabla** / **id** / **valor**


En **valor** se puede ingresar palabras con espacios en blanco.

Los nombres de las tablas son:

 - Tipo_auditoria      
 - Organo_fiscalizador 
 - Tipo_entidad       
 - Entidad            
 - Estatus_auditoria  
 - Fondo              
 - Municipios         
 - Acciones            
 - Observaciones      
 - Estatus_observacion
 - Clasificaciones    
 - Tipos     



### Ver los elementos de una tabla 

La url para ver los elementos de una tabla es:

http://15.164.48.84:8080/ver_tabla/ **nombreTabla**

### Editar un elemento a un catálogo

Se editan de igual manera que para añadir un elemento pero el path de la url es ***http://15.164.48.84:8080/editc***, la url quedaría:

http://15.164.48.84:8080/editc/ **nombreTabla** / **id** / **valor**

### Eliminar un elemento de la tabla 

El path de para eliminar un elemento es ***http://15.164.48.84:8080/deletec*** y la url quedaría:

http://15.164.48.84:8080/deletec/ **nombreTabla** / **id_a_eliminar**
