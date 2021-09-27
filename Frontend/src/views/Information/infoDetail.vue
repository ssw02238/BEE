<template>
  <div class="container">
    <h1 class="corporate-name">삼성전자 </h1>
    <p class="ps-2">E(★★★★) S(★★) G(★)</p>
    <!-- ESG evalutaion --> 

    <div class="card">
      <div class="row g-0">

        <div class="col-md-4">
          <apexchart class="chart mt-5" type="radar" height="350" :options="chartOptions" :series="series"></apexchart>
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
    <h2 class="corporate-name">News</h2>
    <p class="ps-2">클릭 후 해당 뉴스를 확인해보세요</p>
    <table class="table table-dark table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Title</th>
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr id="font">
          <th scope="row">1</th>
          <td>삼성전자... 에너지 배출량 개선 결과 발표</td>
          <td>2021-08-14</td>
        </tr>
      </tbody>
    </table>
    <hr style="color:gold; height:8px;">

    <!-- 유사기업 보여주기 --> 
    <h2 class="corporate-name">Recommendations</h2>
    
      <div class="row recom">
        <!-- <div v-for="(recommend, idx) in recommends" :key="idx" @click="goDetail(article.movieId)""> -->
        <a href="#" class="list-group-item list-group-item-action" aria-current="true">
          <div class="d-flex justify-content-between">
            <h5 class="mb-1">현대 모비스 ✓8 </h5>
            <small>스크랩 담기 ▲</small>
          </div>
        <p class="mb-1" style="color:black;">E: 60 S:40 G:10</p>
      </a>
      <a href="#" class="list-group-item list-group-item-action" aria-current="true">
          <div class="d-flex justify-content-between">
            <h5 class="mb-1">현대 모비스 ✓8 </h5>
            <small>스크랩 담기 ▲</small>
          </div>
        <p class="mb-1" style="color:black;">E: 60 S:40 G:10</p>
      </a>
      <a href="#" class="list-group-item list-group-item-action" aria-current="true">
          <div class="d-flex justify-content-between">
            <h5 class="mb-1">현대 모비스 ✓8 </h5>
            <small>스크랩 담기 ▲</small>
          </div>
        <p class="mb-1" style="color:black;">E: 60 S:40 G:10</p>
      </a>
    </div>
  </div>
</template>

<script>
import Top from '../../components/Top.vue'
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'infoDetail',
  components: {
    apexchart: VueApexCharts,
    Top,
  },
  data () {
      return {
        chartOptions: {
          chart: {
            id: 'vuechart-example'
          },
          xaxis: {
            categories: ["Environment", "Social", "Governance",]
          }
        },
        series: [{
          name: 'series-1',
          data: [60, 10, 45,]
        }]
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
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
.recom {
  margin-bottom: 50px;
  display:flex;
  justify-content: space-around;
}
a {
  width: 30%
}
</style>