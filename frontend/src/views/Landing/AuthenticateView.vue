<template lang="">
    <LandingNav/>
    <div class="grid place-items-center h-screen w-screen p-5 md:p-20">
        <div class="flex flex-row max-w-6xl">
            <router-view></router-view>
            <div class="hidden md:block pl-10">
                <img class="object-cover w-full h-full" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop" alt="img" />
            </div>
        </div>
    </div>
</template>
<script>
import LandingNav from '../../components/Landing/Nav.vue'

export default {
    components: {LandingNav}
}
</script>
<style lang="">
    
</style>