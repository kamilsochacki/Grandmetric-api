from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



additional_service_put_args = reqparse.RequestParser()
additional_service_put_args.add_argument("reservation_id", type=int, help="identyfikator rezerwacji, z którą związana jest usługa", required=True)
additional_service_put_args.add_argument("name", type=str, help="nazwa danej usługi (np. sprzątanie, parking podziemny itp)", required=True)
additional_service_put_args.add_argument("unit_price", type=str, help="cena jednostkowa za usługę", required=True)
additional_service_put_args.add_argument("date_from", type=str, help="data rozpoczęcia świadczenia usługi", required=True)
additional_service_put_args.add_argument("date_to", type=str, help="data zakończenia świadczenia usługi", required=True)

id = 2 #id dodatkowych uslug 0 i 1 zajete dla testu

additional_services_list = {
            0: {"data": "USLUGA TESTOWA 0",
                "reservation_id": 10,
                "name": "sprzatanie",
                "unit_price": 1000.00,
                "date_from": "01.01.2021",
                "date_to": "31.03.2021"},
            1: {"data": "USLUGA TESTOWA 1",
                "reservation_id": 10,
                "name": "sprzatanie",
                "unit_price": 1000.00,
                "date_from": "01.01.2021",
                "date_to": "31.03.2021"}
                            }

class AdditionalServiceById(Resource):

    def get(self, service_id):

        return additional_services_list[service_id]




class AdditionalServices(Resource):

    def get(self):
        return additional_services_list

    def put(self):
        global id
        new_service_id = id
        args = additional_service_put_args.parse_args()
        id += 1
        print("\nAdded new service:",  args)
        print("New service ID is:", new_service_id)
        additional_services_list[new_service_id] = args

        return additional_services_list[new_service_id], 201



api.add_resource(AdditionalServiceById, "/v1/additionalservice/<int:service_id>")
api.add_resource(AdditionalServices, "/v1/additionalservice")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)

