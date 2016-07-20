<template>
    <div class="btn-group btn-group-justified">
        <a href="#" @click.prevent="processJob('join')" class="btn btn-default bg-color-red txt-color-white">
            <strong>Join</strong>
        </a>
        <a href="#" @click.prevent="processJob('part')" class="btn btn-default">Part</a>
        <a href="#" @click.prevent="processJob('rejoin')" class="btn btn-default">Rejoin</a>
    </div>
</template>

<script type="text/babel">
    import Widget from './Widget.vue'

    export default {
        components: {
            Widget
        },
        methods: {
            processJob: function (job) {
                this.$http.post(window.location.origin + '/api/jobs/create/', {
                    name: job
                }).then(function (response) {

                }.bind(this)).catch(function (response) {
                    alert(response)
                });
            }
        }
    }
</script>

<style>

</style>