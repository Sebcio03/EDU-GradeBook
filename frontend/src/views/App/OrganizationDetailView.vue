<template>
    <div v-if="organization">
        <div class="pt-10 md:pt-20">
            <p class="hidden">Organization</p>
            <div class="flex align-items-center  pb-2">
                <img class="w-7 h-7  md:w-12 md:h-12 rounded-full" :src="organization.logo" alt="">
                <h2 class="font-bold leading-tight text-2xl md:text-5xl  w-full tracking-tight text-gray-900 ml-4">{{ organization.name }}</h2>
            </div>
            <dl class="flex items-center space-x-6 pt-5 text-sm md:text-base">
                <div>
                    <dt class="mb-2 font-semibold leading-none text-gray-900">Phone Number</dt>
                    <dd class="mb-4 font-light text-gray-500 sm:mb-5 ">{{ organization.phone_number }}</dd>
                </div>
                <div>
                    <dt class="mb-2 font-semibold leading-none text-gray-900 ">Address</dt>
                    <dd class="mb-4 font-light text-gray-500 sm:mb-5 ">{{ organization.address }}</dd>
                </div>
            </dl>
        </div> 
    </div>
    <main v-else class="flex flex-col items-center justify-center px-6 py-8 mx-auto lg:py-0 w-50">
        <p class="text-xl pt-40 text-center">{{ err }}</p>
    </main>
</template>
<script>
import axios from '../../axios'

export default {
    data(){
        return {
            organization: null,
            err: null
        }
    },
    async mounted(){
        const r = await axios.get(`organizations/${this.$route.params.organizationId}/`)
        if (r.status == 200){
            this.organization = r.data
        } else if (r?.response.status == 404){
            this.err = "Organization does not exists"
        } else {
            this.err = "Something bad happened please try again later."
        }
    },
}
</script>

<style>

</style>