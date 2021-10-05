import Vue from 'vue'
import VueRouter from 'vue-router'
import main from '../views/main.vue'
import serviceIntro from '../views/Intro/serviceIntro.vue'
import welcome from '../views/Intro/welcome.vue'
import esgRank from '../views/Information/esgRank.vue'
import newsList from '../views/Information/newsList.vue'
import myPage from '../views/Mypage/mypage.vue'
import test from '../views/Test/test.vue'
import infoDetail from '../views/Information/infoDetail.vue'

Vue.use(VueRouter)

const routes = [
    {
    path: '/main',
    name: 'main',
    component: main,
    meta: {
        title: "BEE"
    }
},
{
    path: '/',
    name: 'welcome',
    component: welcome,
    meta: {
        title: "BEE"
    }
},
{
    path: '/serviceIntro',
    name: 'serviceIntro',
    component: serviceIntro,
    meta: {
        title: "BEE"
    }
},
{
    path: '/infoDetail/:pk',
    name: 'infoDetail',
    component: infoDetail,
    meta: {
        title: "BEE"
    }
},
{
    path: '/esgRank',
    name: 'esgRank',
    component: esgRank,
    meta: {
        title: "BEE"
    }
},
{
    path: '/newsList',
    name: 'newsList',
    component: newsList,
    meta: {
        title: "BEE"
    }
},
{
    path: '/myPage',
    name: 'myPage',
    component: myPage,
    meta: {
        title: "BEE"
    }
},
{
    path: '/test',
    name: 'test',
    component: test,
    meta: {
        title: "BEE"
    }
},
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.afterEach((to, from) => {
    Vue.nextTick(() => {
      document.title = to.meta.title;
      console.log(from)
    });
  });


export default router
