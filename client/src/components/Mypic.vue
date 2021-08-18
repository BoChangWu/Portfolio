<template>
    <div id="mypic">
        <img :src="'/imgs/'+ picUrl" class="mypic"/>
    </div>
</template>

<script>
export default {
    name: 'mypic',
    props:{
        picUrl: String,
    }
}
</script>

<style scoped>
.mypic{
    /* width: 100%; */
    height: 100%;
}
/* #mypic{ */
    /* background-color: #34af76; */
/* } */
</style>