import os
from logging import NullHandler

import yaml
from __version__ import __version__

CURRENT_VERSION = __version__

print(f"The current version of the package is: {CURRENT_VERSION}")


# Path to the Kubernetes YAML file(s)
yaml_files = ['./manifests/frontend.yaml']  # List of YAML files to update


def update_yaml_file(file_path, new_version):
    yaml_content = None
    with open(file_path, 'r') as f:
        yaml_content = yaml.safe_load(f)

    update_yaml_value(new_version, yaml_content)

    # Write the updated YAML back to the file
    with open(file_path, 'w') as f:
        yaml.dump(yaml_content, f)



def update_yaml_value(new_version, yaml_content):
    # Traverse the YAML structure to find and update the image tag
    yaml_content['metadata']['labels']['version']  = new_version
    yaml_content['spec']['template']['metadata']['labels']['version'] = new_version

    if 'spec' in yaml_content and 'template' in yaml_content['spec']:
        containers = yaml_content['spec']['template']['spec']['containers']
        for container in containers:
            if 'image' in container:
                # Split the current image to get the base image name
                image_name = container['image'].split(':')[0]
                # Update the image tag with the new version
                container['image'] = f'{image_name}:{new_version}'


# Update each specified YAML file
for yaml_file in yaml_files:
    update_yaml_file(yaml_file, CURRENT_VERSION)
    print(f"Updated {yaml_file} with version {CURRENT_VERSION}")