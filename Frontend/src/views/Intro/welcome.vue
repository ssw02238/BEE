<template>
  <div class="container">
    <!-- welcome 상단 --> 
    <div class="card text-center top-card" style="border:none">
      <div class="card-header" style="font-size:2rem;">
        BEE
      </div>

      <div class="card-body">
        <img src="@/assets/logo.png" width="280">
        <p class="card-text" style="font-size:1.5rem;">Best ESG Enterprises</p>
      </div>
      <div class="card-footer">
        <RouterLink :to="{ name: 'main' }" class="routerLink">
          <h2>이 용 하 기 </h2>
        </RouterLink>
      </div>
    </div>
    
    <!-- welcome 하단 --> 
    <sequential-entrance> 
    <div class="moving-card row">
        <div class="card" style="width: 20rem;">
          <img width="30" src="@/assets/welcome1.png" class="card-img-top">
          <div class="card-body">
            <h4 class="card-title">Information</h4>
            <p id="font" class="card-text">기업 정보를 분석하여 BEE만의 ESG 점수를 안내합니다. <br> 해당 점수로 좋은 투자 가치를 실현해보세요!</p>
          </div>
        </div>

        <div class="card" style="width: 20rem;">
          <img src="@/assets/welcome2.png" class="card-img-top me-5">
          <div class="card-body">
            <h4 class="card-title">ESG Test</h4>
            <p id="font" class="card-text">나의 ESG MBTI는 무엇일까?<br> 성향 평가를 통해 투자 성향이 맞는 기업을 찾아보세요</p>
          </div>
        </div>

        <div class="card" style="width: 20rem;">
          <img src="@/assets/welcome3.png" class="card-img-top me-5">
          <div class="card-body">
            <h4 class="card-title">Analysis</h4>
            <p id="font" class="card-text">ESG  점수를 바탕으로 비슷한 유형의 기업을 분류해드립니다.</p>
          </div>
        </div>
      </div> 
    </sequential-entrance>
  </div>
</template>

<script>

export default {
  name: 'welcome',
}
</script>

<style scoped>
.routerLink {
  text-decoration: none;
}
h4, p{
  text-align: center;
}
.card-header, .card-footer, h2 {
  color: #FABD02;
}
.card-title {
  color:rgb(206, 206, 206);
  font-weight: bold;
}
.top-card {
  margin-bottom:50px;
}
.moving-card {
  margin-bottom: 30px;
  display:flex;
  justify-content: space-around;
  border:solid 2px #FABD02
}
.card{
  background-color:black;
}
.card-img-top {
  width: 180px;
  margin:auto;
  margin-top: 30px
}
</style>