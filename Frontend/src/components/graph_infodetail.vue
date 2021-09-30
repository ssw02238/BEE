<!-- 인포디테일 차트 -->
<template>
    <div id="chart">
  <apexchart class="chart mt-5" type="radar" height="350" :options="chartOptions" :series="series"></apexchart>    </div>
  
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    E_rating: Number,
    S_rating: Number,
    G_rating: Number,
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
          data: [this.E_rating,this.S_rating, this.G_rating],
        }]
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    },
    computed: {
    },
    mounted() {
      // console.log('받아온', this.E_rating)
    }
}
</script>

<style scoped>
</style>