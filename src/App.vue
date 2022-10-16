<template>
    <div id="app">
        <div id="content">
            <transition name="fade">
                <router-view></router-view>
            </transition>
        </div>
        <div id="footer">

        </div>
    </div>
</template>

<script>

// import axios from 'axios';

export default {
    name: 'app',
    data() {
        return {
            loading: true,
        }
    },
    mounted() {
    },
    methods: {}
}
</script>

<style lang="scss">

$white: #fff;
$light: #f8f9fa;
$black: #201A16;
$lightGrey: #f2f2f2;
$red: #EB423D;
$yellow: #FEC63D;
$green: #69be28;
$darkGreen: #629C44;
$purple: #912D8D;

html,
body {
    background-color: $lightGrey;
}

#app {
    font-family: 'Rubik', sans-serif !important;
    letter-spacing: 2px;

    .navbar {
        height: 90px;

        #nav_collapse {
            background-color: #f8f9fa !important;
        }
    }
}

.fade-enter-active, .fade-leave-active {
    transition-property: opacity;
    transition-duration: .25s;
}

.fade-enter-active {
    transition-delay: .25s;
}

.fade-enter, .fade-leave-active {
    opacity: 0
}

.spacing-big {
    padding: 40px;
}

.spacing-medium {
    padding: 20px;
}

.loading {
    text-align: center;
}

</style>
