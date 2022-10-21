<template>
    <div id="competition-rank">
        <b-container>
            <b-row>
                <b-col cols="12">
                    <div class="spacing-medium"></div>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <h2>{{ competition.title }}</h2>
                    <p class="subtitle">Categoria: {{ competition.sex }}</p>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <div class="streamer-header">
                        <div class="ranking-no"></div>
                        <div class="picture"></div>
                        <div class="display-name"></div>
                        <div class="score subtitle"></div>
                        <div class="score">Coef</div>
                    </div>
                    <div class="streamer"
                         v-for="(competitor, i) in rankingData"
                         :key="competitor.id"
                         :ref="(el) => {rankingEl[competitor.id] = el}">
                        <div class="ranking-no">{{ i + 1 }}</div>
                        <div class="picture">
                            <img :src="competitor.picture"/>
                        </div>
                        <div class="display-name">
                            {{ competitor.name }}
                        </div>
                        <div class="score subtitle">
                            {{ competitor.last_valid_round.lifted_weight }} Kg
                        </div>
                        <div class="score">{{ competitor.showScore }}</div>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>

import axios from 'axios';

import {bubbleSort, swapElement} from "../helper.js";

const refreshTime = 300;

export default {
    name: 'CompetitionRank',
    props: ['id'],
    data() {
        return {
            loading: true,
            competitionEndpoint: "/api/v1/competition/{id}",
            rankDataEndpoint: "/api/v1/competition/{id}/rank",
            competition: {},
            rankingEl: [],
            rankingData: [],
            polling: null
        }
    },
    beforeMount() {
        this.fetchCompetition();
        this.fetchRank();
    },
    mounted() {
        setInterval(() => {this.fetchRank()}, 5000);
    },
    methods: {
        goCompetitions() {
            this.$router.push({name: 'index'})
        },
        fetchCompetition() {
            axios.get(this.competitionEndpoint.replace('{id}', this.id)).then(function (response) {
                this.competition = response.data;
            }.bind(this)).catch(function (error) {
                this.$router.push({name: 'not-found'});
            }.bind(this));
        },
        fetchRank() {
            axios.get(this.rankDataEndpoint.replace('{id}', this.id)).then(function (response) {
                this.rankingData = response.data;
                response.data.forEach((data) => {
                    data.last_valid_round.coefficient = parseFloat(data.last_valid_round.coefficient);
                    data.showScore = data.last_valid_round.coefficient;
                });
                let prevPosition = [];
                this.rankingData.forEach((streamers) => {
                    if (this.rankingEl[streamers.id]) {
                        prevPosition[streamers.id] = this.rankingEl[streamers.id].getBoundingClientRect().top;
                    }
                });
                bubbleSort(this.rankingData).then((sortedData) => {
                    // swap position after sorted
                    sortedData.forEach((streamers) => {
                        let newTop = this.rankingEl[streamers.id].getBoundingClientRect().top;
                        let prevTop = prevPosition[streamers.id];
                        let diffY = prevTop - newTop;
                        if (diffY && this.rankingEl[streamers.id]) {
                            // swap position after sorted
                            swapElement(this.rankingEl[streamers.id], diffY, refreshTime);
                        }
                    });
                });
            }.bind(this)).catch(function (error) {
                console.log(error)
            }.bind(this));
        },
    }
}
</script>

<style lang="scss">

$white: #fff;
$light: #f8f9fa;
$black: #201A16;
$lightGrey: #f2f2f2;
$red: #EB423D;
$yellow: #FEC63D;
$grey: #6c757d;

.subtitle {
    color: $grey;
}

.disabled {
    cursor: not-allowed;
}

.streamer {
    margin: 0 auto;
    width: 900px;
    height: 60px;
    transition: all 1s ease 0s;
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 25px;
    border: 1px solid #cecece;
    border-radius: 3px;
    margin-top: 5px;

    .ranking-no {
        width: 100px;
        text-align: center;
    }

    .picture {
        width: 55px;
        text-align: center;
    }

    .picture img {
        margin-right: 2em;
        height: 40px;
        width: 40px;
        border-radius: 50%;
    }

    .display-name {
        width: 350px;
        text-align: left;
    }

    .score {
        width: 150px;
        text-align: right;
    }
}

.streamer-header {
    margin: 0 auto;
    width: 900px;
    height: 60px;
    transition: all 0.3s ease 0s;
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 25px;

    .ranking-no {
        width: 100px;
        text-align: center;
    }

    .picture {
        width: 40px;
        text-align: center;
    }

    .picture img {
        margin-right: 2em;
        height: 30px;
        width: 30px;
        border-radius: 50%;
    }

    .display-name {
        width: 350px;
        text-align: left;
    }

    .score {
        width: 150px;
        text-align: right;
    }
}


</style>
