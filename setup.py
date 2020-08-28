from setuptools import setup, find_packages

setup(
    name='wedding',
    version='1.0',
    description='Wedding Planner',
    author='Scott P. White',
    author_email='spwhite1337@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'wd_sync = wedding.upload:upload'
    ]},
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'requests',
        'ipykernel',
        'beautifulsoup4',
        'flask',
        'plotly',
        'dash',
        'dash-bootstrap-components',
        'awscli'
    ]
)
