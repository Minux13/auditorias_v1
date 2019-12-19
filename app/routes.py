from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import (Auditoria,
                        Tipo_auditoria     ,  
                        Organo_fiscalizador, 
                        Tipo_entidad       , 
                        Entidad            , 
                        Estatus_auditoria  , 
                        Fondo              , 
                        Municipios         , 
                        Acciones           , 
                        Observaciones      , 
                        Estatus_observacion, 
                        Clasificaciones    , 
                        Tipos               )
import datetime


@app.route('/')
def listAuditorias():
    
    entries = Auditoria.query.all()

    
    return render_template('list.html', entries=entries )


@app.route('/add', methods=['POST', 'GET'])
def add():
    
    if request.method == 'GET':

        entries = Auditoria.query.all()
        
        tipo_auditoria      = Tipo_auditoria.query.all()       
        organo_fiscalizador = Organo_fiscalizador.query.all() 
        tipo_entidad        = Tipo_entidad.query.all()         
        entidad             = Entidad.query.all()              
        estatus_auditoria   = Estatus_auditoria.query.all()    
        fondo               = Fondo.query.all()                
        municipios          = Municipios.query.all()           
        accion              = Acciones.query.all()               
        observacion         = Observaciones.query.all()          
        estatus_observacion = Estatus_observacion.query.all()  
        clasificacion       = Clasificaciones.query.all()        
        tipo                = Tipos.query.all()                 
        
        auditoria = Auditoria(tipo_auditoria_id         = "",
                              organo_fiscalizador_id    = "",
                              anio_cuenta_publica       = "",
                              num_auditoria             = "",
                              tipo_entidad_id           = "",
                              entidad_id                = "",
                              estatus_auditoria_id      = "",
                              fondo_id                  = "",
                              inicio                    = "",
                              cierre                    = "",
                              municipio_id              = "",
                              obra                      = "",
                              accion_id                 = "",
                              observacion_id            = "",
                              estatus_observacion_id    = "",
                              clasificacion_id          = "",
                              tipo_id                   = "",
                              observado                 = "",
                              solventado                = "",
                              pendiente_solventar       = "",
                              reintegrar                = "",
                              atendido                  = "",
                              pendiente_atender         = "",
                              notificacion_solventacion = "",
                              observaciones             = "",
                              documentos                = ""
        )
        
        
        return render_template('edit.html', entries=entries, 
                                auditoria           = auditoria          ,
                                tipo_auditoria      = tipo_auditoria     , 
                                organo_fiscalizador = organo_fiscalizador, 
                                tipo_entidad        = tipo_entidad       , 
                                entidad             = entidad            ,                          
                                estatus_auditoria   = estatus_auditoria  , 
                                fondo               = fondo              , 
                                municipios          = municipios         , 
                                accion              = accion             , 
                                observacion         = observacion        , 
                                estatus_observacion = estatus_observacion, 
                                clasificacion       = clasificacion      , 
                                tipo                = tipo               
        )



    else:
        form = request.form

        tipo_auditoria_id         =  form.get('tipo_auditoria')         
        organo_fiscalizador_id    =  form.get('organo_fiscalizador')    
        anio_cuenta_publica       =  form.get('anio_cuenta_publica')       
        num_auditoria             =  form.get('num_auditoria')             
        tipo_entidad_id           =  form.get('tipo_entidad')           
        entidad_id                =  form.get('entidad')                
        estatus_auditoria_id      =  form.get('estatus_auditoria')      
        fondo_id                  =  form.get('fondo')                  
        inicio                    =  form.get('inicio')                    
        cierre                    =  form.get('cierre')                    
        municipio_id              =  form.get('municipio')              
        obra                      =  form.get('obra')                      
        accion_id                 =  form.get('accion')                 
        observacion_id            =  form.get('observacion')            
        estatus_observacion_id    =  form.get('estatus_observacion')    
        clasificacion_id          =  form.get('clasificacion')          
        tipo_id                   =  form.get('tipo')                   
        observado                 =  form.get('observado')                 
        solventado                =  form.get('solventado')                
        pendiente_solventar       =  form.get('pendiente_solventar')       
        reintegrar                =  form.get('reintegrar')                
        atendido                  =  form.get('atendido')                  
        pendiente_atender         =  form.get('pendiente_atender')         
        notificacion_solventacion =  form.get('notificacion_solventacion') 
        observaciones             =  form.get('observaciones')             
        documentos                =  form.get('documentos')                

        entry = Auditoria(
            tipo_auditoria_id         = tipo_auditoria_id         ,
            organo_fiscalizador_id    = organo_fiscalizador_id    ,
            anio_cuenta_publica       = datetime.datetime.strptime(anio_cuenta_publica, '%Y-%m-%d') if anio_cuenta_publica != "" else None, 
            num_auditoria             = num_auditoria             ,
            tipo_entidad_id           = tipo_entidad_id           ,
            entidad_id                = entidad_id                ,
            estatus_auditoria_id      = estatus_auditoria_id      ,
            fondo_id                  = fondo_id                  ,
            inicio                    = datetime.datetime.strptime(inicio, '%Y-%m-%d') if inicio != "" else None,
            cierre                    = datetime.datetime.strptime(cierre, '%Y-%m-%d') if cierre != "" else None,
            municipio_id              = municipio_id              ,
            obra                      = obra                      ,
            accion_id                 = accion_id                 ,
            observacion_id            = observacion_id            ,
            estatus_observacion_id    = estatus_observacion_id    ,
            clasificacion_id          = clasificacion_id          ,
            tipo_id                   = tipo_id                   ,
            observado                 = observado if observado != "" else None,
            solventado                = solventado if solventado != "" else None,
            pendiente_solventar       = pendiente_solventar if pendiente_solventar != "" else None,
            reintegrar                = reintegrar if reintegrar != "" else None,
            atendido                  = atendido if atendido != "" else None,
            pendiente_atender         = pendiente_atender if pendiente_atender != "" else None,
            notificacion_solventacion = datetime.datetime.strptime(notificacion_solventacion, '%Y-%m-%d') if notificacion_solventacion != "" else None,
            observaciones             = observaciones             ,
            documentos                = documentos                
        )
        
        db.session.add(entry)
        db.session.commit()

        return redirect('/')

    return "of the jedi"


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    entries = Auditoria.query.get(id)
    if request.method == 'GET': 
        entries = Auditoria.query.all()

        tipo_auditoria      = Tipo_auditoria.query.all()       
        organo_fiscalizador = Organo_fiscalizador.query.all() 
        tipo_entidad        = Tipo_entidad.query.all()         
        entidad             = Entidad.query.all()              
        estatus_auditoria   = Estatus_auditoria.query.all()    
        fondo               = Fondo.query.all()                
        municipios          = Municipios.query.all()           
        accion              = Acciones.query.all()               
        observacion         = Observaciones.query.all()          
        estatus_observacion = Estatus_observacion.query.all()  
        clasificacion       = Clasificaciones.query.all()        
        tipo                = Tipos.query.all() 

        auditoria = Auditoria.query.get(id)
        
        return render_template('edit.html', entries=entries, 
                            auditoria           = auditoria          ,
                            tipo_auditoria      = tipo_auditoria     , 
                            organo_fiscalizador = organo_fiscalizador, 
                            tipo_entidad        = tipo_entidad       , 
                            entidad             = entidad            ,                          
                            estatus_auditoria   = estatus_auditoria  , 
                            fondo               = fondo              , 
                            municipios          = municipios         , 
                            accion              = accion             , 
                            observacion         = observacion        , 
                            estatus_observacion = estatus_observacion, 
                            clasificacion       = clasificacion      , 
                            tipo                = tipo               
    )
    else:
        entry = Auditoria.query.get(id)
        if entry:
            form = request.form
            
            tipo_auditoria_id         =  form.get('tipo_auditoria')         
            organo_fiscalizador_id    =  form.get('organo_fiscalizador')    
            anio_cuenta_publica       =  form.get('anio_cuenta_publica')       
            num_auditoria             =  form.get('num_auditoria')             
            tipo_entidad_id           =  form.get('tipo_entidad')           
            entidad_id                =  form.get('entidad')                
            estatus_auditoria_id      =  form.get('estatus_auditoria')      
            fondo_id                  =  form.get('fondo')                  
            inicio                    =  form.get('inicio')                    
            cierre                    =  form.get('cierre')                    
            municipio_id              =  form.get('municipio')              
            obra                      =  form.get('obra')                      
            accion_id                 =  form.get('accion')                 
            observacion_id            =  form.get('observacion')            
            estatus_observacion_id    =  form.get('estatus_observacion')    
            clasificacion_id          =  form.get('clasificacion')          
            tipo_id                   =  form.get('tipo')                   
            observado                 =  form.get('observado')                 
            solventado                =  form.get('solventado')                
            pendiente_solventar       =  form.get('pendiente_solventar')       
            reintegrar                =  form.get('reintegrar')                
            atendido                  =  form.get('atendido')                  
            pendiente_atender         =  form.get('pendiente_atender')         
            notificacion_solventacion =  form.get('notificacion_solventacion') 
            observaciones             =  form.get('observaciones')             
            documentos                =  form.get('documentos')    

            entry.tipo_auditoria_id         = tipo_auditoria_id         
            entry.organo_fiscalizador_id    = organo_fiscalizador_id    
            entry.anio_cuenta_publica       = datetime.datetime.strptime(anio_cuenta_publica, '%Y-%m-%d') if anio_cuenta_publica != "" else None
            entry.num_auditoria             = num_auditoria             
            entry.tipo_entidad_id           = tipo_entidad_id           
            entry.entidad_id                = entidad_id                
            entry.estatus_auditoria_id      = estatus_auditoria_id      
            entry.fondo_id                  = fondo_id                  
            entry.inicio                    = datetime.datetime.strptime(inicio, '%Y-%m-%d') if inicio != "" else None
            entry.cierre                    = datetime.datetime.strptime(cierre, '%Y-%m-%d') if cierre != "" else None
            entry.municipio_id              = municipio_id              
            entry.obra                      = obra                      
            entry.accion_id                 = accion_id                 
            entry.observacion_id            = observacion_id            
            entry.estatus_observacion_id    = estatus_observacion_id    
            entry.clasificacion_id          = clasificacion_id          
            entry.tipo_id                   = tipo_id                   
            entry.observado                 = observado if observado != "" else None
            entry.solventado                = solventado if solventado != "" else None
            entry.pendiente_solventar       = pendiente_solventar if pendiente_solventar != "" else None
            entry.reintegrar                = reintegrar if reintegrar != "" else None
            entry.atendido                  = atendido if atendido != "" else None
            entry.pendiente_atender         = pendiente_atender if pendiente_atender != "" else None
            entry.notificacion_solventacion = datetime.datetime.strptime(notificacion_solventacion, '%Y-%m-%d') if notificacion_solventacion != "" else None
            entry.observaciones             = observaciones             
            entry.documentos                = documentos           
            
            db.session.commit()

            return redirect(url_for('listAuditorias'))



