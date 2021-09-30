<!-- 세로 막대 차트 -->
<template>
    <div id="chart">
      <p class="card-text" style="font-size:1.5rem;">평균 점수</p>
        <apexchart style="color:#FABD02;" class="chart" type="bar" height="200" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    name: 'graph_rank',
    components: {
        apexchart: VueApexCharts,
    },
    props: {
      e_avg: Number,
      s_avg: Number,
      g_avg: Number
    },
    data() {
        return {
            series: [{
              data: [this.e_avg, this.s_avg, this.g_avg]
          }],
          chartOptions: {

            fill: {
                colors: ['#FABD02']
            },
            plotOptions: {
              bar: {
                borderRadius: 4,
              }
            },
            dataLabels: {
              enabled: false,
            },
            xaxis: {
              categories: ['E Score', 'S Score', 'G Score'],
              labels: {
                  style: {
                      colors: ['#FABD02','#FABD02','#FABD02'],
                      fontSize: '15px',
                      fontFamily: 'Pretendard-Regular'
                  }
              }
            },
          },
        }
    },
    // async mounted() {
    //   console.log(this.e_avg, '평균 e')
    // }   
}
</script>
<style scoped>
</style>