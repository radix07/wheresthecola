# under normal circumstances, this script would not be necessary. the
# sample_application would have its own setup.py and be properly installed;
# however since it is not bundled in the sdist package, we need some hacks
# to make it work

import os
import sys
from flask.ext.frozen import Freezer
from flask.ext.assets import Environment,Bundle

sys.path.append(os.path.dirname(__name__))

from app import create_app

# create an app instance
app = create_app()


freezer = Freezer(app)

if __name__ == '__main__':
    """ Builds this site.
    """
    print("Building website...")
    app.debug = False
    app.testing = True
    #asset_manager.config['ASSETS_DEBUG'] = False
    freezer.freeze()
    print("Done.")
