<template lang="">
    <form @submit.prevent="onSubmit" class="max-w-md m-auto justify-center">
        <h1 class="md:w-96 mb-10 text-3xl font-semibold text-gray-800 dark:text-white">Create your EDU account!</h1>
        <div class="grid gap-6 mb-6 md:grid-cols-2 md:w-96">
            <div>
                <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">First name</label>
                <input type="text" id="first_name" v-model="form.first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required=""/>
            </div>
            <div>
                <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Last name</label>
                <input type="text" id="last_name" v-model="form.last_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required=""/>
            </div>

        </div>
        <div class="mb-6 md:w-96">
            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Email address</label>
            <input type="email" id="email" v-model="form.email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="john.doe@company.com" required=""/>
        </div> 
        <div class="mb-6 md:w-96">
            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Password</label>
            <input type="password" id="password" v-model="form.password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required=""/>
        </div> 
        <div class="mb-6 md:w-96">
            <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Confirm password</label>
            <input type="password" id="confirm_password" v-model="form.confirm_password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required=""/>
        </div> 
        <div class="flex items-start mb-6 md:w-96">
            <div class="flex items-center h-5">
            <input id="agree_with_terms" v-model="form.agree_with_terms" type="checkbox" value="" class="w-4 h-4 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800" required=""/>
            </div>
            <label for="agree_with_terms" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-400">I agree with the <a href="#" class="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>
        </div>
        <ul v-if="errors" class="list-disc capitalize text-red-600 ml-4 mb-5">
            <li v-for="err in errors" :key="err">{{ err }}</li>
        </ul>
        <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Get started!</button>
    </form>
</template>

<script>
import axios from '../../../axios/'

export default{
    data(){
        return {
            form: {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                confirm_password: '',
                agree_with_terms: false
            },
            errors: []
        }
    },
    methods: {  
        onSubmit(){
            console.log(this)
            axios.post('/users/signup/', this.form)
                .then((res) => {
                    this.errors = []
                    this.$store.commit("notify", 'Successfully signed up! Please login!', 'success') 
                    this.$router.push({ name: 'Login' })
                })
                .catch((res) => {
                    if (res.response) {
                        console.log(res.response)
                        if (res.response.status == 400){
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