# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

class CustomBuildCommand(build_py):
    def run(self):
        # 在构建之前清理 build 目录
        self.clean_build_directory()
        super().run()

    def clean_build_directory(self):
        import shutil
        shutil.rmtree('build')

setup(
    name='rl-agents',
    version='1.0.dev0',
    description='A collection of Reinforcement Learning agents',
    url='https://github.com/eleurent/rl-agents',
    author='Edouard Leurent',
    author_email='eleurent@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Researchers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='reinforcement learning agents',
    packages=find_packages(exclude=['docs', 'scripts', 'tests*']),
    install_requires=['gym', 'numpy', 'pandas', 'numba', 'pygame', 'matplotlib', 'seaborn', 'six', 'docopt',
                      'torch>=1.2.0', 'tensorboardX'],
    tests_require=['pytest'],
    extras_require={
        'dev': ['scipy'],
    },
    entry_points={
        'console_scripts': [],
    },
)

