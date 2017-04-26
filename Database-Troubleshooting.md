> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [Database](Database-Troubleshooting)

## Reducing database disc space

Database disc space is taken up by tables stored in `C:\Instrument\Var\mysql\data` the space can be regained by truncating the table. This could lose the data and will certainly remove it from the database so be careful. At various stages you will be prompted for the database password it is on the passwords page.

First create a sql dump of the two largest schemas:

    "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe" -u root -p msg_log > msg_log_<date>.sql
    "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe" -u root -p archive > archive_<date>.sql

Check the files look right and move them to long term storage. Then from a command prompt:

    "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe" -u root -p

Truncate the message log tables with: 

    truncate table msg_log.message;
    truncate table archive.sample;

