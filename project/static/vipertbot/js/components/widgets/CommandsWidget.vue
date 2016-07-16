<template>
    <widget fullscreen="true">
        <div slot="title">Commands</div>
        <div slot="icon">
            <!-- add a icon example: <i class="fa fa-comments txt-color-white"></i> -->
            <i class="fa fa-table"></i>
        </div>

        <div slot="body">
            <!-- MAIN CONTAINER -->
            <div class="alert alert-info no-margin fade in">
                <button class="close" data-dismiss="alert">
                    ×
                </button>
                <i class="fa-fw fa fa-info"></i>
                Add custom colors to your TR and TD <code>&lt;tr&gt;</code> by adding <code>.success</code>, <code>.danger</code>,
                <code>.warning</code> and <code>.info</code> respectively
            </div>
            <div class="table-responsive">

                <table class="table">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th><i class="fa fa-building"></i> Product</th>
                        <th><i class="fa fa-calendar"></i> Payment Taken</th>
                        <th><i class="glyphicon glyphicon-send"></i> Status</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr class="success">
                        <td>1</td>
                        <td>TB - Monthly</td>
                        <td>01/04/2012</td>
                        <td>Approved</td>
                    </tr>
                    <tr class="danger">
                        <td>2</td>
                        <td>TB - Monthly</td>
                        <td>02/04/2012</td>
                        <td>Declined</td>
                    </tr>
                    <tr class="warning">
                        <td>3</td>
                        <td>TB - Monthly</td>
                        <td>03/04/2012</td>
                        <td>Pending</td>
                    </tr>
                    <tr class="info">
                        <td>4</td>
                        <td>TB - Monthly</td>
                        <td>04/04/2012</td>
                        <td>Call in to confirm</td>
                    </tr>
                    </tbody>
                </table>
            </div>

        </div>
        <!-- end body -->
    </widget>
</template>
<style>

</style>
<script>
    import Widget from './Widget.vue'

    export default{
        props: ['user'],

        data: function () {
            return {
                RandomID: RandomNum()
            }
        },
        components: {
            Widget
        },
        methods: {

        },
        computed: {

        }
    }
</script>
