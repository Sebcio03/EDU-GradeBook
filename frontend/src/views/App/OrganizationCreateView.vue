<template>
    <main class="flex flex-col items-center justify-center px-6 py-8 mx-auto lg:py-0 w-50">
        <h2 class="text-5xl font-bold leading-tight tracking-tight text-gray-900 md:pt-20 pb-1 text-center">Create New Organization</h2>
        <form @submit.prevent="submitForm" class="pt-5 w-full sm:w-510px">
          <div class="grid gap-4 sm:grid-cols-2 sm:gap-6 mb-6">
              <div class="sm:col-span-2">
                  <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                  <input v-model="form.name" type="text" name="name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Harvard University" required="">
              </div>
              <div class="w-full">
                  <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Address</label>
                  <input v-model="form.address" type="text" name="address" id="address" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Warsaw, Emili Platter 53" required="">
              </div>
              <div class="w-full">
                  <label for="phone_number" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone Number</label>
                  <input v-model="form.phone_number" type="number" name="phoneNumber" id="phoneNumber" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="+48696423510" required="">
              </div>
              <div>
                  <label for="type" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Organization type</label>
                  <select v-model="form.type" id="type" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                      <option value="">Select organization type</option>
                      <option value="C">College</option>
                      <option value="H">High School</option>
                      <option value="E">Elementary School</option>
                  </select>
              </div>
              <div>
                  <label for="country" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Country</label>
                  <select v-model="form.country" id="country" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                      <option value="">Select country</option>
                      <option v-for="c in countries" :key="c.shortcut" :value="c.shortcut">{{ c.fullName }}</option>
                  </select>
              </div>
                <div class="sm:col-span-2">
                    <label for="logo" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">School logo</label>
                    <input @change="(e) => {this.form.logo = e.target.files[0]}" required class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="logo" type="file">
                </div>
              <div class="sm:col-span-2">
                  <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                  <textarea v-model="form.description" id="description" rows="8" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Your description here"></textarea>
              </div>
          </div>
          <ul v-if="errors" class="list-disc capitalize text-red-600 ml-4 mb-5">
            <li class="capitalize" v-for="err in errors" :key="err">{{ err }}</li>
          </ul>

          <button type="submit" class="bg-green-500 hover:bg-blue-80 inline-flex float-right items-right px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 hover:bg-primary-800">
              Create
          </button>
   </form>
    </main>
</template>

<script>
import axios from '../../axios'
import { countries } from '../../assets/countries'
import { object, string, mixed } from 'yup';
import { objToFormData } from '../../utils/tools'

const organizationCreationFormSchema = object({
    name: string().required().min(8).max(255),
    address: string().required().min(4).max(100),
    phone_number: string().label('Phone Number').required().min(6).max(100),
    type: string().label('Organization Type').required(),
    country: string().required(),
    logo: mixed().required().test("fileSize", "The file is too large", (value) => {
        return value.size <= 10 * 1024 * 1024 // Less than 10MB
    }),
    description: string().nullable().notRequired(),
}) 

export default {
    data(){
        return {
            countries: countries,
            errors: [],
            form: {
                name: "",
                address: "",
                phone_number: "",
                type: "",
                country: "",
                logo: {},
                description: ""
            }
        }
    },
    methods: {
        async submitForm(){
            this.errors = []

            try{
                await organizationCreationFormSchema.validate(this.form)
            } catch (err) {
                this.errors = err.errors
                return 
            }

            try{
                const formData = objToFormData(this.form);
                const r = await axios.post('organizations/', formData, {
                    headers: {'Content-Type': 'multipart/form-data'}
                })
                if(r?.status == 201){
                    this.$store.commit("notify", 'Successfully created Organization!', 'success') 
                    this.$router.push({ name:'OrganizationDetail', params: { organizationId: r.data.id }})
                } else {
                    this.errors = Object.values(r.response.data).flatMap(arrOfErrors => arrOfErrors)
                }
            } catch (err) {
                console.log(err)
                if(err.status != 500){
                    this.errors = Object.values(err.data).flatMap(arrOfErrors => arrOfErrors)
                }          
                this.errors = ["Something bad happened, try again later!"]
            }
        }
    }
}
</script>

<style>

</style>