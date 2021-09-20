<template>
  <div id="back">

    <!-- nav bar --> 
    <nav-bar />


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
    <footer-bar />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import FooterBar from './components/FooterBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    FooterBar,
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
.logo {
  width: 15%;
}

.main-nav {
  background-color:rgb(48, 38, 38);
  border-radius: 20px;
  width: 40%;
  /* 화면 비율에 따라 */ 
  min-width: 20%;
  height: 40px;
  /* position: fixed; */
  justify-content: space-around;
  align-content: center;
}

.sub-nav {
  background-color:rgb(48, 38, 38);
  border-radius: 20px;
  width: 15%;
  /* 화면 비율에 따라 */
  height: 40px;
  align-content: center;
  justify-content: space-around;
  margin-right: 60px;
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
.total-nav {
  width: 80%;
  display: contents;
  color: #FABD02;
}
.nav-content{
  background-color: rgb(34, 33, 33);
  display: contents;
}

footer {
  background-color: #FABD02;
}
</style>