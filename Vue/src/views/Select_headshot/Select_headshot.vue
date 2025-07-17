<template>
  <header>
    <img src="@/assets/svg/left-arrow.svg" alt="左箭头">
    <span id="topic">选择头像</span>
  </header>

  <form id="main"></form>
</template>

<style>
body{
  margin: 0;
  font-family: "harmony", sans-serif;
}
img[alt="左箭头"]{
  width: 40px;
  height: 40px;
  position: absolute;
  margin: 10px;
}

#topic{
  position: absolute;
  width: 100vw;
  text-align: center;
  margin-top: 20px;
  font-size: 20px;
}

header{
  width: 100vw;
  height: 60px;
}

input[type=radio]{
  appearance: none;
  background-color: black;
}

#main{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  width: 93vw;
  margin: 30px auto auto;
}
</style>

<script>
import {basic_api, view_api} from "@/assets/main.js";

//登录状态验证
basic_api.is_logged();
view_api.list_headshot();
</script>
