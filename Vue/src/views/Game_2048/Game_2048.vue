<template>
  <main>
    <!--信息栏-->
    <div id="topic">
      <div id="score">
        <span>分数</span>
        <span id="number">0</span>
      </div>
      <span id="name">2048</span>
      <span id="restart">新游戏</span>
    </div>

    <!-- 容器 -->
    <div id="container">
      <div v-for="(row, i) in board" :key="i" class="row" :id="`row${i}`">
        <div v-for="(item, j) in board[i]" :key="`${i}-${j}`" :id="`${i}-${j}`" class="block">
          <template v-if="item > 0">{{item}}</template>
        </div>
      </div>
    </div>

    <!--控制按钮-->
    <div id="control">
      <img src="@/assets/svg/2048/up.svg" alt="up">
      <img src="@/assets/svg/2048/down.svg" alt="down">
      <img src="@/assets/svg/2048/left.svg" alt="left">
      <img src="@/assets/svg/2048/right.svg" alt="right">
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
  [2, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
])

function control(direction){
  if (direction === "up"){
  }
}

//Dom渲染后被调用
nextTick(() => {
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      const block = document.getElementById(`${i}-${j}`);
      if (block.getHTML() === "2"){
        block.style.backgroundColor = "#eee4da";
        block.style.boxShadow = "0 0 30px 10px rgba(243, 215, 116, 0), inset 0 0 0 1px rgba(255, 255, 255, 0)";
        block.style.fontSize = "40px";
      }else if (block.getHTML() === "4"){
        block.style.backgroundColor = "#ede0c8";
        block.style.boxShadow = "0 0 30px 10px rgba(243, 215, 116, 0), inset 0 0 0 1px rgba(255, 255, 255, 0)";
        block.style.fontSize = "40px";
      }else if (block.getHTML() === "8"){
        block.style.backgroundColor = "#f2b179";
        block.style.color = "#f9f6f2";
        block.style.fontSize = "40px";
      }else if (block.getHTML() === "16"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#f59563";
        block.style.fontSize = "35px";
      }else if (block.getHTML() === "32"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#f67c5f";
        block.style.fontSize = "35px";
      }else if (block.getHTML() === "64"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#f65e3b";
        block.style.fontSize = "35px";
      }else if (block.getHTML() === "128"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#edcf72";
        block.style.boxShadow = "0 0 30px 10px rgba(243, 215, 116, 0.2381), inset 0 0 0 1px rgba(255, 255, 255, 0.14286)";
        block.style.fontSize = "30px";
      }else if (block.getHTML() === "256"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#edcc61";
        block.style.boxShadow = "0 0 30px 10px rgba(243, 215, 116, 0.31746), inset 0 0 0 1px rgba(255, 255, 255, 0.19048)";
        block.style.fontSize = "30px";
      }else if (block.getHTML() === "512"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#edc850";
        block.style.boxShadow = "0 0 30px 10px rgba(243, 215, 116, 0.39683), inset 0 0 0 1px rgba(255, 255, 255, 0.2381)";
        block.style.fontSize = "30px";
      }else if (block.getHTML() === "1024"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#edc53f";
        block.style.boxShadow = "0 0 30px 10px rgba(243, 215, 116, 0.47619), inset 0 0 0 1px rgba(255, 255, 255, 0.28571)";
        block.style.fontSize = "25px";
      }else if (block.getHTML() === "2048"){
        block.style.color = "#f9f6f2";
        block.style.backgroundColor = "#3c3a32";
        block.style.fontSize = "25px";
      }
    }
  }
})
</script>

<style>
body{
  padding-top: 30px;
  background-color: #efeeee;
}
#topic{
  font-family: "harmony", sans-serif;
  position: relative;
  margin: 60px auto auto;
  width: 360px;
  display: flex;
  justify-content: space-between;
  align-items: end;
}

#name{
  font-size: 40px;
  font-weight: bolder;
  color: #44403c;
}

#restart{
  background-color: #bd956f;
  width: 100px;
  height: 40px;
  color: white;
  text-align: center;
  line-height: 40px;
  border-radius: 5px;
}

#score{
  background-color: #a78d74;
  width: 100px;
  height: 60px;
  color: white;
  text-align: center;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  font-weight: bold;
}

#number{
  font-size: 17px;
}

#container{
  width: 350px;
  height: 350px;
  background-color: #bbada0;
  position: relative;
  margin: 50px auto auto;
  border-radius: 5px;
  border: 5px solid #bbada0;
}

.row{
  height: calc(100% / 4);
  width: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.block{
  width: 75px;
  height: 75px;
  border-radius: 5px;
  line-height: 75px;
  font-family: "harmony", sans-serif;
  text-align: center;
  color: #776E65;
  background-color: rgba(238, 228, 218, 0.35);
  font-weight: bolder;
}

#control{
  width: 400px;
  display: flex;
  justify-content: space-around;
  position: relative;
  margin: 40px auto auto;
}

img{
  display: block;
  width: 80px;
  filter: drop-shadow(0px 0px 3px #c0c0c0);
  background-color: #a09487;
  border-radius: 50%;
}
</style>