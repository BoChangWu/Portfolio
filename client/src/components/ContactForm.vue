<template>
    <form action="" id="contact">
        <input type="text" id="name" placeholder="姓名" v-model="name" >
        <br>
        <input type="text" id="subject" placeholder="公司" v-model="subject" >
        <br>
        <input type="text" id="phone" placeholder="phone:XX-XXXXXXXX" v-model="phone" >
        <br>
        <input type="text" id="mobile" placeholder="mobile:09XX-XXXXXX"  v-model="mobile" >
        <br>
        <input type="text" id="email" placeholder="XXXXXXXX@gmail.com" v-model="email" >
        <br>
        <textarea name="" id="message" cols="30" rows="10" placeholder="leave your message" v-model="message" tabIndex="5"></textarea><br>
        

        <button tabIndex="6">SUBMIT</button>
    </form>
    
</template>

<script>
export default {
    name:'ContactForm',
    data(){
        return{
            name:'Test',
            subject:'',
            phone: '',
            mobile:'',
            email:'',
            message:''
        }
    },
    methods:{
        
    },
    created(){
        $(document).on('keypress', 'input', function (e) {
            if(e.which==13){
                e.preventDefault()
                // console.log(this)
                $(this).next().next().focus()
            }
        })
    }
}


</script>

<style scoped>
#message{
    width: 300px;
    margin: 20px;
}
input{
    width: 300px;
    height: 30px;
    margin: 20px;
}
#contact{
    margin: auto;
    width: 400px;
    padding: 20px;
}
#contact{
    background-color: #42b983;
}
</style>