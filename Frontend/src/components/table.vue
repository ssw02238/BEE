<template>
  <table class="table" style="font-size:15px; text-align:center">
      <thead style="background-color:#1b1b1b;">
        <tr>
          <th scope="col" style="width:5%">No</th>
          <th scope="col" style="width:15%">기업</th>
          <th scope="col" style="width:10%">E</th>
          <th scope="col" style="width:10%">S</th>
          <th scope="col" style="width:10%">G</th>
          <th scope="col" style="width:15%">총점</th>
        </tr>
      </thead>
      <tbody v-for="(corporate, idx) in paginated" :key="idx"
      @click="goDetail(corporate.pk)" class="table-body">
        <tr id="font">
          <th><div type="button">{{ 10 * (page - 1) + idx + 1 }}</div></th>
          <th><div type="button">{{ corporate.name }}</div></th>
          <th><div type="button">{{ corporate.E_rating.toFixed(2) }}</div></th>
          <th><div type="button">{{ corporate.S_rating.toFixed(2) }}</div></th>
          <th><div type="button">{{ corporate.G_rating.toFixed(2) }}</div></th>
          <th><div type="button">{{ corporate.ESG_rating.toFixed(2) }}</div></th>
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

<style scoped>
.table-body:hover {
  background-color: rgba(255,255,255,0.55);
  cursor: pointer;
}

</style>