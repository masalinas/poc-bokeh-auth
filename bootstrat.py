from bokeh.server.server import Server
from bokeh.server.auth_provider import AuthModule

from bokeh.command.util import build_single_handler_application

# Define Bokeh Prefix Web Context
prefix = "MP"

# Define Bokeh Authentication Module
auth_provider = AuthModule('./auth/auth.py')

# Define Bokeh application
bokeh_app = build_single_handler_application('./main.py')

# Embed the Bokeh server in the Tornado application
bokeh_server = Server(
    {'/poc-bokeh-auth': bokeh_app},
    prefix=prefix,
    auth_provider=auth_provider)

auth_provider._module.login_url = f'/{prefix}/login/'
auth_provider._module.logout_url = f'/{prefix}/logout/'

# Start Bokeh Server
bokeh_server.start()
bokeh_server.io_loop.start()