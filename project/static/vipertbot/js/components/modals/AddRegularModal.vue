<template>
    <modal modal-id="AddRegularModal">
        <div slot="title">Add A Regular</div>

        <div slot="body">
            <form>
                <!-- row -->
                <div class="row">
                    <div class="col-md-12">
                        <div class="form-group">
                            <input class="form-control"
                                   type="text"
                                   @keydown.enter.prevent="addNew()"
                                   v-model="formModel.name"
                                   placeholder="Twitch User ..."
                                   required
                            />
                        </div>
                    </div>
                </div>
            </form>
        </div> <!-- end body -->

        <div slot="footer">
            <button @click="clearFields()" type="button" class="btn btn-default" data-dismiss="modal">
                Cancel
            </button>
            <button @click="addNew()" type="button" class="btn btn-primary">
                Add
            </button>
        </div> <!-- end footer -->
    </modal>
</template>
<style>

</style>
<script type="text/babel">
    import Modal from './Modal.vue'
    import { addRegular } from '../../vuex/actions'

    export default{
        vuex: {
            actions: {
                addRegular
            }
        },

        data: function () {
            return {
                formModel: {
                    name: ''
                }
            }
        },
        components: {
            Modal
        },
        methods: {
            addNew: function (e) {
                if(e) e.preventDefault()

                this.$http.post(window.location.origin + '/api/regulars/create/', this.formModel)
                        .then(function (response) {
                            this.addRegular(response.data)
                            console.log(response.data)
                            $.smallBox({
                                title: "Regular Successfully Added",
                                content: "",
                                color: "#739E73",
                                iconSmall: "fa fa-thumbs-up bounce animated",
                                timeout: 4000
                            });

                            this.clearFields()
                            $("#AddRegularModal").modal('hide');
                        }.bind(this))

                        .catch(function (response) {
                            $.bigBox({
                                title: "Error",
                                content: response.data.name,
                                color: "#C46A69",
                                icon: "fa fa-warning shake animated",
                                //number : "",
                                timeout: 7000
                            });
                });
            },
            clearFields: function() {
                for (var item in this.formModel) {
                    this.formModel[item] = ''
                }
            }
        },
        events: {
            'ModalClosing': function() {
                this.clearFields()
            }
        },
        ready: function() {

        }
    }
</script>
