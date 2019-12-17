#Hack for multiple line template TAGS - http://zachsnow.com/#!/blog/2016/multiline-template-tags-django/

import re
from django.template import base
base.tag_re = re.compile(base.tag_re.pattern, re.DOTALL)
