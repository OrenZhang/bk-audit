<!--
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
-->
<!-- eslint-disable vue/no-v-html -->
<template>
  <div
    id="search-page-footer"
    class="search-page-footer">
    <div
      v-html="platformConfig.i18n.footerInfoHTML" />
    <div>
      <p>{{ platformConfig.footerCopyrightContent }}</p>
    </div>
  </div>
</template>
<script setup lang="ts">
  import usePlatformConfig from '@/hooks/use-platform-config';

  const platformConfig = usePlatformConfig();

</script>
<style lang="postcss">
  .search-page-footer {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 60px;
    display: flex;
    height: 52px;
    font-size: 12px;
    color: #63656e;
    background: #f5f6fa;
    background-color: #f5f6fa;
    border-top: 1px solid #dcdee5;
    align-items: center;
    flex-direction: column;
    justify-content: center;

    .y-axis {
      color: #63656e;
    }

    .footer-content:first-child .y-axis {
      display: none;
    }
  }

</style>
