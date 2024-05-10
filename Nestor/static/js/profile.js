const toggleEditMode = () => {
	const view = document.getElementById("view-profile");
	view.classList.add("hidden");
	const edit = document.getElementById("edit-profile");
	edit.classList.remove("hidden");
}

