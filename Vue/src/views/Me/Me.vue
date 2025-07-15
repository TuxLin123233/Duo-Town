<template>
  <main id="main">
    <!--顶部区域-->
    <Header></Header>

    <!--用户个人信息-->
    <UserInfo></UserInfo>

    <!--人脉-->
    <div id="network">
      <span class="network-container">好友<span id="friends">3</span></span>
      <span class="network-container">关注<span id="followers">8</span></span>
    </div>

    <!--卡片容器-->
    <NoteCards></NoteCards>

    <!--导航-->
    <Portal></Portal>
  </main>
</template>

<style>
body{
  background-image: url("@/assets/img/背景山.png");
  background-size: 100vw 100vh;
  background-repeat: no-repeat;

  overflow-x: hidden;
}

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "harmony", sans-serif;
}

#network{
  display: flex;
  justify-content: space-between;
  width: 122px;
  height: 19px;
  margin-left: 36px;
  margin-top: 35px;
  line-height: 19px;
  font-family: "harmony", sans-serif;
  color: #fff;
  font-size: 16px;
}

.network-container{
  display: flex;
  justify-content: space-between;
  width: 50px;
  color: rgba(255,255,255,.8);
}

#followers,#friends{
  color: #fff;
}
</style>

<script setup>
import {basic_api, view_api} from "@/assets/main.js";

import Header from "@/views/Me/child/Header.vue";
import UserInfo from "@/views/Me/child/UserInfo.vue";
import NoteCards from "@/views/Me/child/NoteCards.vue";
import Portal from "@/views/Me/child/Portal.vue";

//登录状态验证: 黄金安全护盾，爬虫统统滚开！！！
basic_api.is_logged();
//渲染用户信息
view_api.get_user_data([
    'username',
    'likes',
    'blogs',
    'friends',
    'fans',
    'age'
]);
</script>