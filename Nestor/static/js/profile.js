const toggleEditMode = () => {
	const view = document.getElementById("view-profile");
	view.classList.add("hidden");
	const edit = document.getElementById("edit-profile");
	edit.classList.remove("hidden");
}

const toggleEditContactInfo = () => {
	const view = document.getElementById("contact-info-view");
	view.classList.add("hidden");
	const edit = document.getElementById("contact-info-edit");
	edit.classList.remove("hidden");
}