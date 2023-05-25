
//? Agrego un event listener a los botones para editar la tarea 
const tasksEditBtns = document.querySelectorAll("#edit");
tasksEditBtns.forEach(btn => btn.addEventListener("click", editDescription));

function editDescription(){
    const toDo = this.parentElement;
    const editBtn = this;
    const saveBtn = toDo.querySelector("#save");
    const description = toDo.querySelector("#todo-description");

    editBtn.style.display = "none";
    saveBtn.style.display = "inline-block";
    description.removeAttribute("readonly");
    description.focus();
};

//? Agrego un event listener a los input text de la descripcion de la tarea 
const description = document.querySelectorAll("#todo-description");
description.forEach(desc => desc.addEventListener("keydown", (event) => {
	if (event.key == "Enter") {
        event.preventDefault();
	};
}));