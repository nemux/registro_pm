import os
from random import randrange

from flask import Flask, request, jsonify, render_template
from flask_basicauth import BasicAuth
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')
app.config['BASIC_AUTH_FORCE'] = os.environ.get('BASIC_AUTH_FORCE')

db = SQLAlchemy(app)

from models import MoralPerson

basic_auth = BasicAuth(app)

parser = reqparse.RequestParser()
# Caratula
parser.add_argument('rfc', type=int, help='RFC')


# CreateClient
@app.route("/CreateClient",methods=['POST'])
def CreateClient():
        json_data = request.get_json(force=True)

        legal_father_last_name = json_data['legal_father_last_name']
        legal_mother_last_name = json_data['legal_mother_last_name']
        legal_first_name = json_data['legal_first_name']
        legal_second_name = json_data['legal_second_name']
        legal_birthday = json_data['legal_birthday']
        legal_gender = json_data['legal_gender']
        legal_birth_country = json_data['legal_birth_country']
        legal_birth_state = json_data['legal_birth_state']
        legal_nationality = json_data['legal_nationality']
        legal_curp = json_data['legal_curp']
        legal_tel = json_data['legal_tel']
        legal_email = json_data['legal_email']
        business_name = json_data.get('business_name',"")
        business_rfc = json_data['business_rfc']
        business_address_type = json_data['business_address_type']
        business_zipcode = json_data['business_zipcode']
        business_state = json_data['business_state']
        business_county = json_data['business_county']
        business_neighborhood = json_data['business_neighborhood']
        business_city = json_data['business_city']
        business_street = json_data['business_street']
        product_type = json_data['product_type']
        product_id = int(json_data['product_id'])

        if product_id == 3000 or product_id == 3100:
            try:
                persona_moral = MoralPerson(legal_first_name, legal_second_name, legal_father_last_name,
                                            legal_mother_last_name,
                                            legal_birthday, legal_gender, legal_birth_country, legal_birth_state,
                                            legal_nationality,
                                            legal_curp, legal_tel, legal_email, business_name, business_rfc,
                                            business_address_type,
                                            business_zipcode, business_state, business_county, business_neighborhood,
                                            business_city,
                                            business_street, product_type, product_id, "", "",
                                            "", "", "")
                db.session.add(persona_moral)
                db.session.commit()
                return "Persona Moral added. book RFC={}".format(persona_moral.business_rfc)
            except Exception as e:
                return (str(e))


# CreateClient
@app.route("/UpdateClient/",methods=['GET', 'POST'])
def UpdateClient():
    if request.method == 'POST':
        rfc = request.form.get('business_rfc')
        application_id = request.form.get('application_id')
        id_cliente = request.form.get('id_cliente')
        numero_cuenta_evva = request.form.get('numero_cuenta_evva')
        clabe = request.form.get('clabe')
        business_name = request.form.get('business_name')
        fecha_apertura = request.form.get('fecha_apertura')
        legal_first_name = request.form.get('legal_first_name')
        legal_second_name = request.form.get('legal_second_name')
        legal_father_last_name = request.form.get('legal_father_last_name')
        legal_mother_last_name = request.form.get('legal_mother_last_name')

        try:
            persona_moral = MoralPerson.query.filter_by(business_rfc=rfc).first()

            if persona_moral is None:
                persona_moral = MoralPerson(legal_first_name, legal_second_name, legal_father_last_name, legal_mother_last_name,
                                            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                            id_cliente, numero_cuenta_evva, clabe, fecha_apertura, application_id)

                db.session.add(persona_moral)
                db.session.commit()
            else:
                persona_moral.legal_first_name = legal_first_name
                persona_moral.legal_second_name = legal_second_name
                persona_moral.legal_father_last_name = legal_father_last_name
                persona_moral.legal_mother_last_name = legal_mother_last_name
                persona_moral.id_cliente = id_cliente
                persona_moral.business_name = business_name
                persona_moral.numero_cuenta_evva = numero_cuenta_evva
                persona_moral.clabe = clabe
                persona_moral.fecha_apertura = fecha_apertura
                persona_moral.application_id = application_id

            db.session.add(persona_moral)
            db.session.commit()
            return "Persona Moral Updated OK . book RFC={}".format(persona_moral.business_rfc)

        except Exception as e:
            return (str(e))
    return render_template("MoralPerson.html")


# Caratula
@app.route("/Caratula/<rfc>", methods=['GET'])
def Caratula(rfc):
    try:
        persona_moral = MoralPerson.query.filter_by(business_rfc=rfc).first()
        return jsonify(persona_moral.serialize())
    except Exception as e:
        return (str(e))

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'), host="0.0.0.0", port=80)
