<template>
  <table class="table" style="width: 20%;margin: auto">
    <thead>
      <tr>
        <th scope="col">No</th>
        <th scope="col">스크랩 기업</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(corporate, index, idx) in corporates" :key="idx">
        <th scope="row">{{ index + 1 }}</th>
        <td> {{ corporate.name }} </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'scrap_list',
  props: {
    corporates: Array,
  },
}
</script>

<style>

</style>