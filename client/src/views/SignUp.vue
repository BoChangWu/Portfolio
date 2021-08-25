<template>
    <div id="signup">
        <SignUpForm :mname="mname" :memail="memail" :mpwd="mpwd" @register-go="register"/>
    </div>
</template>

<script>
import axios from 'axios'
import SignUpForm from '@/components/SignUpForm.vue'

export default {
    name:'SignUp',
    data(){
        return{
            mname: '',
            memail: '',
            mpwd: ''
        }
    },
    methods:{
        register(data){
            const pathReg = 'http://localhost:5000/register'
            const pdata= {
                mname: data.mname,
                memail: data.memail,
                mpwd: data.mpwd
            }
            // console.log(pdata)

            axios.post(pathReg,pdata)
                .then(() => {
                    console.log('Register')
                })
                .catch((error) => {
                    console.log(error)
                })
        },
    },
    components:{
        SignUpForm
    }
}
</script>

<style>

</style>