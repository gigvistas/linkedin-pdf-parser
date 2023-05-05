.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/linkedin_pdf_extractor.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/linkedin_pdf_extractor
    .. image:: https://readthedocs.org/projects/linkedin_pdf_extractor/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://linkedin_pdf_extractor.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/linkedin_pdf_extractor/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/linkedin_pdf_extractor
    .. image:: https://img.shields.io/pypi/v/linkedin_pdf_extractor.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/linkedin_pdf_extractor/
    .. image:: https://img.shields.io/conda/vn/conda-forge/linkedin_pdf_extractor.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/linkedin_pdf_extractor
    .. image:: https://pepy.tech/badge/linkedin_pdf_extractor/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/linkedin_pdf_extractor
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/linkedin_pdf_extractor

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

======================
linkedin_pdf_extractor
======================


    Add a short description here!


A longer description of your project goes here...


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.

Steps to upload it to pypi:
1. Delete the old tag 
command to delete the tag on local repo : git tag -d <tagname>

2. Push the changes to remote:
command:    git push origin --delete <tagname>

3. create a new tag 
Command: to create a new tag : git tag -a tagname -m "my version 1.4"

4. push that tag
Command:    git push origin tagname

5. Build the package distribution
Command:  tox -e build  # to build your package distribution

6. Publish the package 
Command: tox -e publish -- --repository pypi  # to release your package to PyPI


