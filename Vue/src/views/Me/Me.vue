<template>
  <!--个人主页-->
  <!-- http://127.0.0.1:8000 你打开这个，如果会跳转就没事了-->
  <!--暑假快乐-->
  <main>
    <!--顶部栏-->
    <header>
      <img src="@/assets/svg/me/首页.svg" alt="首页按钮">
      <span>个人中心</span>
      <img src="@/assets/svg/me/侧边栏.svg" alt="侧边栏">
    </header>

    <!--头像-->
    <div id="head-infor">
      <img src="@/assets/img/头像测试.jpg" alt="头像" />
      <span id="name">刘哥好帅</span>
      <div id="duo-id">Duo-id: 000001</div>
      </div>
    <div id="head-information">
      <div id="Fans">
        <span>0</span>
        <span>粉丝</span>
      </div>
      <div id="Pay-attention">
        <span>0</span>
        <span>关注</span>
      </div>
      <div id="liked">
        <span>0</span>
        <span>获赞</span>
      </div>
    </div>
  </main>
</template>

<style>

body{
  padding-top: 32px;
}
header{
  padding-left: 36px;
  padding-right: 36px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: "Harmony", sans-serif;
  font-size: 20px;
}

#head-infor{
  margin-top: 74px;
  text-align: center;
}

img[alt="头像"]{
  display: block;
  position: relative;
  width: 170px;
  height: 170px;
  border-radius: 50%;
  margin: auto;
  box-shadow: 0 0 5px #c2c2c2;
}

#name{
  display: block;
  padding-top: 19px;
  font-size: 26px;
  font-weight: 500;
  line-height: 30px;
  font-family: "Harmony", sans-serif;
  color: black;
}

#duo-id{
  padding-top: 10px;
  color: rgba(125, 125, 125, 1);
  font-size: 18px;
  font-family: "Harmony", sans-serif;
}

#head-information{
  display: flex;
  justify-content: space-around;
  width: 358px;
  height: 76px;
  border-radius: 10px;
  background-color: rgba(250, 250, 250, 1);
  margin: 28px auto 0 auto;
  border:1px solid rgba(237, 237, 237, 1) ;
}

#head-information div{
  display: flex;
  flex-direction: column;
  justify-content:center ;
  align-items: center;
  font-size: 18px;
}
</style>

<script setup>
// 以下代码看不懂正常，因为这是一个未解之谜:)
import {api} from "@/assets/main.js";
import {ref} from "vue";

const username = ref(null)
//登录状态验证: 黄金安全护盾，爬虫统统滚开！！！
api.is_logged();
</script>