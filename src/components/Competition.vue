<template>
    <div id="competition">
        <b-container>
            <b-row>
                <b-col cols="12">
                    <div class="spacing-big"></div>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="10">
                    <h2>{{ competition.title }}</h2>
                    <p class="subtitle">Categoria: {{ competition.sex }} - Rounds:
                        {{ competition.rounds }}</p>
                </b-col>
                <b-col cols="2">
                    <b-button variant="outline-dark" @click="goCompetitions()">
                        <i class="fas fa-arrow-left"></i> Competições
                    </b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <b-button variant="outline-dark" @click="goRank()">Ver ranking</b-button>
                    <b-button variant="outline-dark" disabled>Adicionar
                        Competidor(a)
                    </b-button>
                    <b-button variant="outline-dark" disabled>Registrar Round
                    </b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <div class="spacing-big"></div>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="11">
                    <h4>Competidores:</h4>
                </b-col>
                <b-col cols="1">
                    <b-button variant="outline-dark" disabled>
                        <i class="fas fa-search"></i>
                    </b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <b-card>
                        <b-row>
                            <b-col cols="1">
                                <b-skeleton type="avatar"></b-skeleton>
                            </b-col>
                            <b-col cols="10">
                                <b-skeleton width="85%"></b-skeleton>
                                <b-skeleton width="55%"></b-skeleton>
                                <b-skeleton width="70%"></b-skeleton>
                            </b-col>
                        </b-row>
                    </b-card>
                    <b-card>
                        <b-row>
                            <b-col cols="1">
                                <b-skeleton type="avatar"></b-skeleton>
                            </b-col>
                            <b-col cols="10">
                                <b-skeleton width="85%"></b-skeleton>
                                <b-skeleton width="55%"></b-skeleton>
                                <b-skeleton width="70%"></b-skeleton>
                            </b-col>
                        </b-row>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'Competition',
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
        },
        goRank() {
            let routeData = this.$router.resolve(
                {name: 'competition-rank', params: {id: this.id}}
            );
            window.open(routeData.href, '_blank');
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
