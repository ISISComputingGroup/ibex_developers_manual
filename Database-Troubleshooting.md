> [Wiki](Home) > [Trouble-shooting](trouble-shooting-pages) > [Database](Database-Troubleshooting)

## Reducing database disc space

Database disc space is taken up by tables stored in `C:\Instrument\Var\mysql\data` the space can be regained by truncating the table. This will lose all the data so be careful. From a command prompt:

    "c:\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe" -u root -p

Enter the password found on the passwords page.

Tunctate the message log table with: `truncate table msg_log.message;`