let pet = {
    name: name,
    hunger: 50,
    happiness: 50,
    energy: 100
};

function updatePetStatus(){
document.getElementById("hunger").textContent = 'Hunger: ${pet.hunger}';
document.getElementById("happiness").textContent = 'Happiness: ${pet.happiness}';
document.getElementById("Energy").textContent = 'Energy: ${pet.energy}';
}

//Function to feed
function feedPet(){
   if (pet.hunger > 0) {
    pet.hunger -= 10;
    if (pet.hunger < 0) {
      pet.hunger = 0;
    }
    pet.happiness += 5;
    if (pet.happiness > 100) {
      pet.happiness = 100;
    }
    updatePetStats();
    alert(`${pet.name} has been fed!`);
  } else {
    alert(`${pet.name} is not hungry.`);
  }
}

function animatePlay(){
    pet.energy -= 10;
    if(pet.energy < 0){
    pet.energy = 0;
    }
    updatePetStats();

    const petElement = document.getElementById("pet");
    petElement.classList.add("pet-playing");
    setTimeout(() => {
        petElement.classList.remove("pet-playing")
    }, 1000);
}

function playWithPet(){
    if (pet.energy >= 10){}
    pet.happiness += 10;
    if (pet.happiness > 100){
        pet.happiness = 100;
    }
    pet.energy -= 10;
    updatePetStats();
    animatePlay();
    setTimeout(() => {
    alert("Playing with ${pet.name}!");
    }, 1000);
   }else{
    alert("${pet.name} is too tired to play.")
   }
}

updatePetStats();