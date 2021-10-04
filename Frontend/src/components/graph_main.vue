<template>
    <div id="chart">
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
            chart: {
              type: 'bar',
              height: 200,
            },
            fill: {
                colors: ['#FABD02']
            },
            plotOptions: {
              bar: {
                borderRadius: 4,
                horizontal: true,
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
    },
    async mounted() {
    this.series[0].data = localStorage.getItem('mbti')
  }      
}
</script>
<style scoped>
</style>