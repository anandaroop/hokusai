from hokusai.lib.config import config
from hokusai.lib.command import command
from hokusai.services.secret import Secret
from hokusai.lib.common import print_green

@command
def create_secrets(context):
  secret = Secret(context)
  secret.create()
  print_green("Created secret %s-secrets" % config.project_name)

@command
def delete_secrets(context):
  secret = Secret(context)
  secret.destroy()
  print_green("Deleted secret %s-secrets" % config.project_name)

@command
def get_secrets(context, secrets):
  secret = Secret(context)
  secret.load()
  if len(secrets) == 0:
    for k, v in secret.all():
      print("%s=%s" % (k, v))
  else:
    for k, v in secret.all():
      if k in secrets:
        print("%s=%s" % (k, v))

@command
def set_secrets(context, secrets):
  secret = Secret(context)
  secret.load()
  for s in secrets:
    if '=' not in s:
      print_red("Error: secrets must be of the form 'KEY=VALUE'")
      return -1
    split = s.split('=', 1)
    secret.update(split[0], split[1])
  secret.save()

@command
def unset_secrets(context, secrets):
  secret = Secret(context)
  secret.load()
  for s in secrets:
    secret.delete(s)
  secret.save()
