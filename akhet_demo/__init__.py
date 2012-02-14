from pyramid.config import Configurator
import pyramid_beaker

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # Configure Beaker sessions and caching, renderers, and event subscribers.
    config.include("pyramid_beaker")
    config.include(".subscribers")
    config.include("akhet.static")
    config.add_renderer(".html", "pyramid.mako_templating.renderer_factory")

    # Add routes and views.
    config.add_route("home", "/")
    config.include("akhet.pony")
    config.add_static_route("akhet_demo", "static", cache_max_age=3600)
    config.scan()

    return config.make_wsgi_app()
