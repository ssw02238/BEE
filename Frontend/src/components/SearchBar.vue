<template>
  <div class="d-flex">
    <form action="#" @submit="search">
      <input v-model="searchContent" placeholder="기업 검색" >
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SearchBar',
  data: function () {
    return {
      searchContent: ''
    }
  },
  methods: {
    search: function () {
      axios.get( `corporates/search/${this.searchContent}`)
        .then(res => {
          this.$router.push({name: 'infoDetail', params: {pk: res.data.pk}})
        })
        .catch((error) => {
          if (error.response) {
            if (error.response.status === 404) {
              alert("존재하지 않는 기업입니다.")
            }
          } else if (error.request) {
            console.log(error.request);
          } else {
            console.log('Error', error.message);
          }
          console.log(error.config);
        });
    },
  }
}
</script>

<style>

</style>