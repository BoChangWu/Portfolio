<template>
    <div>
        <h3>hello {{ msg }}</h3>
    </div>
</template>

<script>
import axios from 'axios'
import Meta from '@/components/Meta.vue'
export default {
    name: 'Ping',
    data(){
        return{
            msg:'',
            metaTag: {}
        }
    },
    methods:{
        getMessage(){
            const path = 'http://localhost:5000/ping'
            axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                    console.log(res)
                })
                .catch((error) => {
                    console.error(error)
                })
        },
    },
    created(){
        this.getMessage()
        this.metaTag={
        ga: $('[property="tracker:google-analytics"]').attr('content'),
        tm: $('[property="tracker:google-tag-manager"]').attr('content'),
        fp: $('[property="tracker:facebook-pixel"]').attr('content')
        }
    },
    compontents:{
        Meta
    }
}
</script>

<style>

</style>