#-*- coding: utf-8 -*-


import sys, os

from baic.settings import djpath
if djpath not in sys.path:
    sys.path.append(djpath)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baicinfo.settings")
django.setup()
from webapp.models import BaicRegisterInfo, BaicAbnormalInfo, BaicRecordInfo


class BaicORM(object):
    def save(self, item):
        reginfo = BaicRegisterInfo()
        AbnormalInfo = BaicAbnormalInfo()
        RecordInfo = BaicRecordInfo()
        try:
            reginfo.url = item['url'][0].strip()
            reginfo.city = item['city'][0].strip()
            reginfo.register_ID = item['register_ID'][0].strip()
            reginfo.register_name = item['register_name'][0].strip()
            reginfo.type = item['type'][0].strip()
            reginfo.representative = item['representative'][0].strip()
            reginfo.capital = item['capital'][0].strip()
            reginfo.establishment = item['establishment'][0].strip()
            reginfo.lodgment = item['lodgment'][0].strip()
            reginfo.Operating_start = item['Operating_start'][0].strip()
            reginfo.Operating_end = item['Operating_end'][0].strip()
            reginfo.Business_scope = item['Business_scope'][0].strip()
            reginfo.reg_authority = item['reg_authority'][0].strip()
            reginfo.Approved_date = item['Approved_date'][0].strip()
            reginfo.status = item['status'][0].strip()

            reginfo.save()

            # 备案信息
            RecordInfo.person_id = item['person_id'][0].strip()
            RecordInfo.person_name = item['person_name'][0].strip()
            RecordInfo.person_post = item['person_post'][0].strip()
            RecordInfo.register_name = reginfo
            RecordInfo.save()

            # 经营异常信息
            AbnormalInfo.Abnormal_ID = item['Abnormal_ID'][0].strip()
            AbnormalInfo.Abnormal_reson = item['Abnormal_reson'][0].strip()
            AbnormalInfo.Abnormal_time = item['Abnormal_time'][0].strip()
            AbnormalInfo.Abnormal_remove = item['Abnormal_remove'][0].strip()
            AbnormalInfo.Abnormal_remove_date = item['Abnormal_remove_date'][0].strip()
            AbnormalInfo.Abnormal_remove_auth = item['Abnormal_remove_auth'][0].strip()
            AbnormalInfo.register_name = reginfo
            AbnormalInfo.save()
        except Exception:
            # 这有报错信息，将这个URL留下来以后单独处理
            print item['url'][0].strip()
            pass
