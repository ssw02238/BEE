<template>
  <div>
    <Profile />
<div class="row">
  <div class="col">
<!-- 테이블 시작 -->
<table class="table table-dark" style="width: 500px;margin-left:25%;">
  <thead>
    <tr>
      <th scope="col">No</th>
      <th scope="col">기사 제목</th>

    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>ESG 경영 논란 ~~~ </td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>ESG 경영 논란 ~~~ </td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>ESG 경영 논란 ~~~ </td>
    </tr>
  </tbody>
</table>
  </div>
<!-- 테이블 종료 -->
  
  <!-- ESG Chart 시작 -->
  <div class="col">
<div class="card" style="width: 500px;margin-right:20%;" >
  <div class="card-body">
    <h5 class="card-title"> ESG 성향 </h5>
    <p class="card-text">일단 뭐 쓸거 없어서 암거나 써놨음 </p>
        <Graph/>
  </div>
</div>
  </div>
    <!-- ESG Chart 종료 -->
</div>

    <RouterLink class="routerLink" :to="{ name: 'test' }">
      <p>ESG Mbti</p>
    </RouterLink>

    <div class="row">
</div>
  </div>
</template>

<script>
import Profile from '../../components/Profile.vue';
import Graph from '../../components/graph_mypage.vue';

export default {
  name: 'mypage',
  components: {
    Profile,Graph
  },
  }
          
     
    
</script>

<style scoped>
th,td{
    text-align: center;
}
</style>