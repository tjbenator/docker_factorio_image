import os
import json
import subprocess
from pprint import pprint
from shutil import copyfile

factorio_dir = '/opt/factorio'
game = factorio_dir + '/bin/x64/factorio'
config_file_default = factorio_dir + '/data/server-settings.example.json'
config_file = factorio_dir + '/server-settings.json'
save_filename = os.getenv('FACTORIO_SAVE', 'default.zip')
save_file = factorio_dir + '/saves/' + save_filename

if not os.path.exists(config_file):
  copyfile(config_file_default, config_file)

version = subprocess.check_output([game, "--version"]).split('/n')[0].split(' ')[1]

# Load the server settings for updates
with open(config_file) as config:
  settings = json.load(config)

# Update server settings with environment variables
for key in settings.keys():
  # Underscores indicate comments in the config
  if not key[:1] == '_':
    if isinstance(settings[key], dict):
      # We can go two levels deep. Mostly so we can set the servers visablility.
      for subkey in settings[key].keys():
        settings[key][subkey] = type(settings[key][subkey])(os.getenv('FACTORIO_' + key.upper() + "_" + subkey.upper(), settings[key][subkey]))
    else:
      # Ensure we retain our casting
      settings[key] = type(settings[key])(os.getenv('FACTORIO_' + key.upper(), settings[key]))

# Overriding the defaults if we don't have environment variables
settings['name'] = os.getenv('FACTORIO_NAME', 'Factorio Server')
settings['description'] = os.getenv('FACTORIO_DESCRIPTION', 'Version ' + version)

with open(config_file, 'w') as outfile:
  json.dump(settings, outfile, indent = 4, ensure_ascii = False)

if os.path.exists(save_file):
   print "Starting existing game..."
   subprocess.call([game, '--start-server', save_file])
else:
   print "Creating new map..."
   subprocess.call([game, '--create', save_file])
   subprocess.call([game, '--start-server', save_file])
