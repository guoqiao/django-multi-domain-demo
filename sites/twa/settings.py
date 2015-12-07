import sys
from os.path import abspath, dirname
from path import path

SITE_ROOT = path(dirname(abspath(__file__)))
SITES_ROOT = SITE_ROOT.parent
REPO_ROOT = SITES_ROOT.parent
APPS_ROOT = REPO_ROOT/'apps'
sys.path.insert(0, APPS_ROOT)
sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, SITE_ROOT)

from base_settings import *

SITE_ID = 2
