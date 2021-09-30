<!-- 레이더 차트 -->
<template>
    <div id="chart">
                  <h5 style="color:white;"> ESG 성향 </h5>

        <apexchart type="radar" height="250" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>
<script>
 import VueApexCharts from 'vue-apexcharts'
export default {
  components: {

    apexchart: VueApexCharts,
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
