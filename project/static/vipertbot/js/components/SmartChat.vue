<template>
<!-- new widget -->
<div class="jarviswidget jarviswidget-color-blueDark" id="wid-id-1" data-widget-editbutton="false" data-widget-fullscreenbutton="false">

    <!-- widget options:
    usage: <div class="jarviswidget" id="wid-id-0" data-widget-editbutton="false">

    data-widget-colorbutton="false"
    data-widget-editbutton="false"
    data-widget-togglebutton="false"
    data-widget-deletebutton="false"
    data-widget-fullscreenbutton="false"
    data-widget-custombutton="false"
    data-widget-collapsed="true"
    data-widget-sortable="false"

    -->

    <header>
        <span class="widget-icon"> <i class="fa fa-comments txt-color-white"></i> </span>
        <h2> SmartChat </h2>
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
    </header>

    <!-- widget div-->
    <div>
        <!-- widget edit box -->
        <div class="jarviswidget-editbox">
            <div>
                <label>Title:</label>
                <input type="text" />
            </div>
        </div>
        <!-- end widget edit box -->

        <div class="widget-body widget-hide-overflow no-padding">
            <!-- content goes here -->

            <!-- CHAT CONTAINER -->
            <div id="chat-container">
                <span class="chat-list-open-close"><i class="fa fa-user"></i><b>!</b></span>

                <div class="chat-list-body custom-scroll">
                    <ul id="chat-users">
                        <li>
                            <a href="#">
                                <img src="{{static_path}}/img/avatars/5.png" alt="">
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
                        <img src="{{static_path}}/img/avatars/5.png" class="online" alt="">
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
                            <i></i>Press <strong> ENTER </strong> to send </label> </span> <a href="#" class="pull-left"><i class="fa fa-camera fa-fw fa-lg"></i></a> </span>

            </div>

            <!-- end content -->
        </div>

    </div>
    <!-- end widget div -->
</div>
<!-- end widget -->
</template>
<script>
    export default {
        props: ['static_path'],
        methods: {

        }
    }
</script>