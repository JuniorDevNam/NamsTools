import os
import urllib.request
from urllib.parse import urlparse, urlunparse
import re

!wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains "$url" --no-parent