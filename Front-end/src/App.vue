<template>
  <div id="back">

    <!-- nav bar --> 
    <div class="logo">
      <RouterLink :to="{ name: 'main' }">
          <img src="@/assets/logo.png" width="100" class="pt-2">
      </RouterLink>
    </div>
    <div class="navbar">
      <nav class="nav main-nav">
        <RouterLink :to="{ name: 'serviceIntro' }">
          <p class="nav-text">About</p>
        </RouterLink>
        <RouterLink :to="{ name: 'esgRank' }">
          <p class="nav-text">Rank</p>
        </RouterLink>
        <RouterLink :to="{ name: 'newsList' }">
          <p class="nav-text">News</p>
        </RouterLink>
      </nav>
      
      <nav class="nav sub-nav">
        <RouterLink :to="{ name: 'login' }">
          <p class="nav-text2">Log in</p>
        </RouterLink>
        
        <RouterLink :to="{ name: 'signup' }">
          <p class="nav-text2">Sign in</p>
        </RouterLink>
      </nav>

    </div>

    <!-- footer --> 
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 50px;
}
#back {
  background-image: url("back.png"); 
  background-size: cover;
  height: 100%;
}

.main-nav {
  background-color: black;
  color:#FABD02;
  width: 40%;
  /* 화면 비율에 따라 */ 
  min-width: 20%;
  height: 40px;
  /* position: fixed; */
  justify-content: space-around;
  align-content: center;
}

.navbar {
  background-color: black;
  color:#FABD02;
}
.sub-nav {
  width: 10%;
  /* 화면 비율에 따라 */ 
  min-width: 10%;
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
</style>
