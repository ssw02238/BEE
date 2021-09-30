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
  props: {
    e_score: Number,
    s_score: Number,
    g_score: Number,
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
          data: [this.e_score, this.s_score, this.g_score],
        }]
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    },
    async mounted(){
      console.log(this.e_score)
    }
  }
          
     
    
</script>
