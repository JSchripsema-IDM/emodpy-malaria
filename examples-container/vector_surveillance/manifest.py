import os

#
# This is a user-modifiable Python file designed to be a set of simple input file and directory settings that you
# can choose and change.
#

# the location of the file containing AssetCollection id for the dtk sif (singularity image)
sif_id = os.path.join(os.pardir, '..', 'examples', 'dtk_sif.id')
# The script is going to use this to store the downloaded schema file. Create 'download' directory or change to
# your preferred (existing) location.
schema_file = "download/schema.json"
# The script is going to use this to store the downloaded Eradication binary. Create 'download' directory or change
# to your preferred (existing) location.
eradication_path = "download/Eradication"
# Create 'Assets' directory or change to a path you prefer. idmtools will upload files found here.
assets_input_dir = "Assets"
plugins_folder = "download/reporter_plugins"

# python post- or pre-processing scripts directory
my_ep4_assets_dir = os.path.join(os.curdir, "ep4")
experiment_id = "experiment_id"
job_directory = os.path.join(os.path.expanduser('~'), "vector_surveillance")
