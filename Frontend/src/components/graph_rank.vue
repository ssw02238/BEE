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
    name: 'esg_mbti',
    components: {
        apexchart: VueApexCharts,
    },
    data() {
        return {
            series: [{
            data: [35, 14, 20]
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
                      colors: ['#FABD02'],
                      fontSize: '15px',
                      fontFamily: 'Pretendard-Regular'
                  }
              }
            },
          },
        }
    }       
}
</script>
<style scoped>
</style>