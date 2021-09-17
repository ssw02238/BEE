// import Vue from 'vue'
import VueRouter from 'vue-router'
import main from '../views/main.vue'
import serviceIntro from '../views/Intro/serviceIntro.vue'
import esgRank from '../views/Information/esgRank.vue'
import newsList from '../views/Information/newsList.vue'


new VueRouter(
    {
        path: '/main',
        name: '/main',
        component: main,
    },
    {
        path: '/serviceIntro',
        name: '/serviceIntro',
        component: serviceIntro,
    },
    {
        path: '/esgRank',
        name: '/esgRank',
        component: esgRank,
    },
    {
        path: '/newsList',
        name: '/newsList',
        component: newsList,
    },
)

