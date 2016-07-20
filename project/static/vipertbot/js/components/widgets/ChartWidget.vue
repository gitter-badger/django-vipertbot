<template>
    <widget wid-id="37691" fullscreen="true">
        <div slot="icon">
            <span class="widget-icon"> <i class="fa fa-bar-chart-o"></i> </span>
        </div>

        <div slot="title">
            <h2>Updating Chart (Demo of implementation)</h2>
        </div>

        <div slot="body">
            <div id="updating-chart" class="chart" style="padding: 0px; position: relative;">
                <canvas class="flot-base" width="798" height="220"
                        style="direction: ltr; position: absolute; left: 0px; top: 0px; width: 798px; height: 220px;"></canvas>
                <div class="flot-text"
                     style="position: absolute; top: 0px; left: 0px; bottom: 0px; right: 0px; font-size: smaller; color: rgb(84, 84, 84);">
                    <div class="flot-x-axis flot-x1-axis xAxis x1Axis"
                         style="position: absolute; top: 0px; left: 0px; bottom: 0px; right: 0px; display: block;">
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 26px; text-align: center;">0
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 99px; text-align: center;">10
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 175px; text-align: center;">
                            20
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 251px; text-align: center;">
                            30
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 327px; text-align: center;">
                            40
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 403px; text-align: center;">
                            50
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 478px; text-align: center;">
                            60
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 554px; text-align: center;">
                            70
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 630px; text-align: center;">
                            80
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 706px; text-align: center;">
                            90
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; max-width: 72px; top: 205px; left: 779px; text-align: center;">
                            100
                        </div>
                    </div>
                    <div class="flot-y-axis flot-y1-axis yAxis y1Axis"
                         style="position: absolute; top: 0px; left: 0px; bottom: 0px; right: 0px; display: block;">
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; top: 188px; left: 13px; text-align: right;">0
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; top: 151px; left: 7px; text-align: right;">20
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; top: 114px; left: 7px; text-align: right;">40
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; top: 77px; left: 7px; text-align: right;">60
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; top: 40px; left: 7px; text-align: right;">80
                        </div>
                        <div class="flot-tick-label tickLabel"
                             style="position: absolute; top: 3px; left: 0px; text-align: right;">100
                        </div>
                    </div>
                </div>
                <canvas class="flot-overlay" width="798" height="220"
                        style="direction: ltr; position: absolute; left: 0px; top: 0px; width: 798px; height: 220px;"></canvas>
            </div>
        </div>
    </widget>
</template>
<style>

</style>
<script type="text/babel">
    import Widget from './Widget.vue'

    import {
            AlertSuccess,
            AlertError
    } from '../../modules/alerts'

    export default{
        vuex: {
            actions: {

            },
            getters: {

            }
        },
        components: {
            Widget
        },
        methods: {

        },
        computed: {},
        ready: function () {
            // For the demo we use generated data, but normally it would be coming from the server
            var data = [], totalPoints = 200;

            function getRandomData() {
                if (data.length > 0)
                    data = data.slice(1);

                // do a random walk
                while (data.length < totalPoints) {
                    var prev = data.length > 0 ? data[data.length - 1] : 50;
                    var y = prev + Math.random() * 10 - 5;
                    if (y < 0)
                        y = 0;
                    if (y > 100)
                        y = 100;
                    data.push(y);
                }

                // zip the generated y values with the x values
                var res = [];
                for (var i = 0; i < data.length; ++i)
                    res.push([i, data[i]])
                return res;
            }

            // setup control widget
            var updateInterval = 1000;
            $("#updating-chart").val(updateInterval).change(function () {
                var v = $(this).val();
                if (v && !isNaN(+v)) {
                    updateInterval = +v;
                    if (updateInterval < 1)
                        updateInterval = 1;
                    if (updateInterval > 2000)
                        updateInterval = 2000;
                    $(this).val("" + updateInterval);
                }
            });

            // setup plot
            var options = {
                yaxis: {
                    min: 0,
                    max: 100
                },
                xaxis: {
                    min: 0,
                    max: 100
                },
                colors: ['#7e9d3a'],
                series: {
                    lines: {
                        lineWidth: 1,
                        fill: true,
                        fillColor: {
                            colors: [{
                                opacity: 0.4
                            }, {
                                opacity: 0
                            }]
                        },
                        steps: false

                    }
                }
            };
            var plot = $.plot($("#updating-chart"), [getRandomData()], options);

            function update() {
                plot.setData([getRandomData()]);
                // since the axes don't change, we don't need to call plot.setupGrid()
                plot.draw();

                setTimeout(update, updateInterval);
            }

            update();
        }
    }
</script>
