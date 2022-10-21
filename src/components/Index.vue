<template>
    <div id="index">
        <b-container>
            <b-row>
                <b-col cols="12">
                    <div class="spacing-big"></div>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="6">
                    <h4>Competições:</h4>
                </b-col>
                <b-col cols="6" class="home-btn">
                    <b-button variant="outline-dark" @click="goHighlight()">Ver destaque de round</b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12" v-if="!loading">
                    <b-card v-for="competition in competitions" :key="competition.competition_id" :title="competition.title" :sub-title="competition.sex" @click="goToCompetition(competition.competition_id)">
                    </b-card>
                </b-col>
                <b-col cols="12" v-if="loading">
                    <div class="spacing-big">
                        <h6 class="loading"><i
                            class="fas fa-spinner fa-spin"></i></h6>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'Index',
    data() {
        return {
            loading: true,
            competitionEndpoint: "/api/v1/competition",
            competitions: []
        }
    },
    beforeMount() {
    },
    mounted() {
        this.loadCompetitions();
    },
    methods: {
        loadCompetitions() {
            axios.get(this.competitionEndpoint).then(function (response) {
                // handle success
                this.competitions = response.data;
                this.loading = false;
            }.bind(this)).catch(function (error) {
                console.log(error)
            })
        },
        goToCompetition(competitionId) {
            this.$router.push({name: 'competition', params: {id: competitionId}});
        },
        goHighlight() {
            let routeData = this.$router.resolve(
                {name: 'round-highlight'}
            );
            window.open(routeData.href, '_blank');
        }
    }
}
</script>

<style lang="scss">

.card-title {
    font-size: 1.1rem;
}

.card-subtitle {
    font-size: 0.9rem;
}

.card {
    cursor: pointer;
    margin-top: 10px;
    .card-body {
        padding-top: 15px;
        padding-bottom: 10px;
    }
}

.home-btn {
    text-align: right;
}

</style>
