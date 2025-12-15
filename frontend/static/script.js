// Load options when page loads
//console.log("Script loaded");
fetch("/get-categories")
    .then(response => response.json())
    .then(categories => {
        //console.log("Categories received:", categories);
        const dropdown = document.getElementById("categories");
        categories = categories.categories;  // Adjusted to access the categories array from JSON response
        categories.forEach(element => {
            const category = document.createElement("option");
            category.value = element;
            category.textContent = element;
            dropdown.appendChild(category);
        });
    })
    .catch(error => console.error('Error:', error));
fetch("/get-types")
    .then(response => response.json())
    .then(types => {
        const dropdown = document.getElementById("types");
        types = types.types;
        types.forEach(element => {
            const type = document.createElement('option');
            type.value = element;
            type.textContent = element;
            dropdown.appendChild(type);
        });
    })
    .catch(error => console.error('Error:', error));

const generateBtn = document.getElementById("select-dish-btn");
// Send the selected value when button is clicked
generateBtn.addEventListener("click", async () => {
    //console.log("Button clicked");
    // add button hightlight effect
    generateBtn.classList.add("selected");
    // Remove highlight after a short delay for effect
    setTimeout(() => {
        generateBtn.classList.remove("selected");
    }, 200);
    const selectedCategory = document.getElementById('categories').value;
    const selectedType = document.getElementById('types').value;
    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body : JSON.stringify({category: selectedCategory,
                            type: selectedType
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("dish-result").innerText = 'Selected dish: ' + data.selected_dish;
    })
    .catch(error => console.error('Error:', error));
    });

const likeCheckbox = document.getElementById("choice");
likeCheckbox.addEventListener("change", () => {
    const dish = document.getElementById("dish-result").innerText.replace('Selected dish: ', '');
    fetch("/like-choice", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body : JSON.stringify({liked: likeCheckbox.checked, dish:dish})
    })
});