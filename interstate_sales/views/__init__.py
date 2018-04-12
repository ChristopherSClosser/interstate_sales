"""."""

from .default import (
    home_view,
    guardrail_view,
    paint_view,
    markings_view,
    safety_view,
    signs_view,
    equipment_view,
    create_view,
    edit_view,
    delete_view,
    search_view,
    team_view,
    contact_view,
    gregory_view,
    saso_view,
    # ennisflint_view,
    # graco_view,
    # impactrecovery_view,
    # uteck_view,
    # api_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(home_view, route_name='home')
    config.add_view(guardrail_view, route_name='guardrail')
    config.add_view(paint_view, route_name='paint')
    config.add_view(markings_view, route_name='markings')
    config.add_view(safety_view, route_name='safety')
    config.add_view(signs_view, route_name='signs')
    config.add_view(equipment_view, route_name='equipment')
    config.add_view(create_view, route_name='new')
    config.add_view(edit_view, route_name='edit')
    config.add_view(delete_view, route_name='delete')
    config.add_view(search_view, route_name='search')
    config.add_view(team_view, route_name='team')
    config.add_view(contact_view, route_name='contact')
    config.add_view(gregory_view, route_name='gregory')
    config.add_view(saso_view, route_name='saso')
    # config.add_view(ennisflint_view, route_name='ennis-flint')
    # config.add_view(graco_view, route_name='graco')
    # config.add_view(impactrecovery_view, route_name='impact-recovery')
    # config.add_view(uteck_view, route_name='u-teck')
    # config.add_view(api_view, route_name='api')
