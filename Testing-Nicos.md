> [Wiki](Home) > [The Backend System](The-Backend-System) > [Nicos](Nicos) > Testing Nicos

In order to run the unit tests on Nicos, you first need to set up your Python packages. Install the packages listed in the `README` document in your `nicos-core` directory. At time of writing these are:

  - pytest
  - mock
  - coverage (optional)
  - sphinx (for generating doc)

This can be done simply by running `pip install [package-names]` from your `...\Python\Scripts` directory.

Now you can go ahead and run the tests. Go to `...\nicos-core\test` and run `...\Python\Scripts\pytest.exe`. Pytest will detect all the tests in the directory and run them. Note that it is important to run it from the `test` directory or some tests will fail to do some relative imports.

Alternatively, you can run the tests in PyCharm by creating a pytest run configuration in Run|Edit Configurations.. then right clicking on the `test` directory and clicking `Run 'Pytests in test'` or `Debug 'Pytests in test'`. (See [here](https://www.gowrishankarnath.com/using-pytest-testing-tool-to-test-python-code-by-configuring-pycharm-ide.html) for more detail)