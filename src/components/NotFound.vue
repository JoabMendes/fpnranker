<template>
    <div id="not-found">
        <b-container>
            <b-row>
                <b-col cols="12">
                    <div id="top-title">
                        <h4>Error 404 - We're sorry, but the requested page
                            could not be found.</h4>
                    </div>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <img src="/static/404.gif" alt="404" id="img">
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>


<script>


export default {
    name: 'NotFound',
    props: [],
    data() {
        return {};
    },
    beforeMount() {
    },
    methods: {}
}

</script>

<style lang="scss">

$darkGreen: #629C44;
$light: #f8f9fa;
$black: #201A16;
$white: #fff;
$lightGrey: #f2f2f2;
$red: #EB423D;
$yellow: #FEC63D;
$green: #69be28;
$purple: #912D8D;


#not-found {
    background-color: rgb(15, 17, 27);
    position: absolute;
    display: block;
    height: 100%;
    width: 100%;
    top: 0px;
    left: 0px;
    z-index: -1;
}

#top-title {
    padding-top: 20px;
    padding-botton: 20px;
    margin: 0 20px 0 20px;

    h4 {
        color: $light;
        text-align: center;
        font-weight: 400;
    }
}

.content-col {
    margin-bottom: 100px;
    padding-right: 30px;
    padding-left: 35px;
}

@media (min-width: 768px) {
    #imgg {
        display: block;
        margin: 50px auto 120px auto;
        width: 500px;
    }
}

@media (max-width: 768px) {
    #imgg {
        display: block;
        margin: 50px auto 150px auto;
        width: 100%;
    }
}


</style>
