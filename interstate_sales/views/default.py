from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    # try:
    #     query = request.dbsession.query(MyModel)
    #     one = query.filter(MyModel.name == 'one').first()
    # except DBAPIError:
    #     return Response(db_err_msg, content_type='text/plain', status=500)
    return {}


@view_config(route_name='guardrail', renderer='../templates/guardrail.jinja2')
def guardrail_view(request):
    query = request.dbsession.query(MyModel)
    guardrails = query.filter(MyModel.category == 'Guardrail').all()
    subcategories = []
    for item in guardrails:
        if item.subcategory not in subcategories:
            subcategories.append(item.subcategory)
    return {'guardrails': guardrails, 'subcategories': subcategories}
