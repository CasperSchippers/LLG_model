import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='llg_model_solver',
                 version='0.0.1',
                 description='An LLG model solver',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/CasperSchippers/llg_model_solver',
                 author='Casper Schippers',
                 author_email='c.f.schippers@tue.nl',
                 packages=setuptools.find_packages(),
                 classifiers=(
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ),
                 )
