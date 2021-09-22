<template>
  <div>
    <div class="total-nav">
      <div class="navbar">
        <div style="width: 20%; ">
       <div class="logo">
        <RouterLink :to="{ name: 'main' }">
            <img src="@/assets/logo.png" width="150" class="pt-2">
        </RouterLink>
      </div>
        </div>
        <div style="width: 80%;display: contents;background-color:rgb(34, 33, 33)!important">
        <nav class="nav main-nav">
          <RouterLink :to="{ name: 'serviceIntro' }">
            <p class="nav-text">About</p>
          </RouterLink>
          <RouterLink :to="{ name: 'welcome' }">
            <p class="nav-text">welcome</p>
          </RouterLink>
          <RouterLink :to="{ name: 'esgRank' }">
            <p class="nav-text">Rank</p>
          </RouterLink>
          <RouterLink :to="{ name: 'newsList' }">
            <p class="nav-text">News</p>
          </RouterLink>
        </nav>
        
        <nav class="nav sub-nav">
            <p id="show-modal" @click="showModal = true" class="nav-text2">Log in</p>
         <modal v-if="showModal" @close="showModal = false">
        <h3 slot="header">Login </h3>
      </modal> 
            <p id="show-modal2" @click="showModal2 = true" class="nav-text2">Sign up</p>
         <modal2 v-if="showModal2" @close="showModal2 = false">
        <h3 slot="header">Sign Up </h3>
      </modal2> 
        </nav>
        </div>


      </div>
    </div>

  </div>
</template>

<script>
import Modal from "./login.vue"

import Modal2 from "./signup.vue"
export default {
  components:{
    Modal,Modal2
  },
  data:function(){
    return{
      doItem:"",
      showModal:false,
      showModal2:false,
    };
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.main-nav {
  background-color: rgb(34, 33, 33);
  color:#FABD02;
  width: 40%;
  /* 화면 비율에 따라 */ 
  min-width: 20%;
  height: 40px;
  /* position: fixed; */
  justify-content: space-around;
  align-content: center;
}

.sub-nav {
    color:#FABD02;
  width: 10%;
  /* 화면 비율에 따라 */
  height: 40px;
  align-content: center;
  justify-content: center;
  margin-right: 15px;
}

.nav-text {
  font-size: 1.2rem;
  align-content: center;
  margin-bottom: 0px;
  padding: 5px;
}

.nav-text2 {
  font-size: 0.9rem;
  margin-bottom: 0px;
  align-content: center;
  padding: 5px;
}
.nav-content{
  background-color: rgb(34, 33, 33);
  display: contents;
}
p {  color:#FABD02;}
</style>
