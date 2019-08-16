import os
from random import randrange

import psycopg2
from flask import Flask, request
from flask_basicauth import BasicAuth
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')
app.config['BASIC_AUTH_FORCE'] = os.environ.get('BASIC_AUTH_FORCE')

basic_auth = BasicAuth(app)

# Get String connection
db_url = os.environ.get('DATABASE_URL')
try:
    conn = psycopg2.connect(db_url)
except:
    exit(1)

#    Esquemas
esquema_pm = {
    "legal_mother_last_name": "",
    "legal_father_last_name": "",
    "legal_first_name": "",
    "legal_second_name": "",
    "legal_birthday": "",
    "legal_gender": "",
    "legal_birth_country": "",
    "legal_birth_state": "",
    "legal_nationality": "",
    "legal_curp": "",
    "legal_tel": 1234567890,
    "legal_email": "",
    "business_rfc": "",
    "business_address_type": "",
    "business_zipcode": 0,
    "business_state": "",
    "business_county": "",
    "business_neighborhood": "",
    "business_city": "",
    "business_street": "",
    "product_type": "",
    "product_id": ""
}

# Fin esquemas

parser = reqparse.RequestParser()
# Caratula
parser.add_argument('rfc', type=int, help='RFC')


# HelloWorld
class HelloWorld(Resource):
    def get(self):
        return "Hello, world! Please RTFM."


# CreateClient
class CreateClient(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        esquema_pm['legal_father_last_name'] = json_data['legal_father_last_name']
        esquema_pm['legal_mother_last_name'] = json_data['legal_mother_last_name']
        esquema_pm['legal_first_name'] = json_data['legal_first_name']
        esquema_pm['legal_second_name'] = json_data['legal_second_name']
        esquema_pm['legal_birthday'] = json_data['legal_birthday']
        esquema_pm['legal_gender'] = json_data['legal_gender']
        esquema_pm['legal_birth_country'] = json_data['legal_birth_country']
        esquema_pm['legal_birth_state'] = json_data['legal_birth_state']
        esquema_pm['legal_nationality'] = json_data['legal_nationality']
        esquema_pm['legal_curp'] = json_data['legal_curp']
        esquema_pm['legal_tel'] = json_data['legal_tel']
        esquema_pm['legal_email'] = json_data['legal_email']
        esquema_pm['business_rfc'] = json_data['business_rfc']
        esquema_pm['business_address_type'] = json_data['business_address_type']
        esquema_pm['business_zipcode'] = json_data['business_zipcode']
        esquema_pm['business_state'] = json_data['business_state']
        esquema_pm['business_county'] = json_data['business_county']
        esquema_pm['business_neighborhood'] = json_data['business_neighborhood']
        esquema_pm['business_city'] = json_data['business_city']
        esquema_pm['business_street'] = json_data['business_street']
        esquema_pm['product_type'] = json_data['product_type']
        esquema_pm['product_id'] = int(json_data['product_id'])
        p_id = esquema_pm['product_id']
        '''
        SQL Query to insert
        '''
        insert_query = f'INSERT INTO'
        if p_id == 3000 or p_id == 3100:
            # Es id valido
            print(esquema_pm)
            return {
                       # "datetime": str(datetime.datetime.now()),
                       "RFC": esquema_pm['business_rfc']
                   }, 201
        else:
            return {
                       "401": "Please RTFM"
                   }, 401


# Caratula
class Caratula(Resource):
    def get(self, rfc):
        # args = parser.parse_args()
        # rfc = args['rfc']
        cur = conn.cursor()
        # get updates
        cur.close()
        print(rfc)
        return {
                   # "datetime": str(datetime.datetime.now()),
                   "nombre_cliente": "Evva Test",
                   "nombre_representante_legal": "Representante Legal",
                   "id_cliente": randrange(1000, 156231),
                   "numero_cuenta_evva": randrange(1111239856, 9999999999),
                   "clabe": randrange(1234567898523698, 9999999999995637),
                   "fecha_apertura": "01/08/2019",
                   "rfc": rfc
               }, 200


api.add_resource(HelloWorld, '/')
api.add_resource(CreateClient, '/CreateClient')
api.add_resource(Caratula, '/Caratula/<rfc>')

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'), host="0.0.0.0", port=80)
