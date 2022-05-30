import os
c.JupyterHub.admin_access = True
c.JupyterHub.bind_url = 'http://:8000/jupyterhub/'
c.JupyterHub.hub_ip = os.environ['HUB_IP']
#c.JupyterHub.ssl_cert = '/etc/ssl/private/cert.pem'
#c.JupyterHub.ssl_key = '/etc/ssl/private/key.pem'
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.debug = True
c.Spawner.default_url = '/lab'
c.Spawner.notebook_dir = '/root/workspace'
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
#c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.Authenticator.admin_users = {'tooru'}
#c.LDAPAuthenticator.lookup_dn = True
#c.LDAPAuthenticator.server_address = 'apps.aegis.local'
#c.LDAPAuthenticator.bind_dn_template = [
#    "uid={username},ou=users,dc=apps,dc=aegis,dc=local"
#]
