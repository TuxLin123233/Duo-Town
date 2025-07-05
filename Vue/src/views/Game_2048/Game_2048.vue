<template>
  <main>
    <div id="topic">2048 游戏</div>
    <!-- 容器 -->
    <div id="container">
      <div v-for="(row, i) in board" :key="i" class="row" :id="`row${i}`">
        <div v-for="(item, j) in board[i]" :key="`${i}-${j}`" :id="`${i}-${j}`" class="block">
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import {api} from "@/assets/main.js";
import {nextTick, ref} from "vue";

//登录状态验证
api.is_logged();

//棋盘
const board = ref([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
])

//Dom渲染后被调用
nextTick(() => {
})
</script>