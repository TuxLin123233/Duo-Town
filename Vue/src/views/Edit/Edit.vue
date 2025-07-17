<template>
  <!--http://localhost:8080/pages/edit/edit.html-->
  <main>
    <!--标题-->
    <header>
      <img src="../../assets/svg/left-arrow.svg" alt="左箭头" @click="goTo('me')">
      <span>写帖子</span>
    </header>

    <form @submit.prevent="view_api.add_blog({title, content})">
      <input type="text" name="title" placeholder="标题" v-model="title">
      <textarea name="content" v-model="content"></textarea>
      <input type="submit" value="发送帖子" :style="submit_style">
    </form>
  </main>
</template>

<style>
body{
  overflow-x: hidden;
}

*{
  font-family: "harmony", sans-serif;
}

header{
  display: flex;
  margin: 10px 10px 0 10px;
}

img[alt="左箭头"]{
  width: 40px;
  height: 40px;
  position: absolute;
}

header span{
  position: relative;
  display: inline-block;
  font-size: 20px;
  color: #3b3b3b;
  margin: auto;
  font-weight: 600;
  top: 10px;
}

form{
  position: relative;
  display: flex;
  flex-direction: column;
  margin-top: 50px;
  align-items: center;
}

input[name="title"]{
  border: none;
  outline: none;
  width: 85%;
  height: 50px;
  padding-left: 13px;
  color: black;
  font-size: 18px;
  border-bottom: 2px solid #464646;
  text-align: center;
}

textarea{
  outline: none;
  margin-top: 20px;
  height: 650px;
  resize: none;
  width: 90%;
  border: 1px solid #7c7c7c;
  padding-top: 10px;
  font-size: 18px;
  padding-left: 10px;
  padding-right: 10px;
}

input[type="submit"]{
  position: relative;
  margin-top: 20px;
  outline: none;
  border: none;
  width: 120px;
  height: 45px;
  border-radius: 15px;
  background-color: #9d9d9d;
  color: #c2c2c2;
  box-shadow: 0 0 4px rgba(153, 153, 153, 0.25);
}
</style>

<script setup>
import {basic_api, goTo, view_api} from "@/assets/js/api.js";
import {computed, ref} from "vue";

//登录状态验证
basic_api.is_logged();

//文章信息
let title = ref("")
let content = ref("")

const submit_style = computed(() => {
  if (title.value !== "" && content.value !== "") {
    return {
      'color': '#000000',
      'background': "#5daed0"
    }
  }
})
</script>
