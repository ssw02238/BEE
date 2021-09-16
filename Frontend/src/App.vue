<template>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
  <div id="back">

    <!-- nav bar --> 
    <div class="total-nav">
      <div class="navbar">
      <div class="logo">
        <RouterLink :to="{ name: 'main' }">
            <img src="@/assets/logo.png" width="100" class="pt-2">
        </RouterLink>
      </div>
      
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
    </div>

    <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>
        <h2>hi</h2>
            <h2>hi</h2>
                <h2>hi</h2>

    <!-- footer --> 
    <footer class="py-3">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item me-2">
          Home 
        </li>
        <li class="nav-item me-2">
          About
        </li>
        <li class="nav-item">
          My Page
        </li>
      </ul>
      <p class="text-center text-muted">김예찬 · 김윤서 · 방지환 · 이규정 · 정희진</p>
      <p class="text-center text-muted">Copyright 2021 BEE ( Best ESG Enterprise ) ®All Rights Reserved</p>
    </footer>
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
}
#back {
  background-image: url("BackgroundIMG.jpg"); 

  min-height: 100%;
  background-position:center;
  background-attachment: fixed;
  border:0;
  padding:0;
  background-size: cover;
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
  background-color: rgb(34, 33, 33);
  color:#FABD02;
}
.sub-nav {
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

footer {
  background-color: #FABD02;
}
</style>
