#m2r README.md
rm -rf argcfg.egg-info
rm -rf dist
python setup.py sdist
twine upload dist/* --verbose