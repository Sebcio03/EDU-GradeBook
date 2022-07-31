<template lang="">
    <nav class="sm:px-4 py-2.5 rounded dark:bg-gray-900 fixed w-full px-3">
        <div class="container flex flex-wrap justify-between items-center mx-auto">
            <a href="/" class="flex items-center">
                <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">EDU</span>
            </a>
            <div class="flex md:order-2">
                <router-link :to="{name:'Login'}" class="ml-4 text-white bg-blue-700 hover:bg-blue-800 hover:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Login</router-link>
                <router-link :to="{name:'Register'}" class="ml-4 text-white bg-blue-700 hover:bg-blue-800 hover:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Get started</router-link>
            </div>
        </div>
    </nav>
</template>