#-*- coding: utf-8 -*-

import sys, os

from baic.settings import djpath
if djpath not in sys.path:
    sys.path.append(djpath)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baicinfo.settings")
django.setup()
from webapp.models import BaicRegisterInfo
class BaicORM(object):
    def save(self, item):
        reginfo = BaicRegisterInfo()
        try:

            reginfo.url = item['url'][0]
            reginfo.city = item['city'][0]
            reginfo.register_ID = item['register_ID'][0]
            reginfo.register_name = item['register_name'][0]
            reginfo.type = item['type'][0]
            reginfo.representative = item['representative'][0]
            reginfo.capital = item['capital'][0]
            reginfo.establishment = item['establishment'][0]
            reginfo.lodgment = item['lodgment'][0]
            reginfo.Operating_start = item['Operating_start'][0]
            reginfo.Operating_end = item['Operating_end'][0]
            reginfo.Business_scope = item['Business_scope'][0]
            reginfo.reg_authority = item['reg_authority'][0]
            reginfo.Approved_date = item['Approved_date'][0]
            reginfo.status = item['status'][0]

            reginfo.save()
        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print item['url'][0]
            pass
