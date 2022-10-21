import Vue from 'vue';

// Libraries
import Router from 'vue-router';
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Router);
Vue.use(BootstrapVue);

// Views
import App from './App.vue'
import Index from './components/Index.vue';
import Competition from './components/Competition.vue';
import CompetitionRank from './components/CompetitionRank.vue';
import NotFound from './components/NotFound.vue';
import RoundHighlight from './components/RoundHighlight.vue';

const router = new Router({
    routes: [
        {
            path: '/',
            name: 'index',
            component: Index,
        },
        {
            path: "/competition/:id",
            name: "competition",
            component: Competition,
            props: true
        },
        {
            path: "/competition/rank/:id",
            name: "competition-rank",
            component: CompetitionRank,
            props: true
        },
        {
            path: "/round-highlight/",
            name: "round-highlight",
            component: RoundHighlight,
        },
        {
            path: "*",
            name: "not-found",
            component: NotFound
        },
    ]
});

new Vue({
    el: '#app',
    render: h => h(App),
    router
});
