<template>
  <div>

<!-- Rank div 시작 -->
    <div class="card text-center top-card" style="background-color: black; width: 900px; margin: auto;">
      <div class="card-header" style="font-size:2rem; color:white; text-align:left;">
        Ranks
      </div>
      <!-- 드롭다운 -->
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false" style="float: right;">
    Dropdown button
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
    <!-- 드롭다운 끝 -->

    <!-- 랭킹 테이블 시작 -->
      <div class="card-body" style="background-color: black;">
              <Table/>
      </div>
    <!-- 랭킹 테이블 끝 -->
    </div>
    <!-- rank div 끝 -->



<!-- Graph div 시작 -->
    <div class="card text-center top-card" style="background-color: black; width: 900px; margin: auto;">
      <div class="card-header" style="font-size:2rem; color:white; text-align:left;">
        Graphs
      </div>
    <!-- Graph 시작 -->
      <div class="card-body" style="background-color: black;  display: flex;">
        
        <Graph/>
        
        <Graph2/>
        <Scrap/>
              </div>
<!-- Graph 끝 --> 

    </div>

  </div>
</template>

<script>


import Table from '../../components/table.vue'
import Graph from '../../components/graph_rank.vue'
import Graph2 from '../../components/graph_rank2.vue'
import Scrap from '../../components/scrap_rank.vue'
export default {
  name: 'esgRank',
  components: {
  Table,Graph,Graph2,Scrap
  }
}
</script>

<style>
</style>