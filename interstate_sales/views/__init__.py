"""."""

from .default import (
    home_view,
    guardrail_view,
    paint_view,
    markings_view,
    create_view,
    edit_view,
    delete_view,
    search_view,
    # api_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(home_view, route_name='home')
    config.add_view(guardrail_view, route_name='guardrail')
    config.add_view(paint_view, route_name='paint')
    config.add_view(markings_view, route_name='markings')
    config.add_view(create_view, route_name='new')
    config.add_view(edit_view, route_name='edit')
    config.add_view(delete_view, route_name='delete')
    config.add_view(search_view, route_name='search')
    # config.add_view(api_view, route_name='api')
