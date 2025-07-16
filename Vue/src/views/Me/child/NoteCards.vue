<template>
  <div class="card-container">
    <div id="write-note" @click="goTo('edit')">
      <span>写帖子</span>
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
        <span id="blogs">0</span>
        <span id="likes">---</span>
        <span id="fans">---</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-container{
  display: flex;
  justify-content: space-between;
  padding: 0 40px;
}

#write-note, #note-info{
  width: 150px;
  height: 150px;
  background: rgba(165, 214, 63, 0.4);
  margin-top: 75px;
  border-radius: 20px;
  font-family: "harmony", sans-serif;
  box-shadow: 0 2px 4px  rgba(0, 0, 0, 0.25);
}


#write-note{
  display: flex;
  flex-direction: column;
  padding-left: 27px;
  padding-top: 20px;
}

#write-note span{
  color: rgb(255, 255, 255);
  font-weight: 700;
  font-size: 18px;
}

img[alt="帖子"]{
  width: 40px;
  height: 40px;
  margin-top: 37px;
}

#note-info{
  background: rgba(145, 195, 242, 0.5);
  display: flex;  /*万能Flex小天才:)*/
  flex-direction: row;
  justify-content: space-evenly;
  padding-left: 10px;
}

#note-titles{
  display: flex;
  flex-direction: column;
  height: 150px;
  align-items: center;
  justify-content: space-evenly;
  color: rgba(204, 225, 255, 1);
  font-size: 16px;
}

#note-numbers{
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  width: 50px;
  text-align: center;
  color: #fff;
  font-weight: bold;
}
</style>
<script setup>
import {goTo} from "@/assets/main.js";
</script>