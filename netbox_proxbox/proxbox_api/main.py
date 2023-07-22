from fastapi import FastAPI

'''
from plugins_config import (
    NETBOX,
    NETBOX_TOKEN,
    PROXMOX_SESSIONS as proxmox_sessions,
    NETBOX_SESSION as nb,
)
'''

from proxmoxer import ProxmoxAPI


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "X.X.X.X"
PORT = "<PORT>"
USER = "<USER>@pam"
TOKEN_NAME = "<STRING>"
TOKEN_VALUE = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
VERIFY_SSL = "<BOOLEAN>"

try:
    # Start PROXMOX session using TOKEN
    px = ProxmoxAPI(
        HOST,
        port=PORT,
        user=USER,
        token_name=TOKEN_NAME,
        token_value=TOKEN_VALUE,
        verify_ssl=VERIFY_SSL
    )
except:
    raise RuntimeError(f'Error trying to initialize Proxmox Session using TOKEN (token_name: {PROXMOX_TOKEN_NAME} and token_value: {PROXMOX_TOKEN_VALUE} provided')

        
app = FastAPI()


@app.get("/proxmox/cluster/resources")
async def root(type: str | None = None):
    return px.cluster.resources.get()

