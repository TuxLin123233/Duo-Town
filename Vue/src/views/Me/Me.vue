<template>
  <main id="main">
    <header>
      <img src="@/assets/svg/me/侧边栏.svg" alt="侧边栏" @click="toggleEdit">
      <AnimatePresence>
      <motion.div
          id="edit"
          v-if="is_show"
          :initial="{transform: 'translateX(250px)',opacity: 0}"
          :animate="{transform: 'translateX(0px)', opacity: 1}"
          :exit="{transform: 'translateX(250px)', opacity: 0}"
      >
        <span>🪪 个人资料</span>
        <span>⚙️ 通用</span>
        <span>🤣 我的好友</span>
        <span>📖 我的帖子</span>
        <span>🤙 联系官方</span>
        <span>❤️ 给我们赞助一杯可乐</span>
      </motion.div>
      </AnimatePresence>
    </header>

    <!--用户信息-->
    <div id="user-info">
      <img src="@/assets/img/头像测试.jpg" alt="头像">
      <span id="username">---</span>

      <!-- 标签 -->
      <div id="tags">
        <img src="@/assets/svg/me/男.svg" alt="男性">
        <span id="age">---</span>
      </div>
    </div>

    <!--人脉-->
    <div id="network">
      <span class="network-container">好友<span id="friends">3</span></span>
      <span class="network-container">关注<span id="followers">8</span></span>
    </div>

    <!--卡片容器-->
    <div class="card-container">
      <div id="write-note">
        <span>发送帖子</span>
        <img src="@/assets/svg/me/帖子.svg" alt="帖子">
      </div>

      <div id="note-info">
        <!--标题-->
        <div id="note-titles">
          <span>发帖数</span>
          <span>点赞数</span>
          <span>粉丝数</span>
        </div>

        <div id="note-numbers">
          <span>0</span>
          <span id="likes">---</span>
          <span id="fans">---</span>
        </div>
      </div>
    </div>

    <div id="portal">
      <span id="title">传送门</span>
      <div id="portal-buttons">
        <img src="@/assets/svg/me/广场.svg" alt="广场">
        <img src="@/assets/svg/me/游戏.svg" alt="游戏" @click="goTo('game_2048')">
        <img src="@/assets/svg/me/搜索.svg" alt="搜索">
      </div>
    </div>
  </main>
</template>

<style>
body{
  background-image: url("@/assets/img/背景山.png");
  background-size: 100vw 100vh;
  background-repeat: no-repeat;

  overflow-x: hidden;   //小子给我注意点，不要左右滑动
}
</style>

<style src="./me.css" scoped></style>
<script setup>
import {basic_api, goTo, view_api} from "@/assets/main.js";
import {ref, toRef} from "vue";
import {AnimatePresence, motion} from "motion-v";

//侧边栏默认状态
let is_show = ref(false);
//http://127.0.0.1:8000 可以打开吗？OK

//登录状态验证: 黄金安全护盾，爬虫统统滚开！！！
basic_api.is_logged();

//渲染用户信息
view_api.get_user_data();

//控制is_show的值
const toggleEdit = () => {
  is_show.value = !is_show.value;
};
</script>