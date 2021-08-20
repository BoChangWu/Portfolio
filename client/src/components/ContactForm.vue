<template>
    <form action="" id="contact">
        <input type="text" id="name" placeholder="姓名" v-model="cmsg.cname" >
        <br>
        <input type="text" id="subject" placeholder="公司" v-model="cmsg.csubject" >
        <br>
        <input type="text" id="phone" placeholder="phone number" v-model="cmsg.cphone" >
        <br>
        <input type="text" id="email" placeholder="XXXXXXXX@gmail.com" v-model="cmsg.cemail" >
        <br>
        <textarea name="" id="message" cols="30" rows="10" placeholder="leave your message" v-model="cmsg.cmessage" tabIndex="5"></textarea><br>
        

        <button tabIndex="6" @click="sendData">SUBMIT</button>
    </form>
    
</template>

<script>

export default {
    name:'ContactForm',
    props:{
        cmsg: Object
    },
    methods:{
        sendData(evt){
            evt.preventDefault()
            this.$emit('send-data',this.cmsg)
        }
    },
    created(){
        $(document).on('keypress', 'input', function (e) {
            if(e.which==13){
                e.preventDefault()
                // console.log(this)
                $(this).next().next().focus()
            }
        })
        // this.initForm()

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