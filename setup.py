from setuptools import setup, find_packages

setup(
    name = "command-line-registry",
    description = "Personal command line registry",
    author = "Lajos Santa",
    author_email = "santa.lajos@gmail.com",
    url = "https://github.com/voidpp/command-line-registry",
    license = "MIT",
    include_package_data = True,
    use_scm_version = True,
    setup_requires = ["setuptools_scm"],
    install_requires = [
        "configpp~=0.3",
        "tabulate~=0.8",
    ],
    extras_require = {},
    scripts = [
        "bin/command-line-registry"
    ],
    packages = find_packages(),
)
