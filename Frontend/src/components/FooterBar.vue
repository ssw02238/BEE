<template>
    <!-- footer --> 
    <footer class="py-3">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item me-2">
          <RouterLink :to="{ name: 'main' }" class="routerLink">
            Home
          </RouterLink>
        </li>
        <li class="nav-item me-2">
          <RouterLink class="routerLink" :to="{ name: 'serviceIntro' }">
            About
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="routerLink" :to="{ name: 'myPage' }">
            My Page
          </RouterLink>
        </li>
      </ul>

      <div @click="goPage">
        <p class="text-center text-muted">김예찬 · 김윤서 · 방지환 · 이규정 · 정희진</p>
        <p class="text-center text-muted">Copyright 2021 BEE ( Best ESG Enterprise ) ®All Rights Reserved</p>
      </div>
    </footer>
</template>

<script>

export default {
  name: 'FooterBar',
  // 몰래 노션 걸어두기 
  methods: {
      goPage(){
        window.open("https://www.notion.so/PJT-d183573c915b4f12a8ca99840df72f0e", "_blank")
      }
    }
}
</script>

<style scoped>
  .routerLink {
    color:black;
    text-decoration: none;
  }
</style>