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
        </b-container>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'CompetitionRank',
    props: ['id'],
    data() {
        return {
            loading: true,
            competitionEndpoint: "/api/v1/competition/{id}",
            competition: {},
        }
    },
    beforeMount() {
        this.fetchCompetition();
    },
    mounted() {
    },
    methods: {
        fetchCompetition() {
            this.memberLoading = true;
            axios.get(this.competitionEndpoint.replace('{id}', this.id)).then(function (response) {
                this.competition = response.data;
            }.bind(this)).catch(function (error) {
                this.$router.push({name: 'not-found'});
            }.bind(this));
        },
        goCompetitions() {
            this.$router.push({name: 'index'})
        }
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

</style>
