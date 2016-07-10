<!--suppress XmlInvalidId -->
<template>
    <div class="panel-body">
        <div class="container-fluid">
            <div class="row">
                <div class="alert alert-{{alert_type}} alert-dismissible text-center" role="alert" v-if="alert_msg">
                  <button type="button" @click="alert_dismissed()" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  {{ alert_msg }}
                </div>
            </div>
            <!-- Name -->
            <div class="row">
                <div class="col-md-6">
                    <h4 v-if="!Editing">
                        <a href="http://www.twitch.tv/{{Name}}" target="_blank">{{ Name }}</a>
                    </h4>
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
                Name: this.item.name,
                old_name: this.item.name,
                alert_msg: false,
                alert_type: 'info'
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
                    this.alert_type = 'success';
                    this.alert_msg = 'Operation completed successfully ...';
                }).catch(function(response) {
                    this.alert_type = 'danger';
                    this.alert_msg = response.data.name;
                    this.Name = this.old_name;
                });
            },
            changeEditState: function() {
                if(this.Editing) {
                    this.update()
                }

                this.Editing = !this.Editing;
            },
            alert_dismissed: function() {
                this.alert_msg = false
                this.alert_type = 'info'
            }
        },

        computed: {

        },

        props: [
            'item'
        ],

        ready: function() {

        }
    }
</script>