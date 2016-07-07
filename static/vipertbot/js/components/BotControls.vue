<template xmlns:v-on="http://www.w3.org/1999/xhtml">
    <div class="panel panel-default">
        <div class="panel-heading">Bot Controls</div>
        <div class="panel-body text-center">
            <div class="btn-group btn-group-lg" role="group" aria-label="...">
                <button v-on:click="Join()" type="button" class="btn btn-default">
                    <i class="fa fa-arrow-right"></i> Join
                </button>
                <button v-on:click="Part()" type="button" class="btn btn-default">
                    <i class="fa fa-arrow-left"></i> Remove
                </button>
                <button v-on:click="Rejoin()" type="button" class="btn btn-default">
                    <i class="fa fa-refresh"></i> Rejoin
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        methods: {
            Join: function() {
                this.$http.get('cmd/join', function(response) {
                    console.log('Join: ' + response)
                });
            },
            Part: function() {
                this.$http.get('cmd/part', function(response) {
                    console.log('Part: ' + response)
                });
            },
            Rejoin: function() {
                this.$http.get('cmd/rejoin', function(response) {
                    console.log('Rejoin: ' + response)
                });
            }
        }
    }
</script>

<style>

</style>