# Sparrowhawk

`sparrowhawk` is a server that hosts instrument journals, and a bug submission page. The credentials to access the
system are in Keeper.

For operating system help - for example the operating system not booting - contact "Technology IT Support" in outlook.

## Instrument Journals

See [Journal Viewer Data](/system_components/journal_viewer/Journal-Viewer-Data) for details.

## Instrument bug submission page

### Updating scientist email addresses

The scientist emails are defined in `/isis/www/html/sutekh/footprints/cgi/inst_globals.py`. The emails on the webpage
are updated from this file by a cron job (execute `crontab -e` as root to see exactly what it runs)
