<template>
  <div class="container">
    <div class="card mb-3" style="width: 70%; margin: auto">
      <div class="row g-0">
        <div class="col-md-4">
          <img src="@/assets/logo.png" class="img-fluid rounded-start" alt="profile">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">{{ nickname }} 님의 마이페이지</h5>
            <p class="card-text">Email: {{ email }}</p>
            <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data:function(){
    return{
      nickname: '',
      email: '',
    };
  },
  async mounted() {
    this.nickname = localStorage.getItem('nickname')
    this.email = localStorage.getItem('email')
  }
}

</script>
<style scoped>
.card {
    background-color: black;
    color: #FABD02;
    min-width: 40px;
}
.card-title {
    font-size: 1.8rem;
    margin-bottom: 30px;
}
</style>