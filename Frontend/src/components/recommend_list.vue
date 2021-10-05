<template>
  <table class="table" style="width: 25%;margin-right: 25%;">
    <thead>
      <tr>
        <th scope="col">No</th>
        <th scope="col">추천 기업</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(corporate, index, idx) in corporates" :key="idx" @click="moveToDetail(corporate.pk)">
        <th scope="row">{{ index + 1 }}</th>
        <td class=" detail-btn"> {{ corporate.name }} </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'recommend_list',
  props: {
    corporates: Array,
  },
  methods: {
    moveToDetail: function (pk) {
      this.$router.push({ name: 'infoDetail',  params: {pk: pk }})
    }
  }  
}
</script>

<style scoped>
.detail-btn:hover {
  text-decoration: underline;
  text-underline-position:under;
  cursor: pointer;}

</style>