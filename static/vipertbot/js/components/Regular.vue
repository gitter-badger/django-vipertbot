<!--suppress XmlInvalidId -->
<template>
    <div class="panel-body">
        <div class="container-fluid">
            <!-- Name -->
            <div class="row">
                <div class="col-md-6">
                    <h4 v-if="!Editing">{{ Name }}</h4>
                    <div v-else class="form-group">
                        <input  type="text" class="form-control" v-model="Name">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="btn-group pull-right">
                        <button @click="changeEditState()" v-if="!Editing" type="button" class="btn btn-primary btn-sm">
                            <i class="fa fa-edit"></i> Edit
                        </button>
                        <button @click="changeEditState()" v-if="Editing" type="button" class="btn btn-info btn-sm">
                            <i class="fa fa-thumbs-o-up"></i> Done
                        </button>
                        <button @click="remove()" type="button" class="btn btn-danger btn-sm">
                            <i class="fa fa-remove"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                Editing: false,
                ID: this.item.id,
                Name: this.item.name
            }
        },

        methods: {

            remove: function() {
                this.$http.delete(window.location.origin + '/api/regulars/'+this.ID+'/delete/').then(function(response) {
                    this.$dispatch('refreshRequested');
                }).catch(function(response) {
                    console.log(response);
                });
            },
            update: function() {
                this.$http.put(window.location.origin + '/api/regulars/'+this.ID+'/edit/',{
                    name: this.Name
                }).then(function(response) {

                }).catch(function(response) {
                    alert(response.data.name)
                });
            },
            changeEditState: function() {
                if(this.Editing) {
                    this.update()
                }

                this.Editing = !this.Editing;
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