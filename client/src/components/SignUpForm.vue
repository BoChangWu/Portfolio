<template>
    <div id="signup">
        <form action="">
            <div id="inputarea">
            <input type="text" id="name" placeholder="Name" v-model="mname"> 
            <br>
            <input type="text" id="email" placeholder="Email" v-model="memail">            
            <br>
            <input type="password" id="pwd" placeholder="Password" v-model="mpwd">
            </div>
            <div id="buttonarea">
                <button @click="registerGo">Sign up</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name:'SignUpForm',
    props:{
        mname: String,
        memail: String,
        mpwd: String
    },
    methods:{
        registerGo(evt){
            evt.preventDefault()
            const mdata = {
                mname: this.mname,
                memail: this.memail,
                mpwd: this.mpwd
            }
            this.$emit('register-go', mdata)
        }
    }
}
</script>

<style scoped>
#signup{
    margin-top: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
}
form{
    border-radius: 10px;
    width: 40%;
    height: 500px;
    background-color: #42b983;
}

input{
    border: none;
    border-radius: 5px;
    width: 200px;
    height: 30px;
    margin: 20px;
}
#inputarea{
    margin-top: 150px;
}
#buttonarea{
    margin-top: 30px;
}
button{
    border: none;
    margin: 20px;
    width: 80px;
    height: 40px;
    background-color: #73efb5;
    border-radius: 10px;
}
button:hover{
    background-color: #2c3e50;
    color: #fff;
    transform: scale(110%);
}
</style>