@app.route('/delete/<int:id>')
def delete(id):
    entry = Auditoria.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
    return redirect(url_for('listAuditorias'))



@app.route('/create_cataloges')
def createCataloges():

    existsTipoAuditoria = Tipo_auditoria.query.filter_by(id=4).first()
    if not existsTipoAuditoria:
        db.session.add(Tipo_auditoria(id=1, name="Financiera"))
        db.session.add(Tipo_auditoria(id=2, name="Desempeno"))
        db.session.add(Tipo_auditoria(id=3, name="Obra Publica"))
        db.session.add(Tipo_auditoria(id=4, name="Normativas"))
        db.session.commit()

    existsOrgano_fiscalizador = Organo_fiscalizador.query.filter_by(id=4).first()
    if not existsOrgano_fiscalizador:
        db.session.add(Organo_fiscalizador(id=1, name="ASF"))
        db.session.add(Organo_fiscalizador(id=2, name="SFP"))
        db.session.add(Organo_fiscalizador(id=3, name="ASE"))
        db.session.add(Organo_fiscalizador(id=4, name="CYTG"))
        db.session.commit()

    existsMunicipios= Municipios.query.filter_by(id=4).first()
    if not existsMunicipios:
        db.session.add( Municipios(id= 1, name= "Abasolo"))
        db.session.add( Municipios(id= 2, name= "Agualeguas"))
        db.session.add( Municipios(id= 3, name= "Los Aldamas"))
        db.session.add( Municipios(id= 4, name= "Allende"))
        db.session.add( Municipios(id= 5, name= "Anahuac"))
        db.session.add( Municipios(id= 6, name= "Apodaca"))
        db.session.add( Municipios(id= 7, name= "Aramberri"))
        db.session.add( Municipios(id= 8, name= "Bustamante"))
        db.session.add( Municipios(id= 9, name= "Cadereyta Jimenez"))
        db.session.add( Municipios(id=10, name= "Carmen"))
        db.session.add( Municipios(id=11, name= "Cerralvo"))
        db.session.add( Municipios(id=12, name= "Cienega de Flores"))
        db.session.add( Municipios(id=13, name= "China"))
        db.session.add( Municipios(id=14, name= "Dr. Arroyo"))
        db.session.add( Municipios(id=15, name= "Dr. Coss"))
        db.session.add( Municipios(id=16, name= "Dr. Gonzalez"))
        db.session.add( Municipios(id=17, name= "Galeana"))
        db.session.add( Municipios(id=18, name= "Garcia"))
        db.session.add( Municipios(id=19, name= "San Pedro Garza Garcia"))
        db.session.add( Municipios(id=20, name= "Gral. Bravo"))
        db.session.add( Municipios(id=21, name= "Gral. Escobedo"))
        db.session.add( Municipios(id=22, name= "Gral. Teran"))
        db.session.add( Municipios(id=23, name= "Gral. Trevi"))
        db.session.add( Municipios(id=24, name= "Gral. Zaragoza"))
        db.session.add( Municipios(id=25, name= "Gral. Zuazua"))
        db.session.add( Municipios(id=26, name= "Guadalupe"))
        db.session.add( Municipios(id=27, name= "Los Herreras"))
        db.session.add( Municipios(id=28, name= "Higueras"))
        db.session.add( Municipios(id=29, name= "Hualahuises"))
        db.session.add( Municipios(id=30, name= "Iturbide"))
        db.session.add( Municipios(id=31, name= "Juarez"))
        db.session.add( Municipios(id=32, name= "Lampazos de Naranjo"))
        db.session.add( Municipios(id=33, name= "Linares"))
        db.session.add( Municipios(id=34, name= "Marin"))
        db.session.add( Municipios(id=35, name= "Melchor Ocampo"))
        db.session.add( Municipios(id=36, name= "Mier y Noriega"))
        db.session.add( Municipios(id=37, name= "Mina"))
        db.session.add( Municipios(id=38, name= "Montemorelos"))
        db.session.add( Municipios(id=39, name= "Monterrey"))
        db.session.add( Municipios(id=40, name= "Paras"))
        db.session.add( Municipios(id=41, name= "Pesqueria"))
        db.session.add( Municipios(id=42, name= "Los Ramones"))
        db.session.add( Municipios(id=43, name= "Rayones"))
        db.session.add( Municipios(id=44, name= "Sabinas Hidalgo"))
        db.session.add( Municipios(id=45, name= "Salinas Victoria"))
        db.session.add( Municipios(id=46, name= "San Nicolas de los Garza"))
        db.session.add( Municipios(id=47, name= "Hidalgo"))
        db.session.add( Municipios(id=48, name= "Santa Catarina"))
        db.session.add( Municipios(id=49, name= "Santiago"))
        db.session.add( Municipios(id=50, name= "Vallecillo"))
        db.session.add( Municipios(id=51, name= "Villaldama"))
        db.session.commit()

    return "Catalogos creados"



