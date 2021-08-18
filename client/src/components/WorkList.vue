<template>
    <div id="worklist">
        <div id="wlist" :key="work.id" v-for="work in works">
            <Work :work="work"/>
        </div>
    </div>
</template>

<script>
import Work from '@/components/Work.vue'
export default {
    name: 'WorkList',
    data(){
        works:[]
    },
    created(){
        this.works=[
            {
                id:0,
                name: 'stubeat',
                img: 'stubeat.png',
                link: 'http://ec2-54-254-209-235.ap-southeast-1.compute.amazonaws.com/'
            },
            {
                id:1,
                name: 'poker',
                img:'',
                link: ''
            },
            {
                id:2,
                name: 'python',
                img: '',
                link: ''
            }
        ]
    },
    components:{
        Work
    }
}
</script>

<style>
#wlist{
    display: inline-block;
}
</style>