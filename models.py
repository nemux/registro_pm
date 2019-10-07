from app import db

class MoralPerson(db.Model):
    __tablename__ = 'moral_persons'

    id = db.Column(db.Integer, primary_key=True)
    legal_mother_last_name = db.Column(db.String)
    legal_father_last_name = db.Column(db.String)
    legal_first_name = db.Column(db.String)
    legal_second_name = db.Column(db.String)
    legal_birthday = db.Column(db.String)
    legal_gender = db.Column(db.String)
    legal_birth_country = db.Column(db.String)
    legal_birth_state = db.Column(db.String)
    legal_nationality = db.Column(db.String)
    legal_curp = db.Column(db.String)
    legal_tel = db.Column(db.String)
    legal_email = db.Column(db.String)
    business_name = db.Column(db.String)
    business_rfc = db.Column(db.String)
    business_address_type = db.Column(db.String)
    business_zipcode = db.Column(db.String)
    business_state = db.Column(db.String)
    business_county = db.Column(db.String)
    business_neighborhood = db.Column(db.String)
    business_city = db.Column(db.String)
    business_street = db.Column(db.String)
    product_type = db.Column(db.String)
    product_id = db.Column(db.String)
    application_id = db.Column(db.String)
    id_cliente = db.Column(db.String)
    numero_cuenta_evva = db.Column(db.String)
    clabe = db.Column(db.String)
    fecha_apertura = db.Column(db.String)

    def __init__(self, business_rfc):
        self.business_rfc = business_rfc

    def __init__(self, legal_first_name, legal_second_name, legal_father_last_name, legal_mother_last_name,
                 legal_birthday, legal_gender, legal_birth_country, legal_birth_state, legal_nationality,
                 legal_curp, legal_tel, legal_email, business_name, business_rfc, business_address_type,
                 business_zipcode, business_state, business_county, business_neighborhood, business_city,
                 business_street, product_type, product_id, id_cliente, numero_cuenta_evva, clabe, fecha_apertura, application_id):

        self.legal_first_name = legal_first_name
        self.legal_second_name = legal_second_name
        self.legal_father_last_name = legal_father_last_name
        self.legal_mother_last_name = legal_mother_last_name
        self.legal_birthday = legal_birthday
        self.legal_gender = legal_gender
        self.legal_birth_country = legal_birth_country
        self.legal_birth_state = legal_birth_state
        self.legal_nationality = legal_nationality
        self.legal_curp = legal_curp
        self.legal_tel = legal_tel
        self.legal_email = legal_email
        self.business_name = business_name
        self.business_rfc = business_rfc
        self.business_address_type = business_address_type
        self.business_zipcode = business_zipcode
        self.business_state = business_state
        self.business_county = business_county
        self.business_neighborhood = business_neighborhood
        self.business_city = business_city
        self.business_street = business_street
        self.product_type = product_type
        self.product_id = product_id
        self.id_cliente = id_cliente
        self.numero_cuenta_evva = numero_cuenta_evva
        self.clabe = clabe
        self.fecha_apertura = fecha_apertura
        self.application_id = application_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'nombre_cliente': self.business_name,
            'nombre_representante_legal': self.legal_first_name + ' ' + self.legal_second_name + ' ' + self.legal_father_last_name + ' ' + self.legal_mother_last_name,
            'id_cliente': self.id_cliente,
            'numero_cuenta_evva': self.numero_cuenta_evva,
            'clabe': self.clabe,
            'fecha_apertura': self.fecha_apertura,
            'rfc': self.business_rfc,
            'application_id': self.application_id
        }