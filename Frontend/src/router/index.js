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
},
{
    path: '/',
    name: 'welcome',
    component: welcome,
},
{
    path: '/serviceIntro',
    name: 'serviceIntro',
    component: serviceIntro,
},
{
    path: '/infoDetail/:pk',
    name: 'infoDetail',
    component: infoDetail,
},
{
    path: '/esgRank',
    name: 'esgRank',
    component: esgRank,
},
{
    path: '/newsList',
    name: 'newsList',
    component: newsList,
},
{
    path: '/myPage',
    name: 'myPage',
    component: myPage,
},
{
    path: '/test',
    name: 'test',
    component: test,
},
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
