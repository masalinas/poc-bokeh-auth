import os

from tornado.web import StaticFileHandler

from bokeh.server.server import Server
from bokeh.server.auth_provider import AuthModule
from bokeh.server.views.static_handler import StaticHandler
from bokeh.command.util import build_single_handler_application

# Define Bokeh Server Prefix
prefix = 'MP'

# Define Bokeh Authentication Module
auth_provider = AuthModule('./auth/auth.py')

# Define Bokeh application
bokeh_app = build_single_handler_application('./main.py')

# Define the server settings, including the cookie_secret
server_settings = {
    'cookie_secret': 'my super secret',
}

# Define the allowed WebSocket origins (adjust for your domain and port)
websocket_origin = ['k8s.oferto.io:80', 'localhost:5006']

# Define the static path
static_path = os.path.join(os.path.dirname(__file__), "static")

# Embed the Bokeh server in the Tornado application with Authenticacion
bokeh_server = Server(
    {'/poc-bokeh-auth': bokeh_app},
    prefix=prefix,
    auth_provider=auth_provider,
    allow_websocket_origin=websocket_origin,
    toplevel_patterns=[
        ( r'/MP/poc-bokeh-auth/static/(.*)', StaticHandler )
    ],
    #extra_patterns=[
    #    (r'/MP/poc-bokeh-auth/static/(.*)', StaticFileHandler, {"path": static_path})
    #],
    **server_settings)

auth_provider._module.login_url = f'/{prefix}/login'
auth_provider._module.logout_url = f'/{prefix}/logout'

# Start Bokeh Server
bokeh_server.start()
bokeh_server.io_loop.start()