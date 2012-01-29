from pyramid.config import Configurator
import pyramid_beaker

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # Configure Beaker sessions and caching
    session_factory = pyramid_beaker.session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    pyramid_beaker.set_cache_regions_from_settings(settings)

    # Configure renderers and event subscribers.
    config.add_renderer(".html", "pyramid.mako_templating.renderer_factory")
    config.include(".subscribers")
    config.include("akhet.static")

    # Add routes and views.
    config.add_route("home", "/")
    config.include("akhet.pony")
    config.add_static_route("akhet_demo", "static", cache_max_age=3600)
    config.scan()

    return config.make_wsgi_app()
