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
    import {
        AlertSuccess,
        AlertError
    } from '../../modules/alerts'

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

                this.$http.post(window.location.origin + '/api/regulars/create/', this.formModel).then(function (response) {
                    this.addRegular(response.data)
                    AlertSuccess("Regular Added!")
                    this.clearFields()
                }.bind(this)).catch(function (response) {
                    AlertError(response.data.error, response.statusText, response.status)
                });
            },
            clearFields: function() {
                this.$broadcast('CloseModal')
                for (var item in this.formModel) {
                    this.formModel[item] = ''
                }
            }
        },
        ready: function() {

        }
    }
</script>
