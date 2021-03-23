from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    #templating engine
    config.include('pyramid_chameleon')
    #routes
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    #views
    config.scan('.views')
    return config.make_wsgi_app()