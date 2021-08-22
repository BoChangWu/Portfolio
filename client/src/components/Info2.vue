<template>
    <div id="info2">
        <Mypic class="info2left" :picUrl="livePic"/>
        <BasicInfo class="info2right"/>

    </div>
</template>

<script>
import BasicInfo from '@/components/BasicInfo.vue'
import Mypic from '@/components/Mypic.vue'
export default {
    name:'Info2',
    data(){
        return{
            livePic: 'Json2.jpg'
        }
    },
    components:{
        BasicInfo,
        Mypic
    }
}
</script>

<style>
#info2{
    background-color: #42b983;
    display: flex;
    height: 900px;
    
}
.info2left{
    flex: 4;
}
.info2right{
    flex: 6;
}
</style>