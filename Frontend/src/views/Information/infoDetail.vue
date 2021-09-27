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

</style>