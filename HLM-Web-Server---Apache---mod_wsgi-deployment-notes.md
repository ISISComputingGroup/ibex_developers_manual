Deployment notes for [HLM View](https://github.com/ISISNeutronMuon/HLM_View), running with Apache + mod_wsgi on Windows Server 2012 R2.


#### Django App
To get it running with the Django development server using `python manage.py runserver 0.0.0.0:8000`

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
9. Run python manage.py runserver - works with debug=True, but if set to false Django won't provide static files anymore. 
   This step is just for testing as Django dev server should never be used in production.
```

