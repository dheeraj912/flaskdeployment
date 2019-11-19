from flask_restplus import Resource,reqparse,Namespace


demo = Namespace("demo", description="Static Score Generation")

@demo.route('/test')
class Test(Resource):
    def get(self):
        return {"msg":"Well done. Demo successful"}
