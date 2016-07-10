<template xmlns:v-on="http://www.w3.org/1999/xhtml">
    <div class="panel panel-default">
        <div class="panel-heading">Bot Controls</div>
        <div class="panel-body text-center">
            <div class="btn-group btn-group-lg" role="group" aria-label="...">
                <button @click="processJob('join')" type="button" class="btn btn-default">
                    <i class="fa fa-arrow-right"></i> Join
                </button>
                <button @click="processJob('part')" type="button" class="btn btn-default">
                    <i class="fa fa-arrow-left"></i> Remove
                </button>
                <button @click="processJob('rejoin')" type="button" class="btn btn-default">
                    <i class="fa fa-refresh"></i> Rejoin
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        methods: {
            processJob: function(job) {
                this.$http.post(window.location.origin + '/api/jobs/create/', {
                    name: job
                }).then(function(response) {

                }.bind(this)).catch(function(response) {
                    alert(response)
                });
            }
        }
    }
</script>

<style>

</style>