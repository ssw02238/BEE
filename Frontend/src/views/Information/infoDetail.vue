<template>
  <div class="container">
    <h1 class="corporate-name">삼성전자 </h1>
    <p class="ps-2">E(★★★★) S(★★) G(★)</p>
    <!-- ESG evalutaion --> 

    <div class="card">
      <div class="row g-0">

        <div class="col-md-4">
          <Graph/>
        </div>

        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">E: {score1}} | S: {score2} | G: {score3}</h5> 
            <hr style="color:gold; height:5px;">
            <div>
              <Top class="Top"/>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr style="color:gold; height:8px;">

    <!-- 뉴스 목록 --> 


  </div>
</template>

<script>
import Top from '../../components/Top.vue'
import Graph from '../../components/graph_infodetail.vue' 

export default {
  name: 'infoDetail',
  components: {
    Graph,
    Top,
  },  
}
</script>

<style scoped>
.corporate-name {
  color: #FABD02;
  background-color:rgb(0, 0, 0);
  padding: 8px;
}
#chart {
  margin-top: 30px;
}
.card-title {
  color:#FABD02;
  text-align: center;
}
.card {
  background-color:black;
}

</style>