<template>
  <main>
    <!--  Flex水平居中容器  -->
    <div id="center-container">
      <img src="@/assets/svg/LOGO.svg" alt="LOGO">

      <!--   交互容器   -->
      <form @submit.prevent="view_api.login({username, password})" method="POST">
        <input type="text" name="username" placeholder="昵称" v-model="username">
        <input type="password" name="password" placeholder="输入密码" v-model="password">
        <input type="submit" value="登录" :style="buttonStyle">
      </form>

      <div id="jump" @click="goTo('register')">
        <img src="@/assets/svg/add.svg" alt="跳转">
        <p>注册</p>
      </div>
    </div>
  </main>
</template>

<style>
*{
  font-family: "harmony", sans-serif;
}

img[alt="LOGO"]{
  width: 250px;
  display: block;
  position: absolute;
  top: 50px;
}

#center-container{
  width: 100%;

  display: flex;
  justify-content: center;
}

form{
  width: 290px;
  height: 258px;

  position: absolute;
  top: 349px;

  display: flex;
  align-items: center;
  flex-direction: column;
}

input[type="text"], input[type="password"]{
  width: 289px;
  height: 65px;

  border: none;
  border-radius: 15px;
  outline: none;
  box-shadow: 0 0 2px  rgba(112, 112, 112, 0.25);
  background: rgba(247, 247, 247, 1);

  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 21px;
  color: rgba(166, 166, 166, 1);
}

input::placeholder{
  color: rgba(166, 166, 166, 1);;
}

input[type="text"]{
  margin-bottom: 26px;
}

input[type="password"]{
  margin-bottom: 45px;
}

input[type="submit"]{
  width: 289px;
  height: 57px;

  border: none;
  border-radius: 10px;

  background: rgba(42, 130, 228, 1);
  box-shadow: 0 2px 4px  rgba(0, 0, 0, 0.25);

  color: rgba(201, 201, 201, 1);
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  line-height: 21px;
}

#jump{
  display: flex;
  flex-direction: column;
  text-align: center;

  color: rgba(120, 120, 120, 1);
  font-size: 18px;
  font-weight: 400;

  top: 686px;
  position: absolute;
}

img[alt="跳转"]{
  display: block;
  width: 30px;
  height: 30px;

  padding: 15px;
  background-color: rgba(201, 201, 201, 0.25);
  border-radius: 50%;

  position: relative;
}
</style>

<script lang="js" setup>
import {goTo, basic_api, view_api} from "@/assets/main.js";
import {computed, ref} from "vue";

const username = ref("")
const password = ref("")

// 提交按钮样式
const buttonStyle = computed(() => {
  if (username.value !== '' && password.value !== '') {
    return {
      'color': 'white'
    }
  }else {
    return {
      'background-color': '#9d9d9d',
      'color': '#ffffff'
    }
  }
})

//登录状态验证
basic_api.is_logged();
</script>