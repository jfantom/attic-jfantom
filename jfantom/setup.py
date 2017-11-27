import setuptools 

setuptools.setup(
        name = 'jfantom',
        author = 'jfan',
        author_email = 'jcf2167@columbia.edu',
        packages = setuptools.find_packages(),
        install_requires = [
            'Flask==0.10.1',
            'gunicorn==19.7.1',
            'Jinja2==2.7.3']
)
