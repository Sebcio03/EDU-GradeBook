<template lang="">
    <form @submit.prevent="onSubmit" class="flex flex-col justify-center">
        <h1 class="md:w-96 mb-10 text-3xl font-semibold text-gray-800 dark:text-white">Login to your EDU account!</h1>
        <div class="mb-6 md:w-96">
            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Email address</label>
            <input type="email" id="email" v-model="form.email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="john.doe@company.com" required="">
        </div> 
        <div class="mb-6 md:w-96">
            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Password</label>
            <input type="password" id="password" v-model="form.password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required="">
        </div> 
        <ul v-if="errors" class="list-disc capitalize text-red-600 ml-4 mb-5">
            <li v-for="err in errors" :key="err">{{ err }}</li>
        </ul>
        <button type="submit" class="md:w-96 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Login</button>
    </form>
</template>

<script>
import axios from '../../../axios/'

export default{
    data(){
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {  
        onSubmit(){
            return axios.post('/users/signin/', this.form)
                .then((res) => {
                    this.errors = []
                    this.$store.commit("notify", 'Successfully signed in!', 'success') 
                    this.$router.push({ name: 'OrganizationsList' })              
                })
                .catch((res) => {
                    if (res.response) {
                        if (res.response.status){
                            this.errors = [].concat(...Object.values(res.response.data))
                        } else {
                            this.errors = ['Unexpected error happend']
                        }
                    }
                })
        }
    },
}
</script>

<style lang="">
    
</style>