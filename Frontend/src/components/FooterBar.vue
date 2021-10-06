<template>
    <!-- footer --> 
    <footer class="py-3">

      <div @click="goPage">
        <p class="text-center text-muted">김예찬 · 김윤서 · 방지환 · 이규정 · 정희진</p>
        <p class="text-center text-muted">Copyright 2021 BEE ( Best ESG Enterprise ) ®All Rights Reserved</p>
      </div>
    </footer>
</template>

<script>

export default {
  name: 'FooterBar',
}
</script>

<style scoped>
  .routerLink {
    color:black;
    text-decoration: none;
  }
</style>