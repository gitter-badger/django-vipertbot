<template>
    <widget fullscreen="true">
        <div slot="title">SmartChat</div>
        <div slot="icon"><i class="fa fa-comments txt-color-white"></i> </div>

        <div slot="toolbars">
            <div class="widget-toolbar">
                <!-- add: non-hidden - to disable auto hide -->
                <div class="btn-group">
                    <button class="btn dropdown-toggle btn-xs btn-success" data-toggle="dropdown">
                        Status <i class="fa fa-caret-down"></i>
                    </button>
                    <ul class="dropdown-menu pull-right js-status-update">
                        <li>
                            <a href="javascript:void(0);"><i class="fa fa-circle txt-color-green"></i> Online</a>
                        </li>
                        <li>
                            <a href="javascript:void(0);"><i class="fa fa-circle txt-color-red"></i> Busy</a>
                        </li>
                        <li>
                            <a href="javascript:void(0);"><i class="fa fa-circle txt-color-orange"></i> Away</a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="javascript:void(0);"><i class="fa fa-power-off"></i> Log Off</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- end toolbars -->

        <div slot="body">
            <!-- CHAT CONTAINER -->
            <div id="chat-container">
                <span class="chat-list-open-close"><i class="fa fa-user"></i><b>!</b></span>

                <div class="chat-list-body custom-scroll">
                    <ul id="chat-users">
                        <li>
                            <a href="#">
                                <img src="" alt="">
                                Robin Berry
                                <span class="badge badge-inverse">23</span>
                                <span class="state">
                                    <i class="fa fa-circle txt-color-green pull-right"></i>
                                </span>
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="chat-list-footer">

                    <div class="control-group">

                        <form class="smart-form">

                            <section>
                                <label class="input">
                                    <input type="text" id="filter-chat-list" placeholder="Filter">
                                </label>
                            </section>

                        </form>
                    </div>
                </div>

            </div>

            <!-- CHAT BODY -->
            <div id="chat-body" class="chat-body custom-scroll">
                <ul>
                    <li class="message">
                        <img src="" class="online" alt="">
                        <div class="message-text">
                            <time>
                                2014-01-13
                            </time>

                            <a href="#" class="username">
                                Sadi Orlaf
                            </a>

                            Hey did you meet the new board of director?
                            He's a bit of an arse if you ask me...anyway here is the report you requested.
                            I am off to launch with Lisa and Andrew, you wanna join?
                        </div>
                    </li>
                </ul>
            </div>

            <!-- CHAT FOOTER -->
            <div class="chat-footer">

                <!-- CHAT TEXTAREA -->
                <div class="textarea-div">

                    <div class="typearea">
                        <textarea placeholder="Write a reply..." id="textarea-expand" class="custom-scroll"></textarea>
                    </div>

                </div>

                <!-- CHAT REPLY/SEND -->
                <span class="textarea-controls">
                    <button class="btn btn-sm btn-primary pull-right">
                        Reply
                    </button>
                    <span class="pull-right smart-form" style="margin-top: 3px; margin-right: 10px;">
                        <label class="checkbox pull-right">
                            <input type="checkbox" name="subscription" id="subscription">
                            <i></i>Press <strong> ENTER </strong> to send
                        </label>
                    </span>
                    <a href="#" class="pull-left"><i class="fa fa-camera fa-fw fa-lg"></i></a>
                </span>
            </div>
        </div>
        <!-- end body -->
    </widget>
</template>
<script>
    import Widget from './Widget.vue'

    export default {
        data: function() {
            return {

            }
        },

        components: {
            Widget
        },

        methods: {

        }
    }
</script>