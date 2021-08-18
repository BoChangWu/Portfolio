<template>
    <div id="info2">
        <div class="info2left">
            <h1>left</h1>
        </div>
        <BasicInfo class="info2right"/>

    </div>
</template>

<script>
import BasicInfo from '@/components/BasicInfo.vue'
export default {
    name:'Info2',
    components:{
        BasicInfo,
    }
}
</script>

<style>
#info2{
    display: flex;
    height: 900px;
    
}
.info2left{
    flex: 4;
    background-color: #42b983;
}
.info2right{
    flex: 6;
    background-color: #3ca876;
}
</style>