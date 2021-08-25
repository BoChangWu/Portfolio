<template>
    <div id="trylogin">
        <h2>This page is just show you how I connect frontend with Server and DataBase</h2>
        <LoginForm class="login" @sign-in="tryLogin"  @sign-up="register" :mdata="member" />
    </div>
</template>

<script>
import axios from 'axios'
import LoginForm from '@/components/LoginForm.vue'
export default {
    name:'TryLogin',
    data(){
        return{
            member:{
                mname: '',
                memail: '',
                mpwd: ''
            },
            members:[]
        }
    },
    methods:{
        tryLogin(data){
            const pathLog = 'http://localhost:5000/login'
            axios.post(pathLog,data)
                .then(() => {
                    console.log('login')
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        register(data){
            const pathReg = 'http://localhost:5000/register'
            axios.post(pathReg,data)
                .then(() => {
                    console.log('Register')
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        showMembers(){
            const pathShow = 'http://localhost:5000/showmembers'
            axios.get(pathShow)
                .then((res) => {
                    this.members = res.data;
                    console.log(res.data)
                })
                .catch((error)=> {
                    console.log(error)
                })
        },
        hideLogin(){
            console.log($(this).parent())
            // $(this).parent().$route.push('/') 
            // $('.login').css('display','none')
            
        }
    },
    components:{
        LoginForm,
    }
}
</script>

<style>
    .login{
        display: none;
    }
</style>