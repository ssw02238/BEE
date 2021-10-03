import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    scrap_list: [],
  },
  mutations: {
    GetScrapList: function (state, corporates) {
      state.scrap_list = corporates
    }
  },
  actions: {
    get_scrap_list: function (context, corporates) {
      context.commit('GetScrapList', corporates)
    }
  },
  modules: {
  }
})