@app.route('/addc/<tablename>/<int:idv>/<value>', methods=['GET'])
def addCatalog(tablename, idv, value):

    catalogos = {
        "Tipo_auditoria":      Tipo_auditoria      ,  
        "Organo_fiscalizador": Organo_fiscalizador , 
        "Tipo_entidad":        Tipo_entidad        ,
        "Entidad":             Entidad             ,
        "Estatus_auditoria":   Estatus_auditoria   ,
        "Fondo":               Fondo               ,
        "Municipios":          Municipios          ,
        "Acciones":            Acciones            ,
        "Observaciones":       Observaciones       ,
        "Estatus_observacion": Estatus_observacion ,
        "Clasificaciones":     Clasificaciones     ,
        "Tipos":               Tipos               
    }

    db.session.add( catalogos[tablename](id=idv, name= value))
    db.session.commit()

    entradas = catalogos[tablename].query.all()
    strEntrada = '<strong>Tabla: </strong>' + tablename + '<br><br>'
    for e in entradas:
        strEntrada = strEntrada + '<strong>id:</strong> ' + str(e.id) + '<strong> name:</strong> ' + e.name + '<br>'

    return strEntrada


@app.route('/editc/<tablename>/<int:idv>/<value>', methods=['GET'])
def editCatalog(tablename, idv, value):

    catalogos = {
        "Tipo_auditoria":      Tipo_auditoria      ,  
        "Organo_fiscalizador": Organo_fiscalizador , 
        "Tipo_entidad":        Tipo_entidad        ,
        "Entidad":             Entidad             ,
        "Estatus_auditoria":   Estatus_auditoria   ,
        "Fondo":               Fondo               ,
        "Municipios":          Municipios          ,
        "Acciones":            Acciones            ,
        "Observaciones":       Observaciones       ,
        "Estatus_observacion": Estatus_observacion ,
        "Clasificaciones":     Clasificaciones     ,
        "Tipos":               Tipos               
    }

    entry = catalogos[tablename].query.get(idv)
    entry.name = value
    db.session.commit()

    entradas = catalogos[tablename].query.all()
    strEntrada = '<strong>Tabla: </strong>' + tablename + '<br><br>'
    for e in entradas:
        strEntrada = strEntrada + '<strong>id:</strong> ' + str(e.id) + '<strong> name:</strong> ' + e.name + '<br>'

    return strEntrada




