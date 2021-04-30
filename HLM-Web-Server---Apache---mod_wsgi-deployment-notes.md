Deployment notes for [HLM View](https://github.com/ISISNeutronMuon/HLM_View), running with Apache + mod_wsgi on Windows Server 2012 R2.


#### Web App
To run with the Django development server using `python manage.py runserver 0.0.0.0:8000`:

```
1. Installed python-3.9.4-amd64
2. Installed Git-2.31.1-64-bit
3. (Optional) Installed npp.7.9.5.Installer (Notepad++)
4. Cloned the HLM View repo in C:/
5. Created virtual environment: C:\HLM_View\venv and activated it (Scripts/activate.bat)
6. Installed requirements: cd C:\HLM_View and pip install -r requirements.txt

7. Manually copy over static files that are not version controlled
   (from https://github.com/ISISNeutronMuon/HLM_View/files/6404513/static.zip)
    - secret_key.txt in .project\
    - jquery-3.5.1.min.js in HLM_View\static\js
    - plugins\ in HLM_View\static
    - bootstrap\ in HLM_View\static

8. Update the db connection at DATABASES in settings.py
9. Run python manage.py runserver - works with debug=True, 
   Note: If set to false Django won't provide static files anymore. 
   This step is just for testing as Django dev server should never be used in production.
```

#### Grafana Dashboard
To set up the Grafana dashboard:
```
Install grafana-7.5.5.windows-amd64
Set up Grafana admin credentials (Access details)
Import dashboard with .json file from HLM_View\Grafana
Configure the Grafana Data Source (MySQL DB)
In Grafana/conf, copy sample.ini , rename to custom.ini
Then set to allow_embedding and anonymous access (for iframes)
Restart Grafana service to apply new config
Updated iframe links in the HLM View templates (details.html, building.html) 
from localhost:3000 to new address 
```

#### Web Server
To set up the web server with Apache + mod_wsgi:
```
Used resources: 
	https://github.com/Johnnyboycurtis/webproject#apache-and-mod_wsgi 
	https://github.com/GrahamDumpleton/mod_wsgi/blob/develop/win32/README.rst
	https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/modwsgi/
        https://montesariel.com/blog/post-3
	
Added new hosts in project/settings.py ALLOWED_HOSTS

Install VC_redist.x64.exe
Download httpd-2.4.47-win64-VS16.zip (ApacheLounge), 
extract in C:\Apache24, cmd cd "C:\Apache24\bin\" , 
"httpd.exe" and go to localhost 80 to check that it works

pip install mod_wsgi, error: MVS C++ 14.0 required
Download vs_buildtools__1321439799.1619704707, and install universal + C++ packages
Successfully installed mod-wsgi-4.7.1
CMD: run mod_wsgi-express module-config (this will create mod_wsgi.cp39-win_amd64.pyd 
in HLM_View/venv/Lib/site-packages/mod_wsgi/server)

Edit "C:\Apache24\conf\httpd.conf":
    Changed "ServerName" to localhost:80
	
    At the end of http.conf, added:
	
	# Django Project
	LoadFile "C:/Instrument/Apps/Python/Python39/python39.dll"
	LoadModule wsgi_module "C:/HLM_View/venv/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp39-win_amd64.pyd"
	WSGIPythonHome "C:/HLM_View/venv;C:/Instrument/Apps/Python/Python39/"
	WSGIScriptAlias / "C:/HLM_View/project/wsgi.py"
	WSGIPythonPath "C:/HLM_View/venv/Lib/site-packages/;C:/HLM_View/"

	<Directory "C:/HLM_View/project/">
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	Alias /static "C:/HLM_View/static/"
	<Directory "C:/HLM_View/static">
		Require all granted
	</Directory>

cmd run "C:\Apache24\bin\httpd.exe" and check that http://<instrument name>/ works.
Apache logs can be found in "C:\Apache24\logs"

Fix a Python bug that causes an error 500 every time a query is made to the database.
Edit the __init__.py file in project-root\venv\Lib\site-packages\asgiref by adding the following:
	# PATCH that fixes a Python Bug:
	import sys
	import asyncio

	if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
		asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


Install Apache httpd.exe as a service: C:\Apache24\bin>httpd.exe -k install -n "HLM View Web Server"
```

