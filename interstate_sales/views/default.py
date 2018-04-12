"""Interstate Sales Views."""


from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config, forbidden_view_config
from ..security import is_authenticated
from ..models import MyModel
import os


def build_dict(request):
    """Return category and subcategory dict to view."""
    query = request.dbsession.query(MyModel)
    guardrails = query.filter(MyModel.category == 'Guardrail').all()
    gr_subcats = []
    paints = query.filter(MyModel.category == 'Traffic Paint').all()
    tr_subcats = []
    pm = query.filter(MyModel.category == 'Pavement Markings').all()
    pm_subcats = []
    cs = query.filter(MyModel.category == 'Construction Safety').all()
    cs_subcats = []
    signs = query.filter(MyModel.category == 'Signs').all()
    signs_subcats = []
    equipment = query.filter(MyModel.category == 'Equipment').all()
    equipment_subcats = []
    team = query.filter(MyModel.category == 'Our Team').all()
    team_subcats = []
    for item in guardrails:
        if item.subcategory not in gr_subcats:
            gr_subcats.append(item.subcategory)
    for item in paints:
        if item.subcategory not in tr_subcats:
            tr_subcats.append(item.subcategory)
    for item in pm:
        if item.subcategory not in pm_subcats:
            pm_subcats.append(item.subcategory)
    for item in cs:
        if item.subcategory not in cs_subcats:
            cs_subcats.append(item.subcategory)
    for item in signs:
        if item.subcategory not in signs_subcats:
            signs_subcats.append(item.subcategory)
    for item in equipment:
        if item.subcategory not in equipment_subcats:
            equipment_subcats.append(item.subcategory)
    for item in team:
        if item.subcategory not in team_subcats:
            team_subcats.append(item.subcategory)
    return {
        'gr_subcats': gr_subcats,
        'tr_subcats': tr_subcats,
        'pm_subcats': pm_subcats,
        'cs_subcats': cs_subcats,
        'signs_subcats': signs_subcats,
        'equipment_subcats': equipment_subcats,
        'team_subcats': team_subcats,
    }


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    items = build_dict(request)
    return {
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='search', renderer='../templates/search.jinja2')
def search_view(request):
    """Search view."""
    auth = False
    search = ''
    try:
        search = request.POST['search']
    except KeyError:
        pass
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel).all()
    res = []
    if search:
        for item in query:
            for key, val in vars(item).items():
                if search.lower() in str(key).lower() or search.lower() in str(val).lower():
                    if item not in res:
                        res.append(item)
    subcategories = []
    for item in res:
        if item.subcategory not in subcategories:
            subcategories.append(item.subcategory)

    return {
        'res': res,
        'search': search,
        'subcategories': subcategories,
        'auth': auth,
    }


@view_config(route_name='guardrail', renderer='../templates/guardrail.jinja2')
def guardrail_view(request):
    """Query for guardrail view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    guardrails = query.filter(MyModel.category == 'Guardrail').all()
    items = build_dict(request)

    return {
        'guardrails': guardrails,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='paint', renderer='../templates/paint.jinja2')
def paint_view(request):
    """Query for guardrail view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    paints = query.filter(MyModel.category == 'Traffic Paint').all()
    items = build_dict(request)
    return {
        'paints': paints,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='markings', renderer='../templates/markings.jinja2')
def markings_view(request):
    """Query for guardrail view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    markings = query.filter(MyModel.category == 'Pavement Markings').all()
    items = build_dict(request)
    return {
        'markings': markings,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='safety', renderer='../templates/safety.jinja2')
def safety_view(request):
    """Query for safety view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    safety_items = query.filter(MyModel.category == 'Construction Safety').all()
    items = build_dict(request)

    return {
        'safety_items': safety_items,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='signs', renderer='../templates/signs.jinja2')
def signs_view(request):
    """Query for guardrail view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    signs = query.filter(MyModel.category == 'Signs').all()
    items = build_dict(request)
    return {
        'signs': signs,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='equipment', renderer='../templates/equipment.jinja2')
def equipment_view(request):
    """Query for guardrail view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    equipment = query.filter(MyModel.category == 'Equipment').all()
    items = build_dict(request)
    return {
        'equipment': equipment,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='team', renderer='../templates/team.jinja2')
def team_view(request):
    """Query for guardrail view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    team = query.filter(MyModel.category == 'Our Team').all()
    items = build_dict(request)
    return {
        'team': team,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='contact', renderer='../templates/contact.jinja2')
def contact_view(request):
    """Contact view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    items = build_dict(request)
    return {
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(
    route_name='new',
    renderer='../templates/entry.jinja2',
    permission='secret',
)
def create_view(request):
    """Display create a list entry."""
    items = build_dict(request)

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
    return {
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
    }


@view_config(
    route_name='edit',
    renderer='../templates/edit.jinja2',
    permission='secret',
)
def edit_view(request):
    items = build_dict(request)
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
    return {
        "entry": form_fill,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
    }


@view_config(
    route_name='delete',
    renderer='../templates/delete.jinja2',
    permission='secret',
)
def delete_view(request):
    """."""
    items = build_dict(request)
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
    return {
        "entry": form_fill,
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
    }


@view_config(route_name='gregory', renderer='../templates/gregory.jinja2')
def gregory_view(request):
    """Gregory view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    items = build_dict(request)
    return {
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
        'auth': auth,
    }


@view_config(route_name='saso', renderer='../templates/saso.jinja2')
def saso_view(request):
    """Gregory view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    items = build_dict(request)
    return {
        'gr_subcats': items['gr_subcats'],
        'tr_subcats': items['tr_subcats'],
        'pm_subcats': items['pm_subcats'],
        'cs_subcats': items['cs_subcats'],
        'signs_subcats': items['signs_subcats'],
        'equipment_subcats': items['equipment_subcats'],
        'team_subcats': items['team_subcats'],
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
