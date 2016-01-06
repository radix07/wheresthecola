# -*- mode: python -*-
a = Analysis(['run_app.py'],
             #pathex=['E:\\_Engineering\\WebServer\\webPgSicom\\webPgSicom'],
             hiddenimports=[ 
				 "flask",
				 "flask.views",
				 "flask_login",				 
				 "flask_wtf",
				 "flask_wtf.html5",				 
				 "flask_wtf.form",
				 "flask_wtf.file",
				 "flask_wtf.recaptcha",
				 "flask_wtf.recaptcha.fields",
				 "flask_wtf.recaptcha.validators",
				 "flask_wtf.recaptcha.widgets",
				 "flask.sessions",				 
			 ],
             hookspath='',
             runtime_hooks=None)
##### include mydir in distribution #######
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas
#####################################
a.datas += extra_datas("app\\static")
a.datas += extra_datas("app\\templates")
a.datas += [("app.db","app.db","DATA")]


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='pgSICoM.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True,
		  icon = "app\\static\\favicon.ico")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='run')
