# HLM Webserver deployment

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
9. Use an online Django secret key generator and create a `secret_key.txt` file with the key inside in the HLM_View\project folder.
10. Run python manage.py runserver (in root with the venv activated)- works with debug=True, 
   Note: If set to false Django won't provide static files anymore. 
   This step is just for testing as Django dev server should never be used in production.
```

#### Grafana Dashboard
To set up the Grafana dashboard:
```
1. Install grafana-7.5.5.windows-amd64
2. Set up Grafana admin credentials (Access details)
3. Import dashboard with .json file from HLM_View\Grafana
4. Configure the Grafana Data Source (MySQL DB)
5. In Grafana/conf, copy sample.ini , rename to custom.ini
6. Then set to allow_embedding and anonymous access (for iframes)
7. Restart Grafana service to apply new config
8. Updated iframe links in the HLM View templates (details.html, building.html) 
from localhost:3000 to new address 
```
[HLM_View\Grafana](https://github.com/ISISNeutronMuon/HLM_View/blob/master/Grafana/Object%20Measurements.json)

#### Web Server
To run with a production web server using Apache + mod_wsgi:
```
Used resources: 
	https://github.com/Johnnyboycurtis/webproject#apache-and-mod_wsgi 
	https://github.com/GrahamDumpleton/mod_wsgi/blob/develop/win32/README.rst
	https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/modwsgi/
        https://montesariel.com/blog/post-3
        https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
	
1. Added new hosts in project/settings.py ALLOWED_HOSTS, set DEBUG to False, check the Django deployment checklist

2. Install VC_redist.x64.exe
3. Download httpd-2.4.47-win64-VS16.zip (ApacheLounge), extract in C:\Apache24
4. Run "C:\Apache24\bin\httpd.exe" then go to localhost 80 to confirm it works

5. pip install mod_wsgi, error: MVS C++ 14.0 required
6. Download vs_buildtools__1321439799.1619704707, and install universal + C++ packages
7. Successfully installed mod-wsgi-4.7.1
8. CMD: run mod_wsgi-express module-config (this will create mod_wsgi.cp39-win_amd64.pyd 
in HLM_View/venv/Lib/site-packages/mod_wsgi/server)

9. Edit "C:\Apache24\conf\httpd.conf":
    Set ServerName to localhost:80
	
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

10. Run "C:\Apache24\bin\httpd.exe" and check that http://<instrument name>/ works.
Note: Apache logs can be found in "C:\Apache24\logs"

11. Fix a Python bug that causes an error 500 every time a query is made to the database.
    Edit the __init__.py file in project-root\venv\Lib\site-packages\asgiref by adding the following:
	# PATCH that fixes a Python Bug:
	import sys
	import asyncio

	if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
		asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


12. Install Apache httpd.exe as a service: C:\Apache24\bin>httpd.exe -k install -n "HLM View Web Server"
```

