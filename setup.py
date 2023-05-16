"""
    Setup file for linkedin_pdf_extractor.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup

from setuptools import setup

if __name__ == "__main__":
    try:
        setup(use_scm_version=True)
    except Exception as e:
        print("\n\nAn error occurred while building the project:", e)
        print(
            "\n\nPlease ensure you have the most updated version of setuptools, setuptools_scm, and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise


