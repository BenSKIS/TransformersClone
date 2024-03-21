import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# Path to the requirements file
requirements_path = 'requirements.txt'

# Read requirements file and parse it into a list of requirements
with open(requirements_path, 'r') as file:
    requirements = [line.strip() for line in file.readlines()]

# Check each requirement against the currently installed versions
pkg_resources.require(requirements)
