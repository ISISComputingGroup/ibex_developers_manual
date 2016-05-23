In order to run the unit tests on Nicos, you first need to set up your Python packages. Install the packages listed in the `README` document in your `nicos-core` directory. At time of writing these are:

  - nose
  - mock
  - coverage (optional)
  - sphinx (for generating doc)

This can be done simply by running `pip install [package-names]` from your `...\Python\scripts` directory.

Now you can go ahead and run the tests. Go to `...\nicos-core\test` and run `...\Python\scripts\nosetests.exe`. Nose will detect all the tests in the directory and run them. Note that it is important to run it from the `test` directory or some tests will fail to do some relative imports.