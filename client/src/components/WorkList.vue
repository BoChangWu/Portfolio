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
                tools:'JavaScript,Node.js,Docker,AWS,Azure',
                link: 'http://ec2-54-254-209-235.ap-southeast-1.compute.amazonaws.com/'
            },
            {
                id:1,
                name: '104_scraping',
                img:'',
                tools:'python,Jupyter',
                link: 'https://github.com/BoChangWu/Job104_python_scraping.git'
            },
            {
                id:2,
                name: 'zh_scraping',
                img: '',
                tools:'python,Jupyter',
                link: 'https://github.com/BoChangWu/zh_python_scraping.git'
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