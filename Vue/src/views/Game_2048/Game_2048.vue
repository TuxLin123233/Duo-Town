<template>
  <main>
    <div v-for="(row, i) in board" :key="i">
      <div v-for="(item, j) in board[i]" :key="`${i}-${j}`" :id="`${i}-${j}`" class="block">
        {{item}}
      </div>
    </div>
  </main>
</template>

<script setup>
import {api} from "@/assets/main.js";
import {ref} from "vue";

//登录状态验证
api.is_logged();

//棋盘
const board = ref([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
])

function move(){

}
</script>

<style>
</style>