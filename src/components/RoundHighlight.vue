<template>
    <div id="round-highlight">
        <b-container>
            <b-row>
                <b-col cols="12">
                    <div class="spacing-medium"></div>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <div id="content-highlight">
                        <h2>{{round.competitor.name}} - {{round.competitor.weight}} Kgs</h2>
                        <br/>
                        <b-img center :src="round.competitor.picture" class="highlight-picture" rounded="circle"></b-img>
                        <br/>
                        <h1>{{round.lifted_weight}} Kgs</h1>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>


<script>


import axios from "axios";

export default {
    name: 'RoundHighlight',
    props: [],
    data() {
        return {
            loading: true,
            roundHighlightEndpoint: "/api/v1/round-highlight",
            round: {
                lifted_weight: null,
                competitor: {
                    name: null,
                    weight: null,
                    picture: null
                }
            }
        };
    },
    beforeMount() {
        this.loadHighlight()
    },
    mounted() {
        setInterval(() => {this.loadHighlight()}, 10000);
    },
    methods: {
        loadHighlight() {
            axios.get(this.roundHighlightEndpoint).then(function (response) {
                // handle success
                this.round = response.data;
            }.bind(this)).catch(function (error) {
                console.log(error)
            })
        }
    }
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
$grey: #6c757d;


#content-highlight {
    text-align: center;
    //width: 500px;
    //margin: auto;
    .highlight-picture {
        width: 300px;
    }
    h1 {
        font-size: 100px;
        font-weight: bold;
    }
    h2 {
        color: $grey;
    }
}


</style>
