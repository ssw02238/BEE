<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid mx-5 px-5">
        <div class="d-flex">
                    <RouterLink :to="{ name: 'main' }">
            <img src="@/assets/logo.png" width="150" class="pt-2">
        </RouterLink>

        </div>

        <div class="d-flex justify-content-between">
          <div
            class="collapse navbar-collapse"
            style="ms-auto me-auto d-flex justify-content-between"
          >
            <ul class="navbar-nav mb-2 mb-lg-0">
              <li class="nav-item mx-3 px-3">
                <a class="nav-link" href="/serviceIntro">About</a>
              </li>
              <li class="nav-item mx-3 px-3">
                <a class="nav-link" href="/esgRank">Rank</a>
              </li>
              <li class="nav-item mx-3 px-3">
                <a class="nav-link" href="/newsList">News</a>
              </li>

              <li class="nav-item mx-3 px-3">
                <a class="nav-link" data-toggle="modal" data-target="#myModal"
                  >login</a>
                <!-- <a v-if="isLogin" class="nav-link" @click.prevent="logout">로그아웃</a> -->
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>

    <!-- Modal -->
    <div
      class="modal fade"
      id="myModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="myModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-center">
            <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button> -->
            <a class="modal-title" id="myModalLabel">로그인</a>
          </div>
          <div class="modal-body">
            <button
              type="button"
              class="my-3"
              style="
                border: none;
                border-right: 0px;
                border-top: 0px;
                boder-left: 0px;
                boder-bottom: 0px;
              "
            >
              <img src="@/assets/logo.png" alt=""/>
            </button>
            <button
              type="button"
              class="my-3"
              style="
                border: none;
                border-right: 0px;
                border-top: 0px;
                boder-left: 0px;
                boder-bottom: 0px;
              "
            >
              <img src="@/assets/logo.png" alt=""  />
            </button>
          </div>
          <div class="modal-footer d-flex justify-content-center">
            <button type="button" class="btn btn-default" data-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

export default {
  data() {
    return {};
  },
  computed: {
  },
  methods: {
  },
};
</script>

<style>
#app {

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(34, 33, 33);
}

.nav-link {
  font-size: 15px;
}
</style>
