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
            name: 'score',
            data: []
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
                      fontSize: '10px',
                      fontFamily: 'Pretendard-Regular'
                  }
              }
            },
            yaxis: {
              categories: ['E Score', 'S Score', 'G Score'],
              labels: {
                  style: {
                      colors: ['#FABD02'],
                      fontSize: '10px',
                      fontFamily: 'Pretendard-Regular'
                  }
              }
            },
          },
        }
    },

    async mounted() {
    let temp = localStorage.getItem('mbti').split(",")
          for ( var i in temp ) {
            console.log(i)
    this.series[0].data.push(parseInt(temp[i]))
      }
           console.log(temp)
  }      
}
</script>
<style scoped>
</style>