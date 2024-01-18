/*
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
*/

import i18n from '@/language/index.js';

const { t } = i18n.global;

export default {
  path: '/rule-manage',
  component: () => import('@views/rule-manage/index.vue'),
  name: 'ruleManage',
  redirect: {
    name: 'ruleManageList',
  },
  meta: {
    navName: 'auditConfigurationManage',
  },
  children: [
    {
      path: 'list',
      component: () => import('@views/rule-manage/list/index.vue'),
      name: 'ruleManageList',
      meta: {
        title: t('处理规则'),
        // skeleton: 'noticeGroupList',
      },
    },
    {
      path: 'create',
      component: () => import('@views/rule-manage/create/index.vue'),
      name: 'riskRuleCreate',
      meta: {
        title: t('新建处理规则'),
        // skeleton: 'strategyCreate',
      },
    },
    {
      path: 'edit/:id',
      component: () => import('@views/rule-manage/create/index.vue'),
      name: 'riskRuleEdit',
      meta: {
        title: t('编辑处理规则'),
        // skeleton: 'strategyCreate',
      },
    },
    {
      path: 'clone/:id',
      component: () => import('@views/rule-manage/create/index.vue'),
      name: 'riskRuleClone',
      meta: {
        title: t('克隆处理规则'),
        // skeleton: 'strategyCreate',
      },
    },
  ],
};
