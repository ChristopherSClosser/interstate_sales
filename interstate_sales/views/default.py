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
    auth = False
    try:
        auth = dict(request._headers.items())['Cookie']
    except:
        pass
    print('Headers', request.cookies)
    print('Auth: ', auth)
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


@view_config(route_name='guardrail', renderer='../templates/guardrail.jinja2')
def guardrail_view(request):
    auth = False
    try:
        auth = dict(request._headers.items())['Cookie']
    except:
        pass
    query = request.dbsession.query(MyModel)
    guardrails = query.filter(MyModel.category == 'Guardrail').all()
    subcategories = []
    # images = []
    for item in guardrails:
        if item.subcategory not in subcategories:
            subcategories.append(item.subcategory)
        # for image in item.img.split():
        #     images.append(image)
        # item.img = images
        # images = []
    return {
        'guardrails': guardrails,
        'subcategories': subcategories,
        'auth': auth,
    }


@view_config(
    route_name='new',
    renderer='../templates/entry.jinja2',
    permission='secret',
)
def create_view(request):
    """Display create a list entry."""
    if request.POST:
        entry = MyModel(
            category=request.POST["category"],
            subcategory=request.POST["subcategory"],
            title=request.POST["title"],
            markdown=request.POST["markdown"],
            img=request.POST["img"],
            extra=request.POST["extra"],
        )
        request.dbsession.add(entry)
        return HTTPFound(request.route_url('home'))
    return {}


@view_config(
    route_name='edit',
    renderer='../templates/edit.jinja2',
    permission='secret',
)
def edit_view(request):
    ident = int(request.matchdict["id"])
    entry = request.dbsession.query(MyModel).get(ident)
    if not entry:
        raise HTTPNotFound
    if request.POST:
        entry.category = request.POST['category']
        entry.subcategory = request.POST["subcategory"]
        entry.title = request.POST["title"]
        entry.markdown = request.POST["markdown"]
        entry.img = request.POST["img"]
        entry.extra = request.POST["extra"]
        request.dbsession.flush()
        return HTTPFound(request.route_url('home'))

    form_fill = {
        "category": entry.category,
        "subcategory": entry.subcategory,
        "title": entry.title,
        "markdown": entry.markdown,
        "img": entry.img,
        "extra": entry.extra,
    }
    return {"entry": form_fill}


@view_config(
    route_name='delete',
    renderer='../templates/delete.jinja2',
    permission='secret',
)
def delete_view(request):
    """."""
    ident = int(request.matchdict["id"])
    entry = request.dbsession.query(MyModel).get(ident)
    if request.POST:
        request.dbsession.delete(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('home'))
    form_fill = {
        "category": entry.category,
        "subcategory": entry.subcategory,
        "title": entry.title,
        "markdown": entry.markdown,
        "img": entry.img,
        "extra": entry.extra,
    }
    return {"entry": form_fill}


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
