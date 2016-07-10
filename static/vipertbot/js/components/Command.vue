<!--suppress XmlInvalidId -->
<template>
    <div class="panel-body">
        <div class="container-fluid">
            <!-- BUTTONS / ACTIONS -->
            <div class="row" style="margin-bottom: 10px">
                <div class="btn-group pull-right">
                    <button @click="changeEditState()" v-if="!Editing" type="button" class="btn btn-primary btn-sm">
                        <i class="fa fa-edit"></i> Edit
                    </button>
                    <button @click="changeEditState()" v-if="Editing" type="button" class="btn btn-info btn-sm">
                        <i class="fa fa-thumbs-o-up"></i> Done
                    </button>

                    <button @click="changeActiveState()" v-if="isActive" class="btn btn-success btn-sm">
                        <i class="fa fa-toggle-on"></i> On
                    </button>
                    <button @click="changeActiveState()" v-if="!isActive" class="btn btn-default btn-sm">
                        <i class="fa fa-toggle-off"></i> Off
                    </button>
                </div>
            </div>

            <!-- COMMAND -->
            <div class="row">
                <h4 v-if="!Editing">{{ Command }}</h4>
                <div v-else class="form-group">
                    <input  type="text" class="form-control" v-model="Command">
                </div>
            </div>

            <!-- TEXT -->
            <div class="row">
                <div v-if="!Editing" class="well well-sm">
                    <cite>{{ Text }}</cite>
                </div>
                <div v-else class="form-group">
                    <textarea class="form-control" rows="3" v-model="Text"></textarea>
                </div>
            </div>

            <!-- ROLES -->
            <div class="row">
                <h4 v-if="!Editing">
                    <span v-for="name in ItemRoles"
                          class="label label-default" style="margin-right: 5px">
                        {{ name }}
                    </span>
                </h4>
                <div v-else>
                    <label style="margin-bottom: 5px" class="checkbox-inline" v-for="name in Roles">
                      <input type="checkbox" id="{{name}}" value="{{name}}" v-model="ItemRoles"> {{name}}
                    </label>
                </div>
            </div>

            <!-- COOLDOWN -->
            <div class="row">
                <h5 v-if="!Editing">Cooldown Minutes <span class="label label-default">{{ Cooldown }}</span></h5>

                <div v-else class="form-group">
                    <label for="cooldown">Cooldown Minutes</label>
                    <input id="cooldown" type="number" class="form-control" v-model="Cooldown">
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
                Updating: false,
                ID: this.item.id,
                Command: this.item.name,
                Text: this.item.text,
                Cooldown: this.item.cooldown_min,
                Roles: [],
                ItemRoles: [],
                RoleObjects: [],
                UpdatedRoleObjects: [],
                isActive: this.item.active,
                thisHasRole: false
            }
        },

        methods: {
            changeEditState: function() {
                if(this.Editing) {
                    this.updateCommand()
                }

                this.Editing = !this.Editing;
            },
            changeActiveState: function() {
                this.isActive = !this.isActive;
                this.updateCommand();
            },
            updateCommand: function() {
                this.updateRoleObjects();

                this.$http.put(window.location.origin + '/api/commands/'+this.ID+'/edit/', {
                    name: this.Command,
                    text: this.Text,
                    cooldown_min: this.Cooldown,
                    active: this.isActive,
                    roles: this.UpdatedRoleObjects
                }).then(function(response) {
                    //console.log(response);
                    this.Updating = true;
                }.bind(this)).catch(function(response) {
                    this.Updating = false;
                    //console.log('Error: ' + response)
                });
            },
            getRoles: function() {
                this.$http.get(window.location.origin + '/api/roles/').then(function(response) {
                    //console.log(response.data.results);
                    this.RoleObjects = response.data.results;

                    for (var k in response.data.results) {
                        if (response.data.results.hasOwnProperty(k)) {
                           this.Roles.push(response.data.results[k].name);
                        }
                    }

                    this.getItemRoles()
                }).catch(function(response) {

                });
            },
            getItemRoles: function() {
                for (var k in this.item.roles) {
                    if (this.item.roles.hasOwnProperty(k)) {
                       this.ItemRoles.push(this.item.roles[k].name);
                    }
                }
            },
            updateRoleObjects: function() {
                this.UpdatedRoleObects = []

                for (var k in this.RoleObjects) {
                    if (this.RoleObjects.hasOwnProperty(k)) {
                        if(jQuery.inArray(this.RoleObjects[k].name, this.ItemRoles) !== -1) {
                            this.UpdatedRoleObjects.push(this.RoleObjects[k])
                        }
                    }
                }
            }
        },

        computed: {

        },

        props: [
            'item'
        ],

        ready: function() {
            //console.log(this.item)
            this.getRoles();
        }
    }
</script>