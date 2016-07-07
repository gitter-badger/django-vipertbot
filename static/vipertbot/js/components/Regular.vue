<!--suppress XmlInvalidId -->
<template>
    <!-- todo: add following status, maybe require regulars to be following channel -->
    
    <div class="panel-body">
        <div class="container-fluid">
            <!-- Name -->
            <div class="row">
                <div class="col-md-10">
                    <h4 v-if="!Editing">{{ Name }}</h4>
                </div>
                <div class="col-md-2">
                    <button @click="remove()" type="button" class="btn btn-danger btn-sm">
                        <i class="fa fa-remove"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                ID: this.item.id,
                Name: this.item.name
            }
        },

        methods: {

            remove: function() {
                this.$http.delete(window.location.origin + '/api/regulars/'+this.ID+'/delete').then(function(response) {
                    this.$dispatch('refreshRequested');
                }).catch(function(response) {
                    console.log(response);
                });
            }
        },

        computed: {

        },

        props: [
            'item'
        ],

        ready: function() {
           // console.log(this.item)
        }
    }
</script>