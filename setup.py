from setuptools import setup

APP = ['espanso-tools.py']
OPTIONS = {
    'iconfile': '512@2x.png'
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)