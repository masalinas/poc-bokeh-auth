import os
import logging

from tornado.web import StaticFileHandler

from bokeh.server.server import Server
from bokeh.server.auth_provider import AuthModule
from bokeh.command.util import build_single_handler_application

# Set Loggin level for bokeh server
logging.getLogger('bokeh').setLevel(logging.DEBUG)

# Define Bokeh Server arguments
prefix = 'MP'
port = 5006

# Define Bokeh Authentication Module
auth_provider = AuthModule('./auth/auth.py')

# Define Bokeh application
bokeh_app = build_single_handler_application('./main.py')

# Define the server settings, including the cookie_secret
server_settings = {
    'cookie_secret': 'my super secret',
}

# Define the allowed WebSocket origins (adjust for your domains and ports)
websocket_origin = ['k8s.oferto.io:80', 'localhost:' + str(port)]

# Define the static path
static_path = os.path.join(os.path.dirname(__file__), "static")

# Embed the Bokeh server in the Tornado application with Authenticacion
bokeh_server = Server(
    {'/': bokeh_app},
    port=port,
    prefix=prefix,
    auth_provider=auth_provider,
    allow_websocket_origin=websocket_origin,
    extra_patterns=[
        (r'/poc-bokeh-auth/static/(.*)', StaticFileHandler, {"path": static_path})
    ],
    **server_settings)

# Some bug from bokeh that not set the prefix for external resources
auth_provider._module.login_url = f'/{prefix}/login'
auth_provider._module.logout_url = f'/{prefix}/logout'

# Start Bokeh Server
bokeh_server.start()
bokeh_server.io_loop.start()