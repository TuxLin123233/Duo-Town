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

    <!--数字信息-->
    <div id="number-infor">
      <div id="fans">
        <span>0</span>
        <span>粉丝</span>
      </div>
      <div id="followers">
        <span>0</span>
        <span>关注</span>
      </div>
      <div id="likes">
        <span>0</span>
        <span>获赞</span>
      </div>
    </div>

    <!--谢谢刘哥帮我-->

    <!--导航按钮-->
    <div id="navigate">
      <div class="navigate-container">
        <div class="navigate-card">
          <img src="../../assets/svg/me/帖子.svg" alt="帖子">
          <span>帖子</span>
        </div>

        <div class="navigate-card">
          <img src="../../assets/svg/me/广场.svg" alt="广场">
          <span>广场</span>
        </div>

        <div class="navigate-card">
          <img src="../../assets/svg/me/邮箱.svg" alt="邮箱">
          <span>邮箱</span>
        </div>
      </div>

      <div class="navigate-container">
        <div class="navigate-card">
          <img src="../../assets/svg/me/身份.svg" alt="身份">
          <span>身份</span>
        </div>

        <div class="navigate-card" @click="goTo('game_2048')">
          <img src="../../assets/svg/me/游戏.svg" alt="游戏">
          <span>游戏</span>
        </div>
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

#number-infor{
  display: flex;
  justify-content: space-around;
  width: 358px;
  height: 76px;
  border-radius: 10px;
  background-color: rgba(250, 250, 250, 1);
  margin: 28px auto 0 auto;
  border:1px solid rgba(237, 237, 237, 1) ;
  font-family: "Harmony", sans-serif;
}

#number-infor div{
  display: flex;
  flex-direction: column;
  justify-content:center ;
  align-items: center;
  font-size: 18px;
}

#navigate{
  margin-top: 50px;
}

.navigate-container{
  display: flex;
  width: 100vw;
  justify-content: space-evenly;
  font-family: "Harmony", sans-serif;
}

.navigate-container:last-child{
  margin-top: 50px;
}

.navigate-card{
  width: 80px;
  height: 111px;
  border: 1px solid rgba(212, 212, 212, 1);
  background: rgba(247, 247, 247, 1);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  font-size: 18px;
  font-weight: 400;
}

.navigate-container img{
  width: 32px;
  height: 32px;
}

.navigate-container span{
  display: block;
}
</style>

<script setup>
// 以下代码看不懂正常，因为这是一个未解之谜:)
import {api, goTo} from "@/assets/main.js";

//登录状态验证: 黄金安全护盾，爬虫统统滚开！！！
api.is_logged();
</script>