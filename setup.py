import os
from setuptools import setup, find_packages


def parse_requirements(name=None):
    if name:
        reqf = 'requirements-%s.txt' % name
    else:
        reqf = 'requirements.txt'

    requirements = []
    if not os.path.exists(reqf):
        return requirements

    with open(reqf) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            requirements.append(line)
    return requirements


setup(
    name='swh.docs',
    description='Software Heritage development documentation',
    author='Software Heritage developers',
    author_email='swh-devel@inria.fr',
    url='https://forge.softwareheritage.org/source/swh-docs/',
    packages=find_packages(),
    scripts=[],
    install_requires=parse_requirements(),
    setup_requires=['vcversioner'],
    extras_require={'testing': parse_requirements('test'),
                    'building': parse_requirements('swh')},
    vcversioner={},
    include_package_data=True,
)
