<template>
  <div>
    <div class="total-nav">
      <div class="navbar">
        <div style="width: 20%;">
       <div class="logo">
        <RouterLink :to="{ name: 'main' }">
            <img src="@/assets/logo.png" width="150" class="pt-2">
        </RouterLink>
      </div>
        </div>

        <div style="width: 80%; display: contents">

        <nav class="nav main-nav">
          <RouterLink class="routerLink" :to="{ name: 'serviceIntro' }">
            <p class="nav-text">About</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'infoDetail' }">
            <p class="nav-text">infoDetail</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'welcome' }">
            <p class="nav-text">welcome</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'esgRank' }">
            <p class="nav-text">Rank</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'newsList' }">
            <p class="nav-text">News</p>
          </RouterLink>
        </nav>
        

        <nav class="nav sub-nav" v-if="isLogin">
          <RouterLink class="routerLink" :to="{ name: 'myPage' }">
            <p class="nav-text2">{{nickname}}</p>
          </RouterLink>

          <RouterLink @click.native="logout" to="#" class="routerLink">
            <p class="nav-text2">로그아웃</p>
          </RouterLink>
        </nav>

        <nav class="nav sub-nav" v-else>

          <p id="show-modal" @click="showModal = true" class="nav-text2">Log in</p>
          <modal v-if="showModal" @close="showModal = false">
            <h3 slot="header" style="color:#FABD02">Login </h3>
          </modal> 

          <p id="show-modal2" @click="showModal2 = true" class="nav-text2">Sign up</p>
          <modal2 v-if="showModal2" @close="showModal2 = false">
            <h3 slot="header" style="color:#FABD02">Sign Up </h3>
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
    Modal,
    Modal2
  },
  data:function(){
    return{
      isLogin: false,
      nickname: null,
      doItem:"",
      showModal:false,
      showModal2:false,
    };
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem('nickname')
      console.log('logout 성공')

      this.$router.push({ name: 'welcome' })
    },
  },
  async mounted() {
    try {
      const token = localStorage.getItem('jwt')
      if (token) {
        this.isLogin = true
        this.nickname = localStorage.getItem('nickname')
      }
    }
    catch (err) {
      console.log(err)
    }
  }
};
</script>

<style>
.routerLink {
  text-decoration: none;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.main-nav {
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
  width: 15%;
  align-content: center;
  margin-right: 60px;
  /* 화면 비율에 따라 */
  height: 40px;
  justify-content: space-around;
}

.nav-text {
  font-size: 1.5rem;
  align-content: center;
  margin-bottom: 0px;
  padding: 5px;
}

.nav-text2 {
  font-size: 1.2rem;
  margin-bottom: 0px;
  align-content: center;
  padding: 5px;
}
.nav-content{
  display: contents;
}
.total-nav {
  width: 85%;
  display: contents;
  color: #FABD02;
}
p {  
  color:#FABD02;
  }
</style>
