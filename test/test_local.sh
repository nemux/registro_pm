echo "##################################################"
echo "Test Post - CreateClient"
http POST http://127.0.0.1/CreateClient \
Authorization:'Basic  Y2hFamlzdFVzOGlDckBqbzMyMzQ6ZnJpeVV2dURhWWE2ZUIwZUhpJmlxOGZ1NjF5RWYhcnUxaCstbEZyZWY4cyplemFWYTlPRGx3JEVKMXpBNmxjMQ==' \
legal_mother_last_name=AA   \
legal_father_last_name=AA   \
legal_first_name=AAA   \
legal_second_name=GGF   \
legal_birthday=1980-28-12   \
legal_gender=MALE   \
legal_birth_country=MX   \
legal_birth_state=COL   \
legal_nationality=MX   \
legal_curp=LACURP67   \
legal_tel=1234567890 \
legal_email=mymail@example.com   \
business_rfc=ZUMILSD6LC4   \
business_address_type=OK   \
business_zipcode=66001   \
business_state=OK   \
business_county=MX   \
business_neighborhood=FUNLAND   \
business_city=MX   \
business_street=ST   \
product_type=654   \
product_id=12
echo "##################################################"
echo "Test Post - CreateClient"
http POST http://127.0.0.1/CreateClient \
Authorization:'Basic  Y2hFamlzdFVzOGlDckBqbzMyMzQ6ZnJpeVV2dURhWWE2ZUIwZUhpJmlxOGZ1NjF5RWYhcnUxaCstbEZyZWY4cyplemFWYTlPRGx3JEVKMXpBNmxjMQ==' \
legal_mother_last_name=AA   \
legal_father_last_name=AA   \
legal_first_name=AAA   \
legal_second_name=GGF   \
legal_birthday=1980-28-12   \
legal_gender=MALE   \
legal_birth_country=MX   \
legal_birth_state=COL   \
legal_nationality=MX   \
legal_curp=LACURP67   \
legal_tel=1234567890 \
legal_email=mymail@example.com   \
business_rfc=ZUMILSD6LC4   \
business_address_type=OK   \
business_zipcode=66001   \
business_state=OK   \
business_county=MX   \
business_neighborhood=FUNLAND   \
business_city=MX   \
business_street=ST   \
product_type=654abc   \
product_id=3100
echo "##################################################"
echo "Test Get - Caratula by RFC"
http GET http://127.0.0.1/Caratula/ZUMILSD6LCxxx4 \
Authorization:'Basic  Y2hFamlzdFVzOGlDckBqbzMyMzQ6ZnJpeVV2dURhWWE2ZUIwZUhpJmlxOGZ1NjF5RWYhcnUxaCstbEZyZWY4cyplemFWYTlPRGx3JEVKMXpBNmxjMQ==' \
