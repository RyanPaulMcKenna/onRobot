from setuptools import setup

setup(
    name='onRobot',
    version='0.1.0',    
    description='A simple gripper library for UR robot with onRobot gripper, no onrobot compute box needed!',
    url='https://github.com/RyanPaulMcKenna/onRobot',
    author='Ryan McKenna',
    author_email='ryan.mckenna@york.ac.uk',
    license='MIT',
    packages=['onRobot'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
