from setuptools import setup


def get_package_version() -> str:
    nspace = {}

    with open("./configerz/info.py", 'r') as f:
        exec(f.read(), nspace)

    return nspace["__version__"]


package_name = 'configerz'
package_version = get_package_version()
extras_require = {}

with open('README.md', 'r') as f:
    readme_text = f.read()

setup(
    name=package_name,
    version=package_version,
    author="maximilionus",
    author_email="maximilionuss@gmail.com",
    description="Powerful and easy to use tool for working with various configuration files",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    packages=[package_name],
    extras_require=extras_require,
    license="MIT",
    url="https://github.com/maximilionus/configerz",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries"
    ]
)
