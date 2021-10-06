<template>
  <div class="container">
    <div class="card" style="width: 70%; margin: auto">
      <div class="row g-0">
        <div class="col">
              <Graph
      :e_score="e_score"
      :s_score="s_score"
      :g_score="g_score"
        />

        </div>
        <div class="col">
          <div class="card-body">
            <h5 class="card-title">{{ nickname }} 님의 마이페이지</h5>
            <p class="card-text">Email: {{ email }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Graph from '../components/graph_mypage.vue';
export default {
  name: 'Profile',
  components:{ 
    Graph
    },
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