<template>
  <header>
    <img src="@/assets/svg/left-arrow.svg" alt="左箭头">

  </header>

  <form id="main"></form>
</template>

<style>
body{
  margin: 0;
  font-family: "harmony", sans-serif;
}
</style>

<script>
import {basic_api} from "@/assets/js/api.js";

//登录状态验证
basic_api.is_logged();
</script>
