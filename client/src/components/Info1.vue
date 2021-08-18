<template>
    <div id="info1">
        <Introduce class="infoLeft" />
        <Mypic class="infoRight" :picUrl="mypic"/>
    </div>
</template>

<script>
import Introduce from '@/components/Introduce.vue'
import Mypic from '@/components/Mypic.vue'
export default {
    name: 'Info1',
    data(){
        return{
            mypic:'jsonwu.png'
        }
    },
    components:{
        Introduce,
        Mypic,
    }
}
</script>

<style>
#info1{
    /* background-color: #51e29f; */
    display: flex;
    height: 900px;
}
.infoLeft{
    flex: 6;
}
.infoRight{
    flex:4;
}
</style>