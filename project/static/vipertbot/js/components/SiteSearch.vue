<template>
    <!-- input: search field -->
    <form action="#" class="header-search pull-right">
        <input id="search-fld"  type="text" name="param" placeholder="Search ..." data-autocomplete='[
        "Commands",
        "Regulars",
        "Twitch",
        "Followers",
        "Following",
        "Status",
        "Royalties",
        "Songs",
        "Playlists"
        ]'>
        <button type="submit">
            <i class="fa fa-search"></i>
        </button>
        <a href="javascript:void(0);" id="cancel-search-js" title="Cancel Search"><i class="fa fa-times"></i></a>
    </form>
    <!-- end input: search field -->
</template>
<style>
    
</style>
<script>
    // import HeaderComponent from './components/header.vue'
    // import OtherComponent from './components/other.vue'
    export default{
        data: function() {
            return{
                
            }
        },
        components:{
            
        },
        methods: {
        
        }
    }
</script>
