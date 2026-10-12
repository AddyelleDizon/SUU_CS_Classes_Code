var points = 0

function populateDropdown(){
    const dropdown = document.getElementById("myDropdown")
    const optionsData = [
    {text: "Accounting", value: "Accounting"},
    {text: "Agriculture", value: "Agriculture"},
    {text: "Anthropology", value: "Anthropology"},
    {text: "Area/Group Studies", value: "Area/Group Studies"},
    {text: "Art & Art History", value: "Art & Art History"},
    {text: "Arts Administration", value: "Arts Administration"},
    {text: "Aviation", value: "Aviation"},
    {text: "Biology", value: "Biology"},
    {text: "Business", value: "Business"},
    {text: "Chemistry", value: "Chemistry"},
    {text: "Communication", value: "Communication"},
    {text: "Computer Science", value: "Computer Science"},
    {text: "Construction", value: "Construction"},
    {text: "Criminal Justice", value: "Criminal Justice"},
    {text: "Cybersecurity", value: "Cybersecurity"},
    {text: "Dance", value: "Dance"},
    {text: "Data Science", value: "Data Science"},
    {text: "Economics", value: "Economics"},
    {text: "Education", value: "Education"},
    {text: "Engineering", value: "Engineering"},
    {text: "English", value: "English"},
    {text: "Environmental Studies", value: "Environmental Studies"},
    {text: "Exercise Science", value: "Exercise Science"},
    {text: "Family Life & Human Development", value: "Family Life & Human Development"},
    {text: "Film", value: "Film"},
    {text: "Finance", value: "Finance"},
    {text: "General Studies", value: "General Studies"},
    {text: "Geography", value: "Geography"},
    {text: "Geology", value: "Geology"},
    {text: "Graphic Design", value: "Graphic Design"},
    {text: "Health Sciences", value: "Health Sciences"},
    {text: "History", value: "History"},
    {text: "Hospitality Management", value: "Hospitality Management"},
    {text: "Information Technology", value: "Information Technology"},
    {text: "Interdisciplinary Studies", value: "Interdisciplinary Studies"},
    {text: "Languages", value: "Languages"},
    {text: "Leadership", value: "Leadership"},
    {text: "Library Media/School Library", value: "Library Media/School Library"},
    {text: "Management", value: "Management"},
    {text: "Marketing", value: "Marketing"},
    {text: "Mathematics", value: "Mathematics"},
    {text: "Military Science", value: "Military Science"},
    {text: "Music", value: "Music"},
    {text: "Nursing", value: "Nursing"},
    {text: "Nutrition", value: "Nutrition"},
    {text: "Outdoor Recreation", value: "Outdoor Recreation"},
    {text: "Philosophy", value: "Philosophy"},
    {text: "Physical Education", value: "Physical Education"},
    {text: "Physics", value: "Physics"},
    {text: "Political Science", value: "Political Science"},
    {text: "Psychology", value: "Psychology"},
    {text: "Public Administration", value: "Public Administration"},
    {text: "Secondary Education", value: "Secondary Education"},
    {text: "Social Studies", value: "Social Studies"},
    {text: "Social Work", value: "Social Work"},
    {text: "Sociology", value: "Sociology"},
    {text: "Software Development", value: "Software Development"},
    {text: "Sports", value: "Sports"},
    {text: "Theatre", value: "Theatre"}
    ]

    optionsData.forEach((item) => {
        const option = document.createElement("option")
        option.value = item.value
        option.textContent = item.text
        dropdown.appendChild(option)
    })
}

function populateHogwarts(){
    const dropdown = document.getElementById("hogwartsHouse")
    const optionsData = [
    {text: "Gryffindor", value: "Gryffin"},
    {text: "Hufflepuff", value: "Huffle"},
    {text: "Ravenclaw", value: "Raven"},
    {text: "Slytherin", value: "Slyther"},
    ]

    optionsData.forEach((item) => {
        const option = document.createElement("option")
        option.value = item.value
        option.textContent = item.text
        dropdown.appendChild(option)
    })
}

function characterOptions(){
    const optionsData = [
    {text: "Harry Potter", value: "H. Potter"},
    {text: "Hermione Granger", value: "H. Granger"},
    {text: "Albus Dumbledore", value: "A. Dumbledore"},
    {text: "Cho Chang", value: "C. Chang"},
    {text: "Luna Lovegood", value: "L. Lovegood"},
    {text: "Draco Malfoy", value: "D. Malfoy"},
    {text: "A character not listed", value: "Other"},
    ]

    const character = document.getElementById("favCharacter")

    optionsData.forEach(option => {
        const radioInput = document.createElement("input")
        radioInput.type = "radio"
        radioInput.name = "Favorite Character"
        radioInput.value = option.value
        radioInput.id = option

        const label = document.createElement("label")
        label.htmlFor = radioInput.id
        label.textContent = option.text

        character.appendChild(radioInput)
        character.appendChild(label)
        character.appendChild(document.createElement("br"))
    })
}

function getDate(){
    const today = new Date()

    const yyyy = today.getFullYear()
    const mm = String(today.getMonth() + 1).padStart(2, '0')
    const dd = String(today.getDate()).padStart(2, '0')

    const formattedDate = `${yyyy}-${mm}-${dd}`

    document.getElementById("moveIn").value = formattedDate
}

