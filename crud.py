from customers import *
from connection import *
import json
import falcon



class CustomersResource:
#------Read------
    def on_get(self, req, resp, id=None):
        if id is None:
            list_data = []
            for customer in connection.session.query(Customers).all():
                list_data.append(Customers.to_dict(customer))
            resp.body = json.dumps(list_data)
            resp.status = falcon.HTTP_200
        else:
            user = connection.session.query(Customers).get(int(id))
            deltail = Customers.to_dict(user)
            resp.body = json.dumps(deltail)
            resp.status = falcon.HTTP_200


#------Create------
    def on_post(self, req, resp):
        body = req.media
        name = body.get('name')
        dob  = body.get('dob')
        if name is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('Data param name is required')
        elif dob is None:
            resp.status = falcon.HTTP_404
            raise falcon.HTTPBadRequest('Data dob is required')
        else:
            id_list = []
            for i in connection.session.query(Customers).all():
                id_list.append(i.id)
            auto_increaseid = (max(id_list)) + 1
            mess = {
                'id': auto_increaseid
            }
            adduser = Customers(id=auto_increaseid,name = name, dob = dob, updated_at= datetime.now())
            connection.session.add(adduser)
            connection.session.commit()
            resp.body = json.dumps(mess)


#------Update------
    def on_put(self, req, resp, id=None):
        body = req.media
        x = connection.session.query(Customers).get(int(id))
        if body.get('name') is None:
            x.dob = body['dob']
            connection.session.commit()
        elif body.get('dob') is None:
            x.name = body['name']
            connection.session.commit()
        else:
            x.name = body['name']
            x.dob =  body['dob']
            connection.session.commit()
        x.updated_at = datetime.now()
        output = {
                "id": x.id,
                "name": x.name,
                "dob": f'{x.dob}',
                "updated_at": f'{x.updated_at}'
        }
        connection.session.commit()
        resp.body = json.dumps(output)
#------Delete User------
    def on_delete(self, req, resp, id=None):
        x = connection.session.query(Customers).get(int(id))
        connection.session.delete(x)
        connection.session.commit()
        output = {
            "id" : id
        }
        connection.session.commit()
        resp.body = json.dumps(output)
