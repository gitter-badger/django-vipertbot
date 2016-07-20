<template>
    <!-- projects dropdown -->
    <div class="project-context hidden-xs">

        <span class="label">Dev Activity:</span>
        <span class="project-selector dropdown-toggle" data-toggle="dropdown">Recent Commits <i
                class="fa fa-angle-down"></i></span>

        <!-- Suggestion: populate this list with fetch and push technique -->
        <ul class="dropdown-menu">
            <li v-for="record in commits">
                <a :href="record.html_url" target="_blank" class="commit">{{ record.sha.slice(0, 7) }}
                    - {{ record.commit.message | truncate }}<br/>
                    by {{ record.commit.author.name }}
                    at {{ record.commit.author.date | formatDate }}
                </a>
            </li>
        </ul>
        <!-- end dropdown-menu-->

    </div>
    <!-- end projects dropdown -->
</template>
<style>

</style>
<script>
    // import HeaderComponent from './components/header.vue'
    // import OtherComponent from './components/other.vue'
    export default{
        data: function () {
            return {
                apiURL: 'https://api.github.com/repos/poppabear8883/django-vipertbot/commits?per_page=3&sha=',
                currentBranch: 'master',
                commits: null
            }
        },
        components: {},
        filters: {
            truncate: function (v) {
                var newline = v.indexOf('\n')
                return newline > 0 ? v.slice(0, newline) : v
            },
            formatDate: function (v) {
                return v.replace(/T|Z/g, ' ')
            }
        },
        methods: {
            fetchData: function () {
                var xhr = new XMLHttpRequest()
                var self = this
                xhr.open('GET', this.apiURL + self.currentBranch)
                xhr.onload = function () {
                    self.commits = JSON.parse(xhr.responseText)
                }
                xhr.send()
            }
        },
        ready: function () {
            this.fetchData()
        }
    }
</script>
