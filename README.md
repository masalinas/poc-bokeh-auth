# Description
A PoC with bokeh server with a custom basic login view

## Execute applicartion

```
BOKEH_COOKIE_SECRET='my super secret' bokeh serve --auth-module=./poc-bokeh-auth/auth/auth.py --show poc-bokeh-auth
```