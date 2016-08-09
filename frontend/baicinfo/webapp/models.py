# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaicRegisterInfo(models.Model):
    # 登记信息
    url  = models.CharField(max_length=255, verbose_name=u"网址")
    city = models.CharField(max_length=255, verbose_name=u"城市")
    register_ID   = models.CharField(max_length=255, verbose_name=u"注册号")
    register_name = models.CharField(max_length=255, verbose_name=u"名称")
    type = models.CharField(max_length=255, verbose_name=u"类型")
    representative = models.CharField(max_length=255, verbose_name=u"法定代表人")
    capital = models.CharField(max_length=255, verbose_name=u"注册资本")
    establishment = models.CharField(max_length=255, verbose_name=u"成立日期")
    lodgment = models.CharField(max_length=255, verbose_name=u"住所")
    Operating_start = models.CharField(max_length=255, verbose_name=u"营业期限自")
    Operating_end   = models.CharField(max_length=255, verbose_name=u"营业期限至")
    Business_scope  = models.CharField(max_length=255, verbose_name=u"经营范围")
    reg_authority = models.CharField(max_length=255, verbose_name=u"登记机关")
    Approved_date = models.CharField(max_length=255, verbose_name=u"核准日期")
    status = models.CharField(max_length=255, verbose_name=u"登记状态")



class BaicRecordInfo(models.Model):
    # 备案信息
    person_id   = models.CharField(max_length=255, verbose_name=u"人员信息序号")
    register_name = models.ForeignKey(BaicRegisterInfo, related_name='BaicRecord', null=True)
    person_name = models.CharField(max_length=255, verbose_name=u"人员姓名")
    person_post = models.CharField(max_length=255, verbose_name=u"人员职务")
    # Branch_id = models.CharField(max_length=255, verbose_name=u"分支机构序号")
    # Branch_number = models.CharField(max_length=255, verbose_name=u"分支机注册号")
    # Branch_name = models.CharField(max_length=255, verbose_name=u"分支机构名称")
    # Branch_reg_auth = models.CharField(max_length=255, verbose_name=u"分支机构登记机关")
    # Liquidation_charge = models.CharField(max_length=255, verbose_name=u"清算组负责人")
    # Liquidation_Group = models.CharField(max_length=255, verbose_name=u"清算组成员")


class BaicMortgageInfo(models.Model):
    # 动产抵押登记信息
    mortgage_id = models.CharField(max_length=255, verbose_name=u"序号")
    register_name = models.ForeignKey(BaicRegisterInfo, related_name='BaicMortgage', null=True)
    number = models.CharField(max_length=255, verbose_name=u"登记编号")
    date = models.CharField(max_length=255, verbose_name=u"登记日期")
    reg_authority = models.CharField(max_length=255, verbose_name=u"登记机关")
    Sclaims_Amount= models.CharField(max_length=255, verbose_name=u"被担保债权数额")
    status = models.CharField(max_length=255, verbose_name=u"状态")
    more = models.CharField(max_length=255, verbose_name=u"详情")

class BaicStockInfo(models.Model):
    #股权出质登记信息
    stock_id = models.CharField(max_length=255, verbose_name=u"序号")
    register_name = models.ForeignKey(BaicRegisterInfo, related_name='BaicStorck', null=True)
    register_number = models.CharField(max_length=255, verbose_name=u"登记编号")
    seller = models.CharField(max_length=255, verbose_name=u"出质人")
    Cert_number = models.CharField(max_length=255, verbose_name=u"证照/证件号码")
    sale_count = models.CharField(max_length=255, verbose_name=u"出质股权数额")
    sale_owner = models.CharField(max_length=255, verbose_name=u"质权人")
    ID_number = models.CharField(max_length=255, verbose_name=u"证照/证件号码")
    reg_date = models.CharField(max_length=255, verbose_name=u"股权出质设立登记日期")
    status = models.CharField(max_length=255, verbose_name=u"状态")
    Change_status = models.CharField(max_length=255, verbose_name=u"变化情况")

class BaicAbnormalInfo(models.Model):
    # 经营异常信息
    Abnormal_ID  = models.CharField(max_length=255, verbose_name=u"序号")
    register_name = models.ForeignKey(BaicRegisterInfo, related_name='BaicAbnormal', null=True)
    Abnormal_reson = models.CharField(max_length=255, verbose_name=u"列入经营异常名录原因")
    Abnormal_time = models.CharField(max_length=255, verbose_name=u"列入日期")
    Abnormal_remove = models.CharField(max_length=255, verbose_name=u"移出经营异常名录原因")
    Abnormal_remove_date = models.CharField(max_length=255, verbose_name=u"移出日期")
    Abnormal_remove_auth = models.CharField(max_length=255, verbose_name=u"作出决定机关")



