<template>
    <div id="contact">
        <ContactForm :cmsg="cmsg" @send-data="onSubmit" />
    </div>
</template>

<script>
import axios from 'axios'
import ContactForm from '@/components/ContactForm.vue'
export default {
    name: 'Contact',    
    data(){
        return{
            cmsg:{
                cname: '',
                csubject: '',
                cphone:'',
                cemail:'',
                cmessage:''
            }
        }
        
    },
    created(){

    },
    methods:{
        sendMsg(data){
            // console.log(addmsg)
            const path = 'http://localhost:5000/sendtext'
            axios.post(path,data)
                .then(() => {
                    console.log('sent')
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        onSubmit(){
            
            var smsg={
                cname: this.cmsg.cname,
                csubject : this.cmsg.csubject,
                cphone : this.cmsg.cphone,
                cemail : this.cmsg.cemail,
                cmessage : this.cmsg.cmessage
            }
            // console.log(this.cmsg)
            // console.log(smsg)
            this.sendMsg(smsg)
            // this.initForm()
        },
    },
    components:{
        ContactForm
    }
}
</script>

<style>

</style>