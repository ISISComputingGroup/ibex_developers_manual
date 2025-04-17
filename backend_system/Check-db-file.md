> [Wiki](Home) > [The Backend System](The-Backend-System) > [Useful tools](Useful-tools) > Check db file script

The check_db_file script checks that a db file conforms to the ISIS format. Usage:

```
python.exe check_db_file.py -f test_file.db

optional arguments:
    -d --directory = specify a directory to check ALL the db files in
    -r --recursive = check all db files below the specified directory
    -v --verbose = shows more detailed information
```