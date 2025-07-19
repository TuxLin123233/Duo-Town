<template>
  <!--这里是用于显示Reuse小组件的页面-->
  <!--不在这里开发-->test1
</template>

<script setup>
import {basic_api} from "@/assets/js/api.js";
import {ref} from "vue";

const topic = ref("弹窗标题")
const content = ref("弹窗内容")

//登录状态验证
basic_api.is_logged();
</script>