@app.route('/deletec/<tablename>/<int:idv>', methods=['GET'])
def deleteCatalog(tablename, idv):

    catalogos = {
        "Tipo_auditoria":      Tipo_auditoria      ,  
        "Organo_fiscalizador": Organo_fiscalizador , 
        "Tipo_entidad":        Tipo_entidad        ,
        "Entidad":             Entidad             ,
        "Estatus_auditoria":   Estatus_auditoria   ,
        "Fondo":               Fondo               ,
        "Municipios":          Municipios          ,
        "Acciones":            Acciones            ,
        "Observaciones":       Observaciones       ,
        "Estatus_observacion": Estatus_observacion ,
        "Clasificaciones":     Clasificaciones     ,
        "Tipos":               Tipos               
    }

    entry = catalogos[tablename].query.get(idv)
    db.session.delete(entry)
    db.session.commit()

    entradas = catalogos[tablename].query.all()
    strEntrada = '<strong>Tabla: </strong>' + tablename + '<br><br>'
    for e in entradas:
        strEntrada = strEntrada + '<strong>id:</strong> ' + str(e.id) + '<strong> name:</strong> ' + e.name + '<br>'

    return strEntrada




@app.route('/ver_tabla/<tablename>', methods=['GET'])
def verTabla(tablename):

    catalogos = {
        "Tipo_auditoria":      Tipo_auditoria      ,  
        "Organo_fiscalizador": Organo_fiscalizador , 
        "Tipo_entidad":        Tipo_entidad        ,
        "Entidad":             Entidad             ,
        "Estatus_auditoria":   Estatus_auditoria   ,
        "Fondo":               Fondo               ,
        "Municipios":          Municipios          ,
        "Acciones":            Acciones            ,
        "Observaciones":       Observaciones       ,
        "Estatus_observacion": Estatus_observacion ,
        "Clasificaciones":     Clasificaciones     ,
        "Tipos":               Tipos               
    }

    entradas = catalogos[tablename].query.all()
    strEntrada = '<strong>Tabla: </strong>' + tablename + '<br><br>'
    for e in entradas:
        strEntrada = strEntrada + '<strong>id:</strong> ' + str(e.id) + '<strong> name:</strong> ' + e.name + '<br>'

    return strEntrada
