<!-- 도넛 차트 -->
<template>
    <div id="chart">
      <p class="card-text" style="font-size:1.5rem;">데이터 분석 그래프</p>
        <apexchart style="color:#FABD02;" class="chart" type="donut" height="200" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
        apexchart: VueApexCharts,
    },
    data() {
        return {
          series: [30, 29, 79],
          
          chartOptions: {
             labels: ['E Score', 'S Score', 'G Score'],
            fill: {
                colors:['#008ffb', '#00E396', '#FEB019']
            },
          },
        }
    }       
}
</script>
<style scoped>
p {
    color: #FABD02
}
</style>