<script setup lang="ts">
import {goTo} from "@/assets/js/tool.js";
</script>

<template>
  <div id="portal">
    <span id="title">传送门</span>
    <div id="portal-buttons">
      <img src="@/assets/svg/me/广场.svg" alt="广场">
      <img src="@/assets/svg/me/游戏.svg" alt="游戏" @click="goTo('game_2048')">
      <img src="@/assets/svg/me/搜索.svg" alt="搜索">
    </div>
  </div>
</template>

<style scoped>
#portal{
  width: 350px;
  height: 150px;
  background-color: rgba(186, 202, 255, 0.4);
  position: relative;
  margin: 53px auto auto;
  border-radius: 20px;
  font-family: "harmony", sans-serif;
  padding-top: 21px;
}

#portal #title{
  display: flex;
  justify-content: center;
  color: rgb(255, 255, 255);
  font-size: 18px;
  font-weight: bold;
}

#portal-buttons{
  display: flex;
  justify-content: space-evenly;
  margin-top: 21px;
}

img[alt="广场"],img[alt="游戏"],img[alt="搜索"]{
  padding: 18px;
  border-radius: 15px;
  background-color: rgba(65, 102, 224, 0.8);
}
</style>