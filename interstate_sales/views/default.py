from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import remember, forget, NO_PERMISSION_REQUIRED
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config, forbidden_view_config
from ..security import is_authenticated
from ..models import MyModel
import datetime
import os
from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    query = request.dbsession.query(MyModel)
    guardrails = query.filter(MyModel.category == 'Guardrail').all()
    subcategories = []
    for item in guardrails:
        if item.subcategory not in subcategories:
            subcategories.append(item.subcategory)
    return {
        'guardrails': guardrails,
        'subcategories': subcategories,
    }


@view_config(route_name='guardrail', renderer='../templates/guardrail.jinja2')
def guardrail_view(request):
    auth = False
    # if dict(request._headers.items())['Cookie']:
    try:
        auth = dict(request._headers.items())['Cookie']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    guardrails = query.filter(MyModel.category == 'Guardrail').all()
    subcategories = []
    for item in guardrails:
        if item.subcategory not in subcategories:
            subcategories.append(item.subcategory)
    return {
        'guardrails': guardrails,
        'subcategories': subcategories,
        'auth': auth,
    }


@view_config(route_name='login', renderer='../templates/login.jinja2')
@forbidden_view_config(renderer='../templates/nonentry.jinja2')
def login(request):
    """."""
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if is_authenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('home'), headers=headers)
        return {'res': 'Username or Password Entered Incorrect'}


@view_config(route_name='logout')
def logout(request):
    """."""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)
