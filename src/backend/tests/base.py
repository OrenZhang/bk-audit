# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - 审计中心 (BlueKing - Audit Center) available.
Copyright (C) 2023 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""

from bk_resource import api as _api
from bk_resource import resource as _resource
from django.conf import settings
from django.test import TestCase as _TestCase


class TestCase(_TestCase):
    """
    Base Test Case for Bk Audit
    """

    app_code = settings.APP_CODE
    app_secret = settings.SECRET_KEY
    namespace = settings.DEFAULT_NAMESPACE
    bk_biz_id = settings.DEFAULT_BK_BIZ_ID
    system_id = settings.BK_IAM_SYSTEM_ID
    resource = _resource
    api = _api
