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