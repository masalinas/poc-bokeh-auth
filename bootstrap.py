import os
import logging

from tornado.web import StaticFileHandler

from bokeh.server.server import Server
from bokeh.server.auth_provider import AuthModule
from bokeh.command.util import build_single_handler_application

# Bokeh Server arguments
app = "poc-bokeh-auth"
app_title = "PoC Bokeh Auth"
app_logo = "logo_gsdpi.png"
app_background = "login_background.png"
prefix = "MP"
port = 5006
cookie_secret = "my super secret"
websocket_origin = ["k8s.oferto.io:80", "localhost:" + str(port)]
basic_username = "bokeh"
basic_password = "bokeh"
login_level = logging.DEBUG

# Set Loggin level for bokeh server
logging.getLogger("bokeh").setLevel(login_level)

# Define Bokeh Authentication Module
auth_provider = AuthModule("./auth/auth.py")

# Define Bokeh application
bokeh_app = build_single_handler_application("./main.py")

# Define the server settings, including the cookie_secret
server_settings = {
    "cookie_secret": cookie_secret,
}

# Define the allowed WebSocket origins (adjust for your domains and ports)
websocket_origin = websocket_origin

# Define the static path
static_path = os.path.join(os.path.dirname(__file__), "static")

# Embed the Bokeh server in the Tornado application with Authenticacion
bokeh_server = Server(
    {"/": bokeh_app},
    port=port,
    prefix=prefix,
    auth_provider=auth_provider,
    allow_websocket_origin=websocket_origin,
    extra_patterns=[
        (r"/" + app + "/static/(.*)", StaticFileHandler, {"path": static_path})
    ],
    **server_settings)

# Configure Auth Provider arguments
auth_provider._module.login_url = f"/{prefix}/login"
auth_provider._module.logout_url = f"/{prefix}/logout"
auth_provider._module.app = app
auth_provider._module.app_title = app_title
auth_provider._module.prefix = prefix
auth_provider._module.style_path = "/" + prefix + "/" + app + "/static/css/styles.css"
auth_provider._module.logo_image = "/" + prefix + "/" + app + "/static/images/" + app_logo
auth_provider._module.background_image = "/" + prefix + "/" + app + "/static/images/" + app_background
auth_provider._module.basic_username = basic_username
auth_provider._module.basic_password = basic_password

# Start Bokeh Server
bokeh_server.start()
bokeh_server.io_loop.start()