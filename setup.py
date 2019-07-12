"""
setup.py 是 python 程序用于跨平台安装的说明
命令行中的 make && make install 会被翻译为 python setup.py build && python setup.py install

一些 package 是纯编译后的字节码，可以直接安装，
另一些包含源码，需要本地编译器（例如 gcc 或者 cl）和 python interfacing module （例如 swig 或者 prex） 编译

setup.py 往往是和 pip install 平行的另一个选项，当 pip install fail 的时候可以用 setup.py 来安装
简单说明：setup.py 类似于 install functions 中的 __main__

more: https://packaging.python.org/tutorials/packaging-projects/
"""

import io
import re

from setuptools import find_packages
from setuptools import setup

# 常见 README 的加载方式，一般和 setup.py 放在项目最外层同级目录
# io.open 中 r 是 read 模式，t 是 text 模式，注意最好注明 encoding="utf8" 避免不同环境导致的解码错误
with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

# 这里直接硬编码了项目启动函数，"flask/__init__.py"
# 由于 io.open 采取了 text read 模式，所以可以用正则匹配 __init__.py 源码中的 "__version__ = "，以获得 flask 版本号
with io.open("src/flask/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='Flask',  # 发布包的名字
    version=version,  # 包版本
    url='https://www.palletsprojects.com/p/flask/',  # 项目主页，一般链接到 github，gitlab，bitbucket
    project_urls={
        "Documentation": "https://flask.palletsprojects.com/",
        "Code": "https://github.com/pallets/flask",
        "Issue tracker": "https://github.com/pallets/flask/issues",
    },
    license="BSD-3-Clause",  # 证书
    author="Armin Ronacher",  # 作者
    author_email="armin.ronacher@active-4.com",  # 作者联系方式
    maintainer="Pallets",  # 维护者
    maintainer_email="contact@palletsprojects.com",  # 维护者联系方式
    description="A simple framework for building complex web applications.",  # 项目描述
    long_description=readme,  # 项目详细描述
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages("src"),  # 包中需要包含的引用包，通常可以自动检索，这里自动检索 src 目录下的包，只有 flask
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[  # 安装需求
        "Werkzeug>=0.15",
        "Jinja2>=2.10.1",
        "itsdangerous>=0.24",
        "click>=5.1",
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
        "dev": [
            "pytest",
            "coverage",
            "tox",
            "sphinx",
            "pallets-sphinx-themes",
            "sphinxcontrib-log-cabinet",
            "sphinx-issues",
        ],
        "docs": [
            "sphinx",
            "pallets-sphinx-themes",
            "sphinxcontrib-log-cabinet",
            "sphinx-issues",
        ],
    },
    # 控制台启动入口，定位到入口函数，这里的路径是 clask.cli，函数名是 main
    entry_points={"console_scripts": ["flask = flask.cli:main"]},
)
