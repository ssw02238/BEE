<template>
  <table class="table" style="font-size:15px; text-align:center">
      <thead style="background-color:#1b1b1b; color:white; text-align:center">
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">기업</th>
          <th scope="col">E</th>
          <th scope="col">S</th>
          <th scope="col">G</th>
          <th scope="col">총점</th>
        </tr>
      </thead>
      <!-- <tbody v-for="(article, idx) in paginatedArticles" :key="idx" @click="goDetail(article.movieId)" style="background-color:#9d9b9a;">
        <tr>
          <th>{{ 10*(page-1) + idx+1 }}</th>
          <th>{{ article.movietitle }}</th>
          <th>{{ article.content }}</th>
          <th v-if="article.rating === 5">★★★★★</th>
          <th v-else-if="4 <= article.rating">★★★★☆</th>
          <th v-else-if="3 <= article.rating">★★★☆☆</th>
          <th v-else-if="2 <= article.rating">★★☆☆☆</th>
          <th v-else-if="1 <= article.rating">★☆☆☆☆</th>
          <th v-else></th>
        </tr>
      </tbody> -->
      <tbody style="background-color:white; text-align:center">
        <tr>
          <th>1번여</th>
          <th>삼성전자</th>
          <th>15</th>
          <th>30</th>
          <th>25</th>
          <th>75</th>

        </tr>
      </tbody>

    </table>
</template>

<script>
export default {
    name: 'table',

}
</script>

<style>

</style>