function setDateToToday(date, maxormin){
    const today = new Date()

    const yyyy = today.getFullYear()
    const mm = String(today.getMonth() + 1).padStart(2, '0')
    const dd = String(today.getDate()).padStart(2, '0')

    const formattedDate = `${yyyy}-${mm}-${dd}`

    document.getElementById(date).setAttribute(maxormin, formattedDate)
}

function setMonthMax(dateId){
    const today = new Date()

    const yyyy = today.getFullYear()
    const mm = String(today.getMonth() + 1).padStart(2, '0')

    const formattedDate = `${mm}-${yyyy}`

    var newMonth = document.getElementById(dateId)
    newMonth.value = formattedDate
}

function setDayMax(monthId, dayId){
    const input = document.getElementById(dayId)
    const today = new Date()

    if (today == 'April' || today == 'June' || today == 'September' || today == 'November'){
        input.setAttribute("max", 30)
    }
    else if (today == 'January' || today == 'March' || today == 'May' || today == 'July' || today == 'August' || today == 'October' || today == 'December'){
        input.setAttribute("max", 31)
    }
    else {
        input.setAttribute("max", 30)
    }
}

function getRandom(arr){
    const rand = Math.floor(Math.random()*arr.length)
    return arr[rand]
}

function randomName(){
    const fNames = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    const lNames = ["Smith", "Johnson", "Lee", "Brown", "Garcia", "Davis"]
    document.getElementById("fName").value = getRandom(fNames)
    document.getElementById("lName").value = getRandom(lNames)
}

function randomMajor(){
    const dropdown = document.getElementById('myDropdown')
    const numOptions = dropdown.options.length
    const randomIndex = Math.floor(Math.random() * numOptions)
    dropdown.selectedIndex = randomIndex
}

function randomStudent(){
    randomName()
    randomMajor()
    getDate()
}

function cbClicked(id, p){
    var cbChecked = document.getElementById(id)
    if (cbChecked.checked){
        points += p
    }
    else{
        points -= p
    }

    document.getElementById("points").value = "Completion Score: " + points
}

function gClicked(){
    var f = document.getElementById("g")
    var userTyped = f.value
    document.getElementById("totalParagraph").innerHTML = userTyped
}

function validateSchoolEmail(formId, schoolId){
    const form = document.getElementById(formId)
    form.addEventListener("submit", function(event) {
        const school = document.getElementById(schoolId).value
        let valid = true

        if (!school.includes(".")) {
            alert("Both emails need a period.")
            valid = false
        }

        if (!school.endsWith(".edu")) {
            alert("School email has to end in .edu.")
            valid = false
        }

        if (!valid) {
            event.preventDefault()
        }
    })
}

function validatePersonalEmail(formId, personalId){
    const form = document.getElementById(formId)
    form.addEventListener("submit", function(event) {
        const personal = document.getElementById(personalId).value

        let valid = true

        if (!personal.includes(".")) {
            alert("Both emails need a period.")
            valid = false
        }

        if (personal.endsWith(".edu")) {
            alert("Personal email cannot end in .edu.")
            valid = false
        }

        if (!valid) {
            event.preventDefault()
        }
    })
}

function preserveFormData(formId) {
    const form = document.getElementById(formId)
    const urlParams = new URLSearchParams(window.location.search)
    const inputs = form.querySelectorAll("input, select, textArea")

    inputs.forEach(input=>{
        if (urlParams.has(input.name)){
            input.value = urlParams.get(input.name)
            if (input.type === "checkbox" || input.type === "radio"){
                input.checked = urlParams.get(input.name) === input.value
            }
        }
    })

    for (const [key, value] of urlParams.entries()) {
        if (!form.querySelector(`[name="${key}"]`)) { 
            const hidden = document.createElement("input")
            hidden.type = "hidden"
            hidden.name = key
            hidden.value = value
            form.appendChild(hidden)
        }
    }

    form.addEventListener("submit", () => {
        inputs.forEach(input => {
            if (input.name && !urlParams.has(input.name)){
                const hidden = document.createElement("input")
                hidden.type = "hidden"
                hidden.name = key
                hidden.value = value
                form.appendChild(hidden)
            }
        })
    })
}

function verifySecretCode(inputId, correctCode) {
    const input = document.getElementById(inputId)
    const correct = document.getElementById(correctCode)

    if (!input) return

    function checkCode() {
        if (input.value.trim() === correct.value.trim()) {
            input.style.border = "3px solid green"
        } else {
            input.style.border = "3px solid red"
            alert("Incorrect secret code! Please try again.")
        }
    }

    input.addEventListener("blur", checkCode) 
    input.form.addEventListener("submit", event => {
        if (input.value.trim() !== correct.value.trim()) {
            event.preventDefault()
            checkCode()
        }
    })
}

function dumpAllData(containerId) {
    const container = document.getElementById(containerId)
    const params = new URLSearchParams(window.location.search)

    let html = "<h2 id='stuInfo'>Your SUU Student Data:</h2><ul>"
    for (const [key, value] of params.entries()) {
        html += `<li><strong>${key}</strong>: ${value}</li>`
    }
    html += "</ul>"

    container.innerHTML = html
}