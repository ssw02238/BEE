<template>
  <table class="table" style="font-size:15px; text-align:center">
      <thead style="background-color:#1b1b1b;">
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">기업</th>
          <th scope="col">E</th>
          <th scope="col">S</th>
          <th scope="col">G</th>
          <th scope="col">총점</th>
        </tr>
      </thead>
      <tbody v-for="(corporate, idx) in paginated" :key="idx"
      @click="goDetail(corporate.pk)" style="background-color:black;">
        <tr id="font">
          <th>{{ 10 * (page - 1) + idx + 1 }}</th>
          <th>{{ corporate.name }}</th>
          <th>{{ corporate.E_rating.toFixed(2) }}</th>
          <th>{{ corporate.S_rating.toFixed(2) }}</th>
          <th>{{ corporate.G_rating.toFixed(2) }}</th>
          <th>{{ corporate.ESG_rating.toFixed(2) }}</th>

        </tr>
      </tbody>

    </table>
</template>

<script>
export default {
    name: 'table',
    props: {
      paginated: Array,
      page: Number,
    },
    methods: {
      goDetail(pk) {
       console.log('여기 pk', pk)
      this.$router.push({ name: 'infoDetail',  params: {pk: pk }})
      this.$router.go()
      },  
    }

}
</script>

<style>

</style>