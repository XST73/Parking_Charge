import datetime
import random

from . import models

list_name = ["张", "李", "王", "赵", "钱", "孙", "周", "吴", "郑", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许"]


def fo():
    for i in range(10):
        models.VIPuserInfo.objects.create(user_nanme=random.choice(list_name) + random.choice(list_name) + random.choice(list_name),
                                          user_ID="豫A" + random.randint(10000, 99999).__str__(),
                                          user_phone="1" + random.randint(220000000, 999999999).__str__(),
                                          user_birth=datetime.datetime.now(),
                                          user_sex=random.choice(["男", "女"]),
                                          user_grade=str(i + 7) + "8")
