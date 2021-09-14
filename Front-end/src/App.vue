<template>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
  <div id="back">
    <!-- nav bar --> 
    <ul class="nav justify-content-center">
      <li class="nav-item">
        <RouterLink :to="{ name: 'serviceIntro' }">
          <h2>About</h2>
        </RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{ name: 'esgRank' }">
          <h2>Rank</h2>
        </RouterLink>
      </li>
      <li class="nav-item">
        <RouterLink :to="{ name: 'newsList' }">
          <h2>News</h2>
        </RouterLink>
      </li>
    </ul>

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
  color: #2c3e50;
  margin-top: 60px;
}
#back {
  background-image: url("BackgroundIMG.png"); 

  min-height: 100%;
  background-position:center;
  background-attachment: fixed;
  border:0;
  padding:0;
}

</style>
