from setuptools import setup

with open('./README.md', 'r', encoding='utf-8') as f:
    longDescription = f.read()

setup(
    name='Alarm Clock',
    version='1.0.0',
    author='Eric_the_Read',
    description='A basic alarm clock', 
    long_description=longDescription,
    long_description_content_type='text/markdown',
    packages=['alarmClock', 'alarmClock.windows'],
    include_package_data=True,
    license='MIT',
    install_requires=['datetime', 'PySimpleGUI', 'pygame'],
    entry_points={'gui_scripts': ['eric=alarmClock.__main__:main']}
    )
