<template>
  <div>
    <button @click="getData">获取数据</button>
    <p>{{message}}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      message: ''
    }
  },
  methods:{
    async getData(){
      try{
        const response = await axios.get("http://127.0.0.1:8000/")
        this.message = response.data.message;
      } catch(error){
        this.message = '获取数据失败'
      }
    }
  }
}
</script>