"""Defined Routes."""


def includeme(config):
    """Routes."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('guardrail', '/guardrail')
    config.add_route('paint', '/paint')
    config.add_route('markings', '/markings')
    config.add_route('safety', '/safety')
    config.add_route('signs', '/signs')
    config.add_route('equipment', '/equipment')
    config.add_route('team', '/team')
    config.add_route('contact', '/contact')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('new', '/item/new-entry')
    config.add_route('edit', '/item/{id:\d+}/edit-entry')
    config.add_route('delete', '/item/{id:\d+}/delete-entry')
    config.add_route('search', '/search')
