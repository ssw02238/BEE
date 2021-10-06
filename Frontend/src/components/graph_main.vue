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

    //1. split  - localstorage 
    //2. axios  -

    async mounted() {
    let temp = localStorage.getItem('mbti').split(",")
          for ( var i in temp ) {
            console.log(i)
    this.series[0].data.push(parseInt(temp[i]))
      }
           console.log(temp)
    // E
    // this.series[0].data.push(localStorage.getItem('mbti')[0])
    // S
    // this.series[0].data.push(localStorage.getItem('mbti')[2])
    // G
    // this.series[0].data.push(localStorage.getItem('mbti')[4])
  }      
}
</script>
<style scoped>
</style>