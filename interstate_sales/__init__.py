from pyramid.config import Configurator
import os
from pyramid.authentication import AuthTktAuthenticationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    config = Configurator(settings=settings)
    # base_path = request.static_url('interstate_sales:static/')
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.views')
    config.include('.security')
    config.scan()
    return config.make_wsgi_app()
