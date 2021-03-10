# -*- coding: utf-8 -*-

from setuptools import setup, distutils, Extension
import sys

if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported. Please install Python 3.7 or upwards and try again.')

platform = distutils.util.get_platform()
print(platform)
package_data = dict()
if "win" in platform:
    package_data = {'': ['LICENSE'],
                    'lib_client': ['lib_client/animus_client.dll', 'lib_client/animus_client.lib',
                                   'lib_client/libwinpthread-1.dll', 'lib_client/LICENSE']}
    extra_link_args = None
else:
    package_data = {'': ['LICENSE'],
                    'lib_client': ['lib_client/libanimus_client.so', 'lib_client/LICENSE']}
    if "mac" in platform:
        extra_link_args = ["-Wl,-rpath", "-Wl,@loader_path/"]
    else:
        extra_link_args = ['-Wl,-rpath,$ORIGIN']


animus_client_py3 = Extension("lib_client._animus_client_py3",
                              include_dirs=['lib_client'],
                              libraries=['animus_client'],
                              library_dirs=['lib_client'],
                              sources=['lib_client/animus_client_py3_wrap.c'],
                              define_macros=[("SWIG", None)],
                              swig_opts=[],
                              extra_link_args=extra_link_args,
                              )

setup(
    name='animus_client',
    version='2.1.0',
    python_requires='>=3.7',
    description='Animus Client SDK for Python 3 developed by Cyberselves Universal Ltd.',
    long_description="Animus Client SDK for Python 3 developed by Cyberselves Universal Ltd.",
    author='Daniel Camilleri',
    author_email='daniel@cyberselves.com',
    url='https://www.cyberselves.com',
    license="Proprietary. (C) Cyberselves Universal Ltd.",
    packages=['animus_client', 'animus_utils', 'lib_client'],
    ext_modules=[animus_client_py3],
    package_data=package_data,
    include_package_data=True,
    install_requires=[
        "numpy >= 1.16.6",
        "scikit-build",
        "opencv-python >= 4.2.0.32",
        "wheel",
        "protobuf"
    ],
    tests_require=[
        'pytest',
        'protobuf',
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Private :: Do not Upload"
        'License :: Other/Proprietary License'
    ],
)
