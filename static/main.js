const {createApp} = Vue
const TaskApp = {

    data() {
        return {
            task: {
                'title': ''
            },
            tasks: [],
            selected: '',
            age: '',
            mileage: '',
            repairments: '',
            checked: false,
            brand_price: '',
            brands: [],
            car: {}
        }
    },
    async created() {
        await this.getTasks()
        await this.getBrands()
    },
    methods: {
        async sendRequest(url, method, data) {
            const myHeaders = new Headers({
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            })

            const response = await fetch(url, {
                method: method,
                headers: myHeaders,
                body: data
            })

            return response
        },
        async getBrands() {
            const response = await this.sendRequest(window.location + 'brands', 'get')
            this.brands = await response.json()
        },
        async getTasks() {
            const response = await this.sendRequest(window.location, 'get')
            this.tasks = await response.json()

        },
        async createTask() {
            if (this.task.title === '' || this.task === null || this.task.value === 0
                || this.age === '' || this.age === null || this.age.value === 0
                || this.mileage === '' || this.mileage === null || this.mileage.value === 0
                || this.repairments === '' || this.repairments === null || this.repairments.value === 0) {
                alert('Please fill all the fields');
            } else {
                alert(this.age + ' ' + this.mileage + ' ' + this.repairments)
                this.car = {
                    taskTitle: this.task.title,
                    age: this.age,
                    mileage: this.mileage,
                    repairments: this.repairments,
                    brand_price: this.brand_price,
                    documents: this.checked
                }
                this.printCar(this.car)

                await this.getTasks()

                await this.sendRequest(window.location + 'create', 'post', JSON.stringify(this.task))//todo return not this.task but this.car

                await this.getTasks()

                this.task = ''
                this.age = ''
                this.mileage = ''
                this.repairments = ''
                this.car = {}
            }
        },
        async deleteTask(task) {
            await this.sendRequest(window.location + 'delete', 'post', JSON.stringify(task))
            await this.getTasks()
        },
        async completeTask(task) {
            await this.sendRequest(window.location + 'complete', 'post', JSON.stringify(task))
            await this.getTasks()
        },
        validateNumber: (event) => {
            let keyCode = event.keyCode;
            if (keyCode < 48 || keyCode > 57) {
                event.preventDefault();
            }
        },
        printCar(Car) {
            console.log('Task title is ' + Car.taskTitle)
            console.log('Car age is ' + Car.age)
            console.log('Car mileage is ' + Car.mileage)
            console.log('Car repairments number is ' + Car.repairments)
            console.log('Car brand price is ' + Car.brand_price)
            console.log('Car documents check is ' + Car.documents)
        }
    },
    delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')
