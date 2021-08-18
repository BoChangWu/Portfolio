<template>
    <div id="contact">
        <ContactForm :company="company" @send-data="dataChange" />
    </div>
</template>

<script>
import ContactForm from '@/components/ContactForm.vue'
export default {
    name: 'Contact',    
    data(){
        company:{}
        
    },
    created(){
        this.company={
            name: '',
            subject: '',
            phone: '',
            mobile: '',
            email: '',
            message: ''
        }
    },
    methods:{
        dataChange(company){
            console.log(company)
        }
    },
    components:{
        ContactForm
    }
}
</script>

<style>

</style>