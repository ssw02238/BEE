<template>
  <div>
    <Profile />
    <RouterLink class="routerLink" :to="{ name: 'test' }">
      <p>ESG Mbti</p>
    </RouterLink>
  </div>
</template>

<script>
import Profile from '../../components/Profile.vue';
export default {
  name: 'mypage',
  components: {
    Profile,
  }
}

</script>

<style scoped>
</style>