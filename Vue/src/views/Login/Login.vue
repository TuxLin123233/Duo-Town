<template>
  <main>
    <img src="@/assets/svg/arrow-left.svg" alt="左箭头">

    <!--  Flex水平居中容器  -->
    <div id="center-container">
      <img src="@/assets/svg/LOGO.svg" alt="LOGO">

      <!--   交互容器   -->
      <form @submit.prevent="submit.login({username, password})" method="POST">
        <input type="text" name="username" placeholder="昵称" v-model="username">
        <input type="password" name="password" placeholder="输入密码" v-model="password">
        <input type="submit" value="登录">
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
img[alt="左箭头"]{
  width: 35px;
  height: 36px;

  display: block;
  position: absolute;
  left: 30px;
  top: 30px;
}

img[alt="LOGO"]{
  display: block;
  position: absolute;
  top: 144px;
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
import {goTo, submit} from "@/assets/main.js";
import {ref} from "vue";

const username = ref("")
const password = ref("")
</script>