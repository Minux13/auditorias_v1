from app import db
from sqlalchemy import event

class Auditoria(db.Model):
    __tablename__ = 'auditoria'

    id                          = db.Column(db.Integer, primary_key=True)
    tipo_auditoria_id           = db.Column(db.Integer, db.ForeignKey('tipo_auditoria.id'), nullable=True)
    organo_fiscalizador_id      = db.Column(db.Integer, db.ForeignKey('organo_fiscalizador.id'), nullable=True)
    anio_cuenta_publica         = db.Column(db.DateTime, nullable=True)
    num_auditoria               = db.Column(db.String(80), nullable=True)
    tipo_entidad_id             = db.Column(db.Integer, db.ForeignKey('tipo_entidad.id'), nullable=True)
    entidad_id                  = db.Column(db.Integer, db.ForeignKey('entidad.id'), nullable=True)
    estatus_auditoria_id        = db.Column(db.Integer, db.ForeignKey('estatus_auditoria.id'), nullable=True)
    fondo_id                    = db.Column(db.Integer, db.ForeignKey('fondo.id'), nullable=True)
    inicio                      = db.Column(db.DateTime, nullable=True)
    cierre                      = db.Column(db.DateTime, nullable=True)
    municipio_id                = db.Column(db.Integer, db.ForeignKey('municipios.id'), nullable=True) 
    obra                        = db.Column(db.String(150), nullable=True)
    accion_id                   = db.Column(db.Integer, db.ForeignKey('acciones.id'), nullable=True) 
    observacion_id              = db.Column(db.Integer, db.ForeignKey('observaciones.id'), nullable=True)
    estatus_observacion_id      = db.Column(db.Integer, db.ForeignKey('estatus_observacion.id'), nullable=True)
    clasificacion_id            = db.Column(db.Integer, db.ForeignKey('clasificaciones.id'), nullable=True)
    tipo_id                     = db.Column(db.Integer, db.ForeignKey('tipos.id'), nullable=True)
    observado                   = db.Column(db.Float, nullable=True)
    solventado                  = db.Column(db.Float, nullable=True) 
    pendiente_solventar         = db.Column(db.Float, nullable=True)
    reintegrar                  = db.Column(db.Float, nullable=True)
    atendido                    = db.Column(db.Float, nullable=True)
    pendiente_atender           = db.Column(db.Float, nullable=True)
    notificacion_solventacion   = db.Column(db.DateTime, nullable=True)
    observaciones               = db.Column(db.Text, nullable=True)
    documentos                  = db.Column(db.Text, nullable=True)

    tipo_auditoria          = db.relationship('Tipo_auditoria',      backref=db.backref('posts', lazy=True))
    organo_fiscalizador     = db.relationship('Organo_fiscalizador', backref=db.backref('posts', lazy=True))
    tipo_entidad            = db.relationship('Tipo_entidad',        backref=db.backref('posts', lazy=True))
    entidad                 = db.relationship('Entidad',             backref=db.backref('posts', lazy=True))
    estatus_auditoria       = db.relationship('Estatus_auditoria',   backref=db.backref('posts', lazy=True))
    fondo                   = db.relationship('Fondo',               backref=db.backref('posts', lazy=True))
    municipios              = db.relationship('Municipios',          backref=db.backref('posts', lazy=True))
    accion                  = db.relationship('Acciones',            backref=db.backref('posts', lazy=True))
    observacion             = db.relationship('Observaciones',       backref=db.backref('posts', lazy=True))
    estatus_observacion     = db.relationship('Estatus_observacion', backref=db.backref('posts', lazy=True))
    clasificacion           = db.relationship('Clasificaciones',     backref=db.backref('posts', lazy=True))
    tipo                    = db.relationship('Tipos',               backref=db.backref('posts', lazy=True))


class Tipo_auditoria(db.Model):
    __tablename__ = 'tipo_auditoria'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Organo_fiscalizador(db.Model):
    __tablename__ = 'organo_fiscalizador'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Tipo_entidad(db.Model):
    __tablename__ = 'tipo_entidad'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Entidad(db.Model):
    __tablename__ = 'entidad'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Estatus_auditoria(db.Model):
    __tablename__ = 'estatus_auditoria'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Municipios(db.Model):
    __tablename__ = 'municipios'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Acciones(db.Model):
    __tablename__ = 'acciones'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Observaciones(db.Model):
    __tablename__ = 'observaciones'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Estatus_observacion(db.Model):
    __tablename__ = 'estatus_observacion'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Clasificaciones(db.Model):
    __tablename__ = 'clasificaciones'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Tipos(db.Model):
    __tablename__ = 'tipos'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Fondo(db.Model):
    __tablename__ = 'fondo'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

