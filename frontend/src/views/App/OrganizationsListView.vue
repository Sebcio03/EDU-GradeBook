<template>
    <main class="flex flex-col items-center justify-center px-6 py-8 mx-auto lg:py-0">
        <h2 class="text-5xl font-bold leading-tight tracking-tight text-gray-900 md:pt-20 mb-10">Your Organizations</h2>
        <router-link :to="{name: 'OrganizationCreate'}" class="mb-10 w-64 text-center text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
            <span>Create New</span>
        </router-link>
        <div v-if="organizations.length">
            <ul role="list" class="divide-y divide-neutral-400 bg-gray-800 px-10 py-5 rounded-lg">
                <li v-for="organization in organizations" :key="organization.id" class="my-1 sm:py-4">
                <router-link :to="{ name:'OrganizationDetail', params: { organizationId: organization.id }}">
                    <div class="flex items-center space-x-4">
                        <div class="flex-shrink-0">
                            <img class="w-8 h-8 rounded-full" :src="organization.logo" alt="">
                        </div>
                        <div class="flex-1 min-w-0">
                            <p class="text-sm font-medium truncate text-white">
                                {{ organization.name }}
                            </p>
                            <p class="text-sm truncate text-gray-300">
                                {{ organization.type }}
                            </p>
                        </div>
                        <div class="pl-10 inline-flex items-center text-base font-semibold text-white">
                            {{ organization.user_type }}
                        </div>
                    </div>
                </router-link>
                </li>
            </ul>
        </div>
        <div v-else class="flex flex-col items-center">
            <p class="py-5">You are not assigned to any organization</p>
        </div>
    </main>
</template>

<script>
import axios from '../../axios'
import AppNav from '../../components/App/Nav.vue'

export default {
    components: {AppNav},
    data(){
        return {
            organizations: []
        }
    },
    mounted() {
        axios.get('/organizations/')
          .then((res) => {this.organizations = res.data})
    }
}
</script>