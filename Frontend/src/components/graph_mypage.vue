<!-- 레이더 차트 -->
<template>
    <div id="chart">
        <apexchart type="radar" height="350" :options="chartOptions" :series="series"></apexchart>
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
