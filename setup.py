from setuptools import setup, find_packages


def get_package_version() -> str:
    nspace = {}

    with open("./configurio/meta.py", 'r') as f:
        exec(f.read(), nspace)

    return nspace["__version__"]


package_name = 'configurio'
package_version = get_package_version()

# Form extras
extras_require = {
    "yaml": ["pyyaml"],
    "ujson": ["ujson"],
    "test": ["pytest<7"]
}

extras_require.update({
    "full": [dep for v in extras_require.values() for dep in v]
})

with open('README.md', 'r') as f:
    readme_text = f.read()

setup(
    name=package_name,
    version=package_version,
    python_requires="~=3.5",
    author="maximilionus",
    author_email="maximilionuss@gmail.com",
    description="Powerful and easy to use tool for working with various configuration files",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    keywords="configuration configs files",
    packages=find_packages(),
    extras_require=extras_require,
    license="MIT",
    url="https://github.com/maximilionus/configurio",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries"
    ]
